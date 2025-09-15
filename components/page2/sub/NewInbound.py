from PySide6.QtWidgets import QWidget
from utils import load_ui_file

class NewInbound(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file("components/page2/sub/newInbound.ui")
        self.setLayout(self.ui.layout())