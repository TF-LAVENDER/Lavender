from PySide6.QtWidgets import QWidget
from utils import load_ui_file

class Page3(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file("components/page3/page3.ui")
        self.setLayout(self.ui.layout())

        self.ui.blockedButton.clicked.connect(self.blocked_clicked)
        self.ui.allowedButton.clicked.connect(self.allowed_clicked)
    
    def menuChange(self, menuNum):
        self.ui.blockedButton.setStyleSheet("border-image: url('components/page3/images/blocked_off.png');")
        self.ui.allowedButton.setStyleSheet("border-image: url('components/page3/images/allowed_off.png');")
        if menuNum == 1:
            self.ui.blockedButton.setStyleSheet("border-image: url('components/page3/images/blocked_on.png');")
        elif menuNum == 2:
            self.ui.allowedButton.setStyleSheet("border-image: url('components/page3/images/allowed_on.png');")

    def blocked_clicked(self):
        self.menuChange(1)

    def allowed_clicked(self):
        self.menuChange(2)