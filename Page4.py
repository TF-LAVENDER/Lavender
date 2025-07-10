from PySide6.QtWidgets import QWidget
from utils import load_ui_file  

class Page4(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file("page4.ui")
        self.setLayout(self.ui.layout())
        