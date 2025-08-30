# Page2.py

import time
import psutil
from PySide6.QtGui import QPen, QColor,QBrush, QPainter, QCursor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QToolTip, QProgressBar
from PySide6.QtCharts import QChart, QChartView, QSplineSeries
from PySide6.QtCore import QTimer, QPointF, QMargins, QPropertyAnimation, QEasingCurve, Property, QEvent

from utils import load_ui_file

WAN_IFACE = "en0"  # 외부망 인터페이스
LAN_IFACE = "en1"  # 내부망 인터페이스

class Page2(QWidget):
    def __init__(self):
        super().__init__()

        # .ui 파일 로딩 및 레이아웃 세팅
        self.ui = load_ui_file("components/page2/page2.ui")
        self.setLayout(self.ui.layout())

        # 라인 시리즈 (보낸/받은 트래픽)
        self.series_sent = QSplineSeries(name="보낸 데이터 (KB/s)")
        self.series_recv = QSplineSeries(name="받은 데이터 (KB/s)")

        # 누적 트래픽 초기화
        self.total_sent = 0
        self.total_recv = 0
        # WAN/LAN별 누적 트래픽 초기화
        self.total_wan_sent = 0
        self.total_wan_recv = 0
        self.total_lan_sent = 0
        self.total_lan_recv = 0

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

        axis_y.setVisible(False)

        axis_x.setGridLineVisible(False)
        axis_y.setGridLineVisible(False)


        # 선 색상 명시 (선택)
        self.series_sent.setPen(QPen(QColor.fromRgbF(1.0, 0.3176, 0.3176, 1.0), 5))
        self.series_recv.setPen(QPen(QColor.fromRgbF(1.0, 0.9686, 0.0, 0.86), 5))

        # 축 범위 강제 지정 (초기값)
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
        # 기존 전체 트래픽 초기화
        self.prev_sent, self.prev_recv = self.get_network_bytes()
        self.x = 0
        # WAN/LAN별 이전 트래픽 초기화
        self.prev_wan_sent, self.prev_wan_recv = self.get_network_bytes_by_iface(WAN_IFACE)
        self.prev_lan_sent, self.prev_lan_recv = self.get_network_bytes_by_iface(LAN_IFACE)

        # 타이머 설정 (1초 간격)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(1000)

        self.series_sent.hovered.connect(self.on_point_hovered_sent)
        self.series_recv.hovered.connect(self.on_point_hovered_recv)

        # 프로그레스바 애니메이션 설정
        self.progress_animation = QPropertyAnimation(self.ui.recv_send_ratio, b"value")
        self.progress_animation.setDuration(300)  # 300ms
        self.progress_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

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

    def get_network_bytes(self):
        counters = psutil.net_io_counters()
        return counters.bytes_sent, counters.bytes_recv

    def get_network_bytes_by_iface(self, iface_name):
        counters = psutil.net_io_counters(pernic=True)
        if iface_name in counters:
            return counters[iface_name].bytes_sent, counters[iface_name].bytes_recv
        else:
            return 0, 0

    def update_chart(self):
        # 전체 트래픽
        sent, recv = self.get_network_bytes()
        sent_speed = (sent - self.prev_sent) / 1024  # KB
        recv_speed = (recv - self.prev_recv) / 1024  # KB
        # WAN 트래픽
        wan_sent, wan_recv = self.get_network_bytes_by_iface(WAN_IFACE)
        wan_sent_speed = (wan_sent - self.prev_wan_sent) / 1024
        wan_recv_speed = (wan_recv - self.prev_wan_recv) / 1024
        # LAN 트래픽
        lan_sent, lan_recv = self.get_network_bytes_by_iface(LAN_IFACE)
        lan_sent_speed = (lan_sent - self.prev_lan_sent) / 1024
        lan_recv_speed = (lan_recv - self.prev_lan_recv) / 1024
        # 기존 전체 트래픽 그래프
        self.series_sent.append(QPointF(self.x, sent_speed))
        self.series_recv.append(QPointF(self.x, recv_speed))
        self.x += 1
        # WAN/LAN 누적 트래픽 업데이트
        self.total_wan_sent += wan_sent_speed
        self.total_wan_recv += wan_recv_speed
        self.total_lan_sent += lan_sent_speed
        self.total_lan_recv += lan_recv_speed
        # WAN/LAN 이전값 갱신
        self.prev_wan_sent, self.prev_wan_recv = wan_sent, wan_recv
        self.prev_lan_sent, self.prev_lan_recv = lan_sent, lan_recv
        # (옵션) WAN_BAR, LAN_BAR에 값 반영하려면 아래와 같이 사용
        # if hasattr(self.ui, 'WAN_BAR'):
        #     self.ui.WAN_BAR.setValue(int(min(wan_recv_speed, 100)))  # 예시: 0~100 스케일
        # if hasattr(self.ui, 'LAN_BAR'):
        #     self.ui.LAN_BAR.setValue(int(min(lan_recv_speed, 100)))  # 예시: 0~100 스케일

        # 최근 데이터에서 최대값 찾기
        all_points = self.series_sent.pointsVector() + self.series_recv.pointsVector()
        if all_points:
            max_y = max(point.y() for point in all_points)
            self.chart.axisY().setRange(0, max_y * 1.2)

        if self.series_sent.count() > 60:
            self.series_sent.removePoints(0, self.series_sent.count() - 60)
            self.series_recv.removePoints(0, self.series_recv.count() - 60)

        # recv_send_ratio 프로그레스 바 업데이트
        self.update_traffic_ratio(sent_speed, recv_speed, wan_sent_speed, wan_recv_speed, lan_sent_speed, lan_recv_speed)

        # WAN/LAN 비율로 BAR 길이 업데이트 (최대 400px)
        total = lan_recv_speed + wan_recv_speed
        max_width = 400
        if total > 0:
            lan_width = int((lan_recv_speed / total) * max_width)
            wan_width = max_width - lan_width
        else:
            lan_width = 0
            wan_width = 0
        if hasattr(self.ui, 'LAN_BAR'):
            self.ui.LAN_BAR.setFixedWidth(lan_width)
        if hasattr(self.ui, 'WAN_BAR'):
            self.ui.WAN_BAR.setFixedWidth(wan_width)

        self.prev_sent, self.prev_recv = sent, recv
        self.chart.axisX().setRange(max(0, self.x - 60), self.x)

    def update_traffic_ratio(self, sent_speed, recv_speed, wan_sent_speed, wan_recv_speed, lan_sent_speed, lan_recv_speed):
        """받는 트래픽과 보내는 트래픽을 색으로 구분해서 표시"""
        if hasattr(self.ui, 'recv_send_ratio'):
            progress_bar = self.ui.recv_send_ratio
            
            # 총 트래픽 계산
            total_traffic = sent_speed + recv_speed
            
            # 누적 트래픽 업데이트
            self.total_sent += sent_speed
            self.total_recv += recv_speed
            
            if total_traffic > 0:
                # 받는 트래픽 비율 계산 (노란색 부분)
                recv_ratio = (recv_speed / total_traffic) * 100

                self.progress_animation.setStartValue(progress_bar.value())
                self.progress_animation.setEndValue(int(recv_ratio))
                self.progress_animation.start()
                
                # 스타일시트 업데이트
                style_sheet = f"""
                QProgressBar {{
                    border-radius: 37px;
                    background-color: #ff5151;
                    text-align: center;
                    color: black;
                }}
                
                QProgressBar::chunk {{
                    background-color: #fff700;
                    border-top-left-radius: 37px;
                    border-bottom-left-radius: 37px;
                }}
                """
                progress_bar.setStyleSheet(style_sheet)
                
                # 라벨 업데이트
                if hasattr(self.ui, 'recv_kbs'):
                    maxKb = 1500
                    maxMb = 1500 * 1024

                    if recv_speed < maxKb:
                        self.ui.recv_kbs.setText(f"{recv_speed:.1f} KB/s")
                    else:
                        self.ui.recv_kbs.setText(f"{recv_speed/1024:.1f} MB/s")
                if hasattr(self.ui, 'send_kbs'):
                    if sent_speed < maxKb:
                        self.ui.send_kbs.setText(f"{sent_speed:.1f} KB/s")
                    else:
                        self.ui.send_kbs.setText(f"{sent_speed / 1024:.1f} MB/s")
                if hasattr(self.ui, 'sum_kbs'):
                    if total_traffic < maxKb:
                        self.ui.sum_kbs.setText(f"{total_traffic:.1f} KB/s")
                    else:
                        self.ui.sum_kbs.setText(f"{total_traffic/1024:.1f} MB/s")
                
                # recv_kbs_2와 send_kbs_2 라벨에 누적 트래픽 표시
                if hasattr(self.ui, 'recv_kbs_2'):
                    if self.total_recv < maxKb:
                        self.ui.recv_kbs_2.setText(f"{self.total_recv:.1f} KB")
                    else:
                        self.ui.recv_kbs_2.setText(f"{self.total_recv/1024:.1f} MB")
                if hasattr(self.ui, 'send_kbs_2'):
                    if self.total_sent < maxKb:
                        self.ui.send_kbs_2.setText(f"{self.total_sent:.1f} KB")
                    else:
                        self.ui.send_kbs_2.setText(f"{self.total_sent/1024:.1f} MB")
            else:
                # 트래픽이 없을 때
                self.progress_animation.setStartValue(progress_bar.value())
                self.progress_animation.setEndValue(0)
                self.progress_animation.start()
                
                if hasattr(self.ui, 'recv_kbs'):
                    self.ui.recv_kbs.setText("0.0 KB/s")
                if hasattr(self.ui, 'send_kbs'):
                    self.ui.send_kbs.setText("0.0 KB/s")
                if hasattr(self.ui, 'sum_kbs'):
                    self.ui.sum_kbs.setText("0.0 KB/s")
                # if hasattr(self.ui, 'recv_kbs_2'):
                #     self.ui.recv_kbs_2.setText(f"{self.total_recv:.1f} KB")
                # if hasattr(self.ui, 'send_kbs_2'):
                #     self.ui.send_kbs_2.setText(f"{self.total_sent:.1f} KB")
            
        if hasattr(self.ui, 'WAN_BAR') and hasattr(self.ui, 'LAN_BAR'):
            wan_progress_bar = self.ui.WAN_BAR
            lan_progress_bar = self.ui.LAN_BAR
            
            # 총 트래픽 계산
            # total_wan_traffic = sent_speed + recv_speed
            
            # 누적 트래픽 업데이트
            self.total_wan_sent += wan_sent_speed
            self.total_wan_recv += wan_recv_speed
            self.total_lan_sent += lan_sent_speed
            self.total_lan_recv += lan_recv_speed
            print(f"Total WAN Sent: {self.total_wan_sent:.1f} KB, Total WAN Recv: {self.total_wan_recv:.1f} KB")

            total_wan = self.total_wan_recv + self.total_wan_sent
            total_lan = self.total_lan_recv + self.total_lan_sent
            
            # if total_traffic > 0:
            if total_wan > 0:
                # 받는 트래픽 비율 계산 (노란색 부분)
                wan_recv_ratio = (self.total_wan_recv / total_wan) * 100
                wan_progress_bar.setValue(int(wan_recv_ratio))
            if total_lan > 0:
                lan_recv_ratio = (self.total_lan_recv / total_lan) * 100
                lan_progress_bar.setValue(int(lan_recv_ratio))

            if hasattr(self.ui, 'WAN_LABEL') :
                maxKb = 1500
                maxMb = 1500 * 1024
                if total_wan < maxKb:
                    self.ui.WAN_LABEL.setText(f"{total_wan:.1f} KB")
                elif total_wan < maxMb:
                    self.ui.WAN_LABEL.setText(f"{total_wan / 1024:.1f} MB")
                else:
                    self.ui.WAN_LABEL.setText(f"{total_wan / (1024 * 1024):.1f} GB")
            if hasattr(self.ui, 'send_kbs'):
                if total_lan < maxKb:
                    self.ui.LAN_LABEL.setText(f"{total_lan:.1f} KB")
                elif total_lan < maxMb:
                    self.ui.LAN_LABEL.setText(f"{total_lan / 1024:.1f} MB")
                else:
                    self.ui.LAN_LABEL.setText(f"{total_lan / (1024 * 1024):.1f} GB")
                
                # 스타일시트 업데이트

                # style_sheet = f"""
                # QProgressBar {{
                #     border-radius: 37px;
                #     background-color: #ff5151;
                #     text-align: center;
                #     color: black;
                # }}
                
                # QProgressBar::chunk {{
                #     background-color: #fff700;
                #     border-top-left-radius: 37px;
                #     border-bottom-left-radius: 37px;
                # }}
                # """
                # wan_progress_bar.setStyleSheet(style_sheet)

    # def eventFilter(self, obj, event):
    #     if obj == getattr(self, '_lan_bar', None):
    #         if event.type() == QEvent.Enter:
    #             tip = f"LAN\nRecv: {self.total_lan_recv:.1f} KB\nSend: {self.total_lan_sent:.1f} KB"
    #             QToolTip.showText(event.globalPosition().toPoint(), tip, self._lan_bar)
    #             self._last_lan_tooltip = tip
    #         elif event.type() == QEvent.Leave:
    #             QToolTip.hideText()
    #         return False
    #     if obj == getattr(self, '_wan_bar', None):
    #         if event.type() == QEvent.Enter:
    #             tip = f"WAN\nRecv: {self.total_wan_recv:.1f} KB\nSend: {self.total_wan_sent:.1f} KB"
    #             QToolTip.showText(event.globalPosition().toPoint(), tip, self._wan_bar)
    #             self._last_wan_tooltip = tip
    #         elif event.type() == QEvent.Leave:
    #             QToolTip.hideText()
    #         return False
    #     return super().eventFilter(obj, event)

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

