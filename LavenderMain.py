#LavenderMain.py

import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import QFile, QIODevice
from components.page1.Page1 import Page1
from components.page2.Page2 import Page2
from components.page3.Page3 import Page3
from components.page4.Page4 import Page4
from utils import load_ui_file


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.ui = load_ui_file("MainWindow.ui")
        self.setCentralWidget(self.ui)
        self.setFixedSize(960, 545) 
        self.show()

        self.content_container = self.ui.findChild(QHBoxLayout, "contentArea")
        print(self.content_container)

        self.page1 = Page1()
        self.page2 = Page2()
        self.page3 = Page3()
        self.page4 = Page4()

    
        self.ui.menuButton1.clicked.connect(self.menu1_clicked)
        self.ui.menuButton2.clicked.connect(self.menu2_clicked)
        self.ui.menuButton3.clicked.connect(self.menu3_clicked)
        self.ui.menuButton4.clicked.connect(self.menu4_clicked)

        self.load_page1()


    def clear_content(self):
        # 기존 위젯 제거
        for i in reversed(range(self.content_container.layout().count())):
            widget = self.content_container.layout().itemAt(i).widget()
            if widget:
                widget.setParent(None)      

    def show_page1(self):
        self.setCentralWidget(Page1())
    def show_page2(self):
        self.setCentralWidget(Page2())
    def show_page3(self):
        self.setCentralWidget(Page3())
    def show_page4(self):
        self.setCentralWidget(Page4())

    def load_page1(self):
        self.clear_content()
        self.content_container.layout().addWidget(self.page1)
    def load_page2(self):
        self.clear_content()
        self.content_container.layout().addWidget(self.page2)
    def load_page3(self):
        self.clear_content()
        self.content_container.layout().addWidget(self.page3)
    def load_page4(self):
        self.clear_content()
        self.content_container.layout().addWidget(self.page4)



    def menuChange(self, menuNum):    
        self.ui.menuButton1.setStyleSheet("border-image:url('images/menu1_off.png');")
        self.ui.menuButton2.setStyleSheet("border-image:url('images/menu2_off.png');")
        self.ui.menuButton3.setStyleSheet("border-image:url('images/menu3_off.png');")
        self.ui.menuButton4.setStyleSheet("border-image:url('images/menu4_off.png');")
        if menuNum == 1:
            self.ui.menuButton1.setStyleSheet("border-image:url('images/menu1_on.png');")
            self.load_page1()
        elif menuNum == 2:
            self.ui.menuButton2.setStyleSheet("border-image:url('images/menu2_on.png');")
            self.load_page2()
        elif menuNum == 3:
            self.ui.menuButton3.setStyleSheet("border-image:url('images/menu3_on.png');")
            self.load_page3()
        elif menuNum == 4:
            self.ui.menuButton4.setStyleSheet("border-image:url('images/menu4_on.png');")
            self.load_page4()


    def menu1_clicked(self):
        self.menuChange(1)
    def menu2_clicked(self):
        self.menuChange(2)
    def menu3_clicked(self):
        self.menuChange(3)
    def menu4_clicked(self):
        self.menuChange(4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())