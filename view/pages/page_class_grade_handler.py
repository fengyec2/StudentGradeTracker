import os
import json
from collections import defaultdict

from PySide6.QtWidgets import QTableWidgetItem, QListWidgetItem, QVBoxLayout, QLabel
from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PySide6.QtGui import QPainter, QFont
from PySide6.QtCore import Qt, QTimer

from common.utils import show_dialog, load_exam_meta, ExamListModel

DATA_DIR = "data"
STUDENTS_DIR = os.path.join(DATA_DIR, "students")


class PageClassGradeHandler:
    def __init__(self, ui):
        self.ui = ui
        self._exam_model = None
        self.init_ui()

    def init_ui(self):
        self.refresh()
    
    def refresh(self):
        """刷新考试下拉框和班级列表"""
        self.load_exam_list()
        self.load_class_list()

    def load_exam_list(self):
        """采用统一模型方式加载考试列表"""
        try:
            meta = load_exam_meta()
            # 倒序显示（最新在上）
            exams = sorted(meta.get("exams_order", []), key=lambda e: e["real_date"], reverse=True)
            self._exam_model = ExamListModel(exams)
        except Exception as e:
            show_dialog(self.ui, f"加载考试元数据失败：{e}")
            self._exam_model = ExamListModel([])

        self.ui.comboExam.clear()
        for i in range(self._exam_model.rowCount()):
            exam = self._exam_model.get_exam(i)
            self.ui.comboExam.addItem(exam["display_name"], userData=exam["filename"])

    def load_class_list(self):
        """动态加载学生班级列表，如果目录不存在则创建"""
        if not os.path.exists(STUDENTS_DIR):
            os.makedirs(STUDENTS_DIR, exist_ok=True)

        class_set = set()
        for file in os.listdir(STUDENTS_DIR):
            if file.endswith(".json"):
                try:
                    with open(os.path.join(STUDENTS_DIR, file), "r", encoding="utf-8") as f:
                        student = json.load(f)
                        cls = student.get("class", "").strip()
                        if cls:
                            class_set.add(cls)
                except Exception:
                    continue  # 忽略无法解析的学生文件

        self.ui.listClasses.clear()
        for cls in sorted(class_set, key=lambda x: int(x) if x.isdigit() else x):
            item = QListWidgetItem(f"{cls}班")
            item.setData(0x0100, cls)
            item.setSelected(True)
            self.ui.listClasses.addItem(item)

    def on_query_clicked(self):
        selected_exam_index = self.ui.comboExam.currentIndex()
        if selected_exam_index < 0:
            show_dialog(self.ui, "请选择考试")
            return

        filename = self.ui.comboExam.currentData()
        selected_classes = [item.data(0x0100) for item in self.ui.listClasses.selectedItems()]
        if not selected_classes:
            show_dialog(self.ui, "请选择班级")
            return

        results = defaultdict(lambda: defaultdict(list))  # class -> subject -> [score]
        for file in os.listdir(STUDENTS_DIR):
            if file.endswith(".json"):
                path = os.path.join(STUDENTS_DIR, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        student = json.load(f)
                        student_class = student.get("class")
                        if student_class not in selected_classes:
                            continue
                        for exam in student.get("exams", []):
                            if exam.get("filename") == filename:
                                for subj in exam.get("subjects", []):
                                    subject = subj.get("subject")
                                    score = subj.get("score", 0)
                                    results[student_class][subject].append(score)
                except Exception:
                    continue

        # 计算平均分
        table_data = []
        subject_set = set()
        for cls, subj_scores in results.items():
            row = {"班级": f"{cls}班"}
            total = 0
            count = 0
            for subj, scores in subj_scores.items():
                avg = round(sum(scores) / len(scores), 2) if scores else 0
                row[subj] = avg
                total += sum(scores)
                count += len(scores)
                subject_set.add(subj)
            row["平均分"] = round(total / count, 2) if count else 0
            table_data.append(row)

        self.populate_table(table_data, subject_set)
        self.populate_chart(table_data, subject_set)

        # 年级平均分
        all_avg = [row["平均分"] for row in table_data if "平均分" in row]
        grade_avg = round(sum(all_avg) / len(all_avg), 2) if all_avg else 0
        self.ui.labelStats.setText(f"年级平均分：{grade_avg}")

    def populate_table(self, data, subjects):
        headers = ["班级"] + sorted(subjects) + ["平均分"]
        self.ui.tableScores.clear()
        self.ui.tableScores.setColumnCount(len(headers))
        self.ui.tableScores.setHorizontalHeaderLabels(headers)
        self.ui.tableScores.setRowCount(len(data))
        for row_idx, row in enumerate(data):
            for col_idx, key in enumerate(headers):
                val = row.get(key, "")
                item = QTableWidgetItem(str(val))
                self.ui.tableScores.setItem(row_idx, col_idx, item)

    def populate_chart(self, data, subjects):
        # 清理旧图表
        layout = self.ui.widgetChart.layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                widget = child.widget()
                if widget:
                    widget.deleteLater()
        else:
            layout = QVBoxLayout(self.ui.widgetChart)
            self.ui.widgetChart.setLayout(layout)

        subjects = sorted(subjects)
        series = QBarSeries()
        
        # 存储所有数据用于后续添加标签
        chart_data = []
        class_names = []
        
        for row in data:
            bar_set = QBarSet(row["班级"])
            row_values = []
            for subj in subjects:
                value = row.get(subj, 0)
                bar_set.append(value)
                row_values.append(value)
            series.append(bar_set)
            chart_data.append(row_values)
            class_names.append(row["班级"])

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("各班级各科平均分")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # 创建坐标轴
        axis_x = QBarCategoryAxis()
        axis_x.append(subjects)
        
        axis_y = QValueAxis()
        # 设置Y轴范围，留出空间显示数值标签
        max_score = 0
        for row_values in chart_data:
            if row_values:
                max_score = max(max_score, max(row_values))
        axis_y.setRange(0, max_score * 1.1)  # 增加10%的空间
        
        chart.addAxis(axis_x, Qt.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        # 显示中文字体（微软雅黑）
        font = QFont("微软雅黑", 10)
        chart.setTitleFont(font)
        axis_x.setLabelsFont(font)
        axis_y.setLabelsFont(font)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # 添加数值标签
        self.add_value_labels(chart_view, series, subjects, chart_data, class_names, max_score)

        layout.addWidget(chart_view)

    def add_value_labels(self, chart_view, series, subjects, chart_data, class_names, max_score):
        """在柱状图上添加数值标签"""
        # 使用定时器确保图表完全渲染后再添加标签
        QTimer.singleShot(100, lambda: self._add_labels_delayed(chart_view, series, subjects, chart_data, class_names, max_score))

    def _add_labels_delayed(self, chart_view, series, subjects, chart_data, class_names, max_score):
        """延迟添加标签的实际实现"""
        chart = chart_view.chart()
        
        # 获取颜色列表，为每个班级分配不同颜色
        colors = ['#409eff', '#67c23a', '#e6a23c', '#f56c6c', '#909399', '#c71585', '#ff6347', '#32cd32']
        
        # 为每个班级的每个科目添加标签
        for class_idx, (class_data, class_name) in enumerate(zip(chart_data, class_names)):
            color = colors[class_idx % len(colors)]
            
            for subj_idx, score in enumerate(class_data):
                if score > 0:
                    label = QLabel(f"{score:.1f}", chart_view)
                    label.setAlignment(Qt.AlignCenter)
                    label.setFont(QFont("微软雅黑", 8))
                    label.setStyleSheet(f"""
                        color: {color}; 
                        background-color: rgba(255, 255, 255, 180); 
                        border-radius: 3px; 
                        padding: 2px;
                        border: 1px solid {color};
                    """)
                    
                    # 计算标签位置
                    bar_rect = chart.plotArea()
                    bar_width = bar_rect.width() / len(subjects)
                    group_width = bar_width / len(chart_data)
                    
                    # X坐标：科目位置 + 班级在组内的偏移
                    x = bar_rect.x() + subj_idx * bar_width + class_idx * group_width + group_width / 2
                    
                    # Y坐标：根据分数比例计算高度
                    y_ratio = score / (max_score * 1.1)
                    y = bar_rect.y() + bar_rect.height() - y_ratio * bar_rect.height() - 25
                    
                    # 调整标签位置，使其居中
                    label.resize(40, 20)
                    label.move(int(x - 20), int(y))
                    label.show()

    def on_bar_hovered(self, status, index, barset, chart_view):
        """处理柱子悬停事件"""
        if status:
            # 可以在这里添加更多的交互效果
            pass