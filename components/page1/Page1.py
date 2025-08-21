from PySide6.QtWidgets import QWidget
from utils import load_ui_file  

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file("components/page1/page1.ui")
        self.setLayout(self.ui.layout())

