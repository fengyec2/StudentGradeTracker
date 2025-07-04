from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot
from common.utils import show_dialog
from components.bar import ProgressInfoBar
from ui_page.ui_page_top_in_class import Ui_page_top_in_class
from view.pages.page_top_in_class_handler import PageTopInClassHandler


class PageTopInClass(QWidget, Ui_page_top_in_class):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loading_bar = None
        self.setupUi(self)

        self.handler = PageTopInClassHandler(self)

        self.examListView.clicked.connect(self.on_exam_selected)
        self.classComboBox.currentTextChanged.connect(self.on_class_changed)

        self.handler.init_exam_list()

    def on_exam_selected(self, index):
        display_name = index.data()
        self.handler.update_class_list_for_exam(display_name)

    def on_class_changed(self, class_name):
        exam_index = self.examListView.currentIndex()
        if not exam_index.isValid():
            return
        exam_name = exam_index.data()
        if exam_name and class_name:
            self.handler.load_top_subject_data(exam_name, class_name)

    def show_state_tooltip(self, title, content):
        self.loading_bar = ProgressInfoBar(title, content, self)
        self.loading_bar.show()

    def close_state_tooltip(self):
        if self.loading_bar:
            self.loading_bar.hide()
            self.loading_bar = None

    def on_common_error(self, msg):
        show_dialog(self, msg, '提示')

    def update_chart(self, subject_names, class_scores, grade_scores):
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.figure import Figure
        from PySide6.QtWidgets import QVBoxLayout
        import matplotlib
        matplotlib.rcParams['font.family'] = 'Microsoft YaHei'

        if self.chartWidget.layout() is None:
            self.chartWidget.setLayout(QVBoxLayout())
        layout = self.chartWidget.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        fig = Figure(figsize=(8, 4))
        ax = fig.add_subplot(111)
        x = range(len(subject_names))
        ax.bar([i - 0.2 for i in x], class_scores, width=0.4, label='班级第一', color='#5B8FF9')
        ax.bar([i + 0.2 for i in x], grade_scores, width=0.4, label='年级第一', color='#61DDAA')
        ax.set_xticks(x)
        ax.set_xticklabels(subject_names, rotation=30)
        ax.set_ylabel("分数")
        ax.set_title("各科班级第一与年级第一对比")
        ax.legend()

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
