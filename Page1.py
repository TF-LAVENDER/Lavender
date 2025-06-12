import psutil
from PySide6.QtGui import QPen, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QTimer, QPointF, QMargins
from utils import load_ui_file

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        
        # .ui 파일 로딩 및 레이아웃 세팅
        self.ui = load_ui_file("page1.ui")
        self.setLayout(self.ui.layout())

        # 라인 시리즈 (보낸/받은 트래픽)
        self.series_sent = QLineSeries(name="보낸 데이터 (KB/s)")
        self.series_recv = QLineSeries(name="받은 데이터 (KB/s)")

        # QChart 구성
        self.chart = QChart()
        self.chart.addSeries(self.series_sent)
        self.chart.addSeries(self.series_recv)
        self.chart.createDefaultAxes()
        self.chart.legend().setVisible(True)
        self.chart.setTitle("실시간 네트워크 트래픽")

        # 🔧 차트 뷰 여백 제거
        self.chart_view = QChartView(self.chart)
        self.chart_view.setContentsMargins(0, 0, 0, 0)
        self.chart_view.setRenderHint(self.chart_view.renderHints())  # 렌더링 힌트 유지

        # 🔧 차트 자체 여백 제거
        self.chart.setMargins(QMargins(0, 0, 0, 0))  # 마진 제거
        self.chart.setBackgroundRoundness(0)  # 배경 둥근 모서리 제거
        self.chart.setBackgroundVisible(False)  # 배경 자체 안 보이게 하고 싶으면 이걸로

        # ✅ 선 색상 명시 (선택)
        self.series_sent.setPen(QPen(QColor("red"), 2))
        self.series_recv.setPen(QPen(QColor("blue"), 2))

        # ✅ 축 범위 강제 지정 (초기값)
        self.chart.axisX().setRange(0, 60)
        self.chart.axisY().setRange(0, 200)

        # 차트 뷰 생성
        self.chart_view = QChartView(self.chart)

        # .ui의 chartContainer에 chart_view 삽입
        if hasattr(self.ui, 'chartContainer'):
            container_layout = self.ui.chartContainer.layout()
            if container_layout is not None:
                container_layout.addWidget(self.chart_view)
            else:
                # layout이 설정되어 있지 않으면 새로 생성
                new_layout = QVBoxLayout(self.ui.chartContainer)
                new_layout.setContentsMargins(0, 0, 0, 0)
                new_layout.addWidget(self.chart_view)

        # 초기 네트워크 상태 저장
        self.prev_sent, self.prev_recv = self.get_network_bytes()
        self.x = 0

        # 타이머 설정 (1초 간격)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(1000)

    def get_network_bytes(self):
        counters = psutil.net_io_counters()
        return counters.bytes_sent, counters.bytes_recv

    def update_chart(self):
        sent, recv = self.get_network_bytes()
        sent_speed = (sent - self.prev_sent) / 1024  # KB
        recv_speed = (recv - self.prev_recv) / 1024  # KB

        self.series_sent.append(QPointF(self.x, sent_speed))
        self.series_recv.append(QPointF(self.x, recv_speed))
        self.x += 1

        if self.series_sent.count() > 60:
            self.series_sent.removePoints(0, self.series_sent.count() - 60)
            self.series_recv.removePoints(0, self.series_recv.count() - 60)

        self.prev_sent, self.prev_recv = sent, recv
        self.chart.axisX().setRange(max(0, self.x - 60), self.x)