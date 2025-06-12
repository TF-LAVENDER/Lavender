# import sys
# from PySide6.QtWidgets import QApplication, QLabel

# app = QApplication(sys.argv)
# label = QLabel("test main")
# label.show()
# app.exec()

import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice



def option_selected(self):
    window.textEdit1.setText('hello world')

def option2_selected(self):
    window.textEdit1.setText('라벤더 프로젝트트')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "TestMainWindow.ui"
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


    window.pushButton1.clicked.connect(option_selected)
    window.pushButton2.clicked.connect(option2_selected)
    sys.exit(app.exec())
    