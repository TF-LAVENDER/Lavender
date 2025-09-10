# LavenderMain.py

import signal
import sys
import subprocess
import os
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout
from PySide6.QtGui import QRegion, QPainterPath
from PySide6.QtCore import Qt, QPoint
from components.page1.Page1 import Page1
from components.page2.Page2 import Page2
from components.page3.Page3 import Page3
from components.page4.Page4 import Page4
from utils import load_ui_file



from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPainterPath, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1) 프레임리스 + 투명 배경
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 2) UI 로드 및 중앙 위젯 투명 처리 (중요!)
        self.ui = load_ui_file("MainWindow.ui")
        self.setCentralWidget(self.ui)
        self.ui.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.setAutoFillBackground(False)
        self.ui.setStyleSheet("background: transparent;")  # UI 파일에서 배경색 줬다면 지워져야 함

        # 3) 윈도우 크기
        self.setFixedSize(960, 545)

        # 4) 절대 쓰지 말 것: setMask(...)  ← 이거 있으면 모서리 계단짐(AA 불가)

        self.show()

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
        self.ui.exitButton.clicked.connect(self.close)
        self.ui.minimizeButton.clicked.connect(self.showMinimized)

    def paintEvent(self, event):
        # 5) 메인 윈도우에 직접 둥근 배경을 그리고 AA 켜기
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        # 경계선 반픽셀 깔끔하게 하려고 살짝 안쪽으로
        r = self.rect().adjusted(0, 0, -1, -1)

        path = QPainterPath()
        path.addRoundedRect(r, 10, 10)

        painter.fillPath(path, QColor(34, 34, 34))




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

    def mousePressEvent(self, event):       #마우스 드레그 함수
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

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
