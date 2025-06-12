from PySide6.QtWidgets import QWidget
from utils import load_ui_file  

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file("page2.ui")
        self.setLayout(self.ui.layout())
        