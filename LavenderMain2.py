import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice




def menuChange(menuNum):
    
    window.munuButton1.setStyleSheet("border-image:url('images/menu1_off.png');")
    window.munuButton2.setStyleSheet("border-image:url('images/menu2_off.png');")
    window.munuButton3.setStyleSheet("border-image:url('images/menu3_off.png');")
    window.munuButton4.setStyleSheet("border-image:url('images/menu4_off.png');")
    if menuNum == 1:
        window.munuButton1.setStyleSheet("border-image:url('images/menu1_on.png');")
    elif menuNum == 2:
        window.munuButton2.setStyleSheet("border-image:url('images/menu2_on.png');")
    elif menuNum == 3:
        window.munuButton3.setStyleSheet("border-image:url('images/menu3_on.png');")
    elif menuNum == 4:
        window.munuButton4.setStyleSheet("border-image:url('images/menu4_on.png');")

def menu1_clicked(self):
    menuChange(1)
def menu2_clicked(self):
    menuChange(2)
def menu3_clicked(self):
    menuChange(3)
def menu4_clicked(self):
    menuChange(4)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "MainWindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    window.munuButton1.clicked.connect(menu1_clicked)
    window.munuButton2.clicked.connect(menu2_clicked)
    window.munuButton3.clicked.connect(menu3_clicked)
    window.munuButton4.clicked.connect(menu4_clicked)

    sys.exit(app.exec())
    