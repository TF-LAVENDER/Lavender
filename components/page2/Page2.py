from PySide6.QtWidgets import QWidget
from utils import load_ui_file  
from components.page2.page2_ui import Ui_MainWindow

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file("components/page2/page2.ui")
        self.setLayout(self.ui.layout())

