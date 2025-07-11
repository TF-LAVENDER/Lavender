from PySide6.QtWidgets import QWidget
from components.page4.page4_ui import Ui_MainWindow
from utils import load_ui_file

class Page4(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file("components/page4/page4.ui")
        self.setLayout(self.ui.layout())