import os
import json
from datetime import datetime
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox

class PageTwoHandler(QObject):
    def __init__(self, parent: 'PageTwo'):
        super().__init__(parent)
        self._parent = parent
        self.student_data = []

    def load_students(self):
        data_dir = './data/students'
        self.student_data.clear()
        names = []

        if os.path.exists(data_dir):
            for file in os.listdir(data_dir):
                if file.endswith('.json'):
                    filepath = os.path.join(data_dir, file)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        try:
                            data = json.load(f)
                            self.student_data.append(data)
                            names.append(data.get('student', '未知'))
                        except Exception as e:
                            print(f"读取失败 {file}: {e}")
        self._parent.set_student_list(names)

    def on_student_selected(self, index):
        student_name = index.data()
        student = next((s for s in self.student_data if s.get('student') == student_name), None)
        if not student:
            QMessageBox.warning(self._parent, '错误', '未找到学生数据')
            return

        exams = student.get('exams', [])
        # 按照日期升序排列
        exams.sort(key=lambda e: e.get('real_date', ''))

        x_labels = [e.get('real_date', '') for e in exams]
        y_values = [e.get('rank', 0) for e in exams]

        self._parent.plot_rank_trend(x_labels, y_values, student_name)
