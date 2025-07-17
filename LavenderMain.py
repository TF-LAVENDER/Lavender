# LavenderMain.py

import signal
import sys
import subprocess
import os
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout
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

        # contentArea는 QWidget이고, 그 layout이 QHBoxLayout임
        self.content_widget = self.ui.findChild(QWidget, "horizontalLayoutWidget")
        if self.content_widget is None:
            raise RuntimeError("horizontalLayoutWidget 위젯을 찾을 수 없습니다. .ui 파일 확인 필요.")
        self.content_container = self.content_widget.layout()
        print(self.content_container)  # QHBoxLayout 출력됨


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
        for i in reversed(range(self.content_container.count())):
            widget = self.content_container.itemAt(i).widget()
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
        self.content_container.addWidget(self.page1)

    def load_page2(self):
        self.clear_content()
        self.content_container.addWidget(self.page2)

    def load_page3(self):
        self.clear_content()
        self.content_container.addWidget(self.page3)

    def load_page4(self):
        self.clear_content()
        self.content_container.addWidget(self.page4)

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


# 🔁 기존 os.fork() 대신 subprocess 사용
def start_daemon():
    try:
        process = subprocess.Popen(
            ["python3", "services/IpBlockDaemon.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return process.pid, process
    except Exception as e:
        print(f"[ERROR] 데몬 실행 실패: {e}")
        return None, None


if __name__ == "__main__":
    daemon_pid, daemon_process = start_daemon()
    if daemon_pid:
        print(f"[INFO] IP 차단 데몬 PID: {daemon_pid}")

    app = QApplication(sys.argv)
    window = MainWindow()
    exit_code = app.exec()

    if daemon_process:
        daemon_process.terminate()

    sys.exit(exit_code)
