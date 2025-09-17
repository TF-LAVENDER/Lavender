from PySide6.QtWidgets import QWidget
from utils import load_ui_file, resource_path

class Page3(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file(resource_path("components/page3/page3.ui"))
        self.setLayout(self.ui.layout())