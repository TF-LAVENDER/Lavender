from PySide6.QtWidgets import QWidget
from utils import load_ui_file

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = load_ui_file("components/page2/page2.ui")
        self.setLayout(self.ui.layout())

        self.ui.blockedButton.clicked.connect(self.blocked_clicked)
        self.ui.allowedButton.clicked.connect(self.allowed_clicked)

        self.ui.blockedButton.setFlat(True)
        self.ui.allowedButton.setFlat(True)
    
    def menuChange(self, menuNum):
        self.ui.blockedButton.setStyleSheet("border-image: url('components/page2/images/blocked_off.png');")
        self.ui.allowedButton.setStyleSheet("border-image: url('components/page2/images/allowed_off.png');")
        if menuNum == 1:
            self.ui.blockedButton.setStyleSheet("border-image: url('components/page2/images/blocked_on.png');")
        elif menuNum == 2:
            self.ui.allowedButton.setStyleSheet("border-image: url('components/page2/images/allowed_on.png');")

    def blocked_clicked(self):
        self.menuChange(1)

    def allowed_clicked(self):
        self.menuChange(2)