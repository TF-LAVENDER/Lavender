# Page1.py

import psutil
from PySide6.QtGui import QPen, QColor,QBrush, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QToolTip
from PySide6.QtCharts import QChart, QChartView, QSplineSeries
from PySide6.QtCore import QTimer, QPointF, QMargins, Qt
from utils import load_ui_file

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        
        # .ui 파일 로딩 및 레이아웃 세팅
        self.ui = load_ui_file("page1.ui")
        self.setLayout(self.ui.layout())

        # 라인 시리즈 (보낸/받은 트래픽)
        self.series_sent = QSplineSeries(name="보낸 데이터 (KB/s)")
        self.series_recv = QSplineSeries(name="받은 데이터 (KB/s)")

        # QChart 구성
        self.chart = QChart()
        self.chart.addSeries(self.series_sent)
        self.chart.addSeries(self.series_recv)
        self.chart.createDefaultAxes()

        # 축 객체 가져오기
        axis_x = self.chart.axisX()
        axis_y = self.chart.axisY()

        # 축 라벨 색상 하얗게
        axis_x.setLabelsBrush(QColor("white"))
        axis_y.setLabelsBrush(QColor("white"))

        axis_y.setLabelsVisible(False)

        axis_x.setGridLineVisible(False)
        axis_y.setGridLineVisible(False)


        # ✅ 선 색상 명시 (선택)
        self.series_sent.setPen(QPen(QColor.fromRgbF(1.0, 0.3176, 0.3176, 1.0), 5))
        self.series_recv.setPen(QPen(QColor.fromRgbF(1.0, 0.9686, 0.0, 0.86), 5))

        # ✅ 축 범위 강제 지정 (초기값)
        self.chart.axisX().setRange(0, 60)
        self.chart.axisY().setRange(0, 2000)

        self.chart.setMargins(QMargins(0, 0, 0, 0)) 
        self.chart.setTitle("")            # 제목 제거
        self.chart.legend().hide()         # 범례 제거

        # 차트 뷰 생성
        self.chart_view = QChartView(self.chart)
        # self.chart.setBackgroundVisible(False)
        self.chart.setBackgroundVisible(True)
        self.chart.setBackgroundRoundness(0)
        self.chart.setPlotAreaBackgroundVisible(False)
        self.chart.setBackgroundBrush(QBrush(QColor("#44407A")))
        self.chart.setPlotAreaBackgroundVisible(True)

        self.chart_view.setStyleSheet("background: transparent; border: none; margin: 0; padding: 0;")
        self.chart_view.setContentsMargins(0, 0, 0, 0)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        
        # 초기 네트워크 상태 저장
        self.prev_sent, self.prev_recv = self.get_network_bytes()
        self.x = 0

        # 타이머 설정 (1초 간격)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(500)

        self.series_sent.hovered.connect(self.on_point_hovered_sent)
        self.series_recv.hovered.connect(self.on_point_hovered_recv)

        # .ui의 chartContainer에 chart_view 삽입
        if hasattr(self.ui, 'chartContainer'):
            container_layout = self.ui.chartContainer.layout()
            if container_layout is not None:
                container_layout.setContentsMargins(0, 0, 0, 0)  # 여백 제거
                container_layout.setSpacing(0)                   # 위젯 간 간격 제거
                container_layout.addWidget(self.chart_view)
            else:
                new_layout = QVBoxLayout(self.ui.chartContainer)
                new_layout.setContentsMargins(0, 0, 0, 0)
                new_layout.setSpacing(0)
                new_layout.addWidget(self.chart_view)

        




        # 트래픽 차트 설정






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

        # 최근 데이터에서 최대값 찾기
        all_points = self.series_sent.pointsVector() + self.series_recv.pointsVector()
        if all_points:
            max_y = max(point.y() for point in all_points)
            self.chart.axisY().setRange(0, max_y * 1.2)

        if self.series_sent.count() > 60:
            self.series_sent.removePoints(0, self.series_sent.count() - 60)
            self.series_recv.removePoints(0, self.series_recv.count() - 60)

        self.prev_sent, self.prev_recv = sent, recv
        self.chart.axisX().setRange(max(0, self.x - 60), self.x)

    def on_point_hovered_sent(self, point, state):
        if state:
            QToolTip.showText(
                self.mapToGlobal(self.chart_view.mapFromScene(
                    self.chart.mapToPosition(point, self.series_sent)
                )),
                f"Sent: {point.y():.1f} KB/s"
            )

    def on_point_hovered_recv(self, point, state):
        if state:
            QToolTip.showText(
                self.mapToGlobal(self.chart_view.mapFromScene(
                    self.chart.mapToPosition(point, self.series_recv)
                )),
                f"Recv: {point.y():.1f} KB/s"
            )