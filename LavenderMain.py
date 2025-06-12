import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from Page1 import Page1
from Page2 import Page2
from Page3 import Page3
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

    
        self.ui.munuButton1.clicked.connect(self.menu1_clicked)
        self.ui.munuButton2.clicked.connect(self.menu2_clicked)
        self.ui.munuButton3.clicked.connect(self.menu3_clicked)
        self.ui.munuButton4.clicked.connect(self.menu4_clicked)

        self.load_page1()


    def clear_content(self):
        # 기존 위젯 제거
        for i in reversed(range(self.content_container.layout().count())):
            widget = self.content_container.layout().itemAt(i).widget()
            if widget:
                widget.setParent(None)      

    def show_page1(self):
        self.setCentralWidget(Page1())

    def load_page1(self):
        self.clear_content()
        page = Page1()
        self.content_container.layout().addWidget(page) 

    def show_page2(self):
        self.setCentralWidget(Page2())

    def load_page2(self):
        self.clear_content()
        page = Page2()
        self.content_container.layout().addWidget(page) 

    def load_page3(self):
        self.clear_content()
        page = Page3()
        self.content_container.layout().addWidget(page) 

    # def show_page2(self):
    #     self.setCentralWidget(Page2())

    def menuChange(self, menuNum):    
        self.ui.munuButton1.setStyleSheet("border-image:url('images/menu1_off.png');")
        self.ui.munuButton2.setStyleSheet("border-image:url('images/menu2_off.png');")
        self.ui.munuButton3.setStyleSheet("border-image:url('images/menu3_off.png');")
        self.ui.munuButton4.setStyleSheet("border-image:url('images/menu4_off.png');")
        if menuNum == 1:
            self.ui.munuButton1.setStyleSheet("border-image:url('images/menu1_on.png');")
            self.load_page1()
        elif menuNum == 2:
            self.ui.munuButton2.setStyleSheet("border-image:url('images/menu2_on.png');")
            self.load_page2()
        elif menuNum == 3:
            self.ui.munuButton3.setStyleSheet("border-image:url('images/menu3_on.png');")
            self.load_page3()
        elif menuNum == 4:
            self.ui.munuButton4.setStyleSheet("border-image:url('images/menu4_on.png');")


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


# def menuChange(menuNum):
    
#     window.munuButton1.setStyleSheet("border-image:url('images/menu1_off.png');")
#     window.munuButton2.setStyleSheet("border-image:url('images/menu2_off.png');")
#     window.munuButton3.setStyleSheet("border-image:url('images/menu3_off.png');")
#     window.munuButton4.setStyleSheet("border-image:url('images/menu4_off.png');")
#     if menuNum == 1:
#         window.munuButton1.setStyleSheet("border-image:url('images/menu1_on.png');")
#     elif menuNum == 2:
#         window.munuButton2.setStyleSheet("border-image:url('images/menu2_on.png');")
#     elif menuNum == 3:
#         window.munuButton3.setStyleSheet("border-image:url('images/menu3_on.png');")
#     elif menuNum == 4:
#         window.munuButton4.setStyleSheet("border-image:url('images/menu4_on.png');")

# def menu1_clicked(self):
#     menuChange(1)
# def menu2_clicked(self):
#     menuChange(2)
# def menu3_clicked(self):
#     menuChange(3)
# def menu4_clicked(self):
#     menuChange(4)



# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     ui_file_name = "MainWindow.ui"
#     ui_file = QFile(ui_file_name)
#     if not ui_file.open(QIODevice.ReadOnly):
#         print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
#         sys.exit(-1)
#     loader = QUiLoader()
#     window = loader.load(ui_file)
#     ui_file.close()
#     if not window:
#         print(loader.errorString())
#         sys.exit(-1)
#     window.show()

#     window.munuButton1.clicked.connect(menu1_clicked)
#     window.munuButton2.clicked.connect(menu2_clicked)
#     window.munuButton3.clicked.connect(menu3_clicked)
#     window.munuButton4.clicked.connect(menu4_clicked)

#     sys.exit(app.exec())
    