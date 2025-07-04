from PyQt5.QtWidgets import (
    QMainWindow, QAction, QFileDialog, QApplication, QVBoxLayout, QWidget,
    QHBoxLayout, QPushButton, QSlider, QLabel, QStyle, QSizePolicy
)
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl, Qt, QTime
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Player")
        self.setGeometry(100, 100, 900, 600)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.init_ui()

    def init_ui(self):
        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Video widget
        self.videoWidget = QVideoWidget()

        # Controls with icons and tooltips
        style = self.style()
        self.playBtn = QPushButton()
        self.playBtn.setIcon(style.standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.setToolTip("Play")
        self.playBtn.clicked.connect(self.play_media)
        self.playBtn.setMinimumWidth(40)

        self.pauseBtn = QPushButton()
        self.pauseBtn.setIcon(style.standardIcon(QStyle.SP_MediaPause))
        self.pauseBtn.setToolTip("Pause")
        self.pauseBtn.clicked.connect(self.mediaPlayer.pause)
        self.pauseBtn.setMinimumWidth(40)

        self.stopBtn = QPushButton()
        self.stopBtn.setIcon(style.standardIcon(QStyle.SP_MediaStop))
        self.stopBtn.setToolTip("Stop")
        self.stopBtn.clicked.connect(self.mediaPlayer.stop)
        self.stopBtn.setMinimumWidth(40)

        self.rewindBtn = QPushButton()
        self.rewindBtn.setIcon(style.standardIcon(QStyle.SP_MediaSeekBackward))
        self.rewindBtn.setToolTip("Rewind 5s")
        self.rewindBtn.clicked.connect(self.rewind_media)
        self.rewindBtn.setMinimumWidth(40)

        self.forwardBtn = QPushButton()
        self.forwardBtn.setIcon(style.standardIcon(QStyle.SP_MediaSeekForward))
        self.forwardBtn.setToolTip("Forward 5s")
        self.forwardBtn.clicked.connect(self.forward_media)
        self.forwardBtn.setMinimumWidth(40)

        self.fullscreenBtn = QPushButton()
        self.fullscreenBtn.setIcon(style.standardIcon(QStyle.SP_TitleBarMaxButton))
        self.fullscreenBtn.setToolTip("Toggle Fullscreen")
        self.fullscreenBtn.clicked.connect(self.toggle_fullscreen)
        self.fullscreenBtn.setMinimumWidth(40)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)
        self.slider.setMinimumWidth(200)
        self.slider.setToolTip("Seek")

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(50)
        self.volumeSlider.valueChanged.connect(self.mediaPlayer.setVolume)
        self.volumeSlider.setMinimumWidth(80)
        self.volumeSlider.setToolTip("Volume")

        self.timeLabel = QLabel("00:00 / 00:00")
        self.timeLabel.setMinimumWidth(90)
        self.timeLabel.setAlignment(Qt.AlignCenter)

        self.fileLabel = QLabel("No file loaded")
        self.fileLabel.setAlignment(Qt.AlignCenter)
        self.fileLabel.setStyleSheet("font-weight: bold; margin: 8px;")

        # Control bar styling
        controlBar = QWidget()
        controlBarLayout = QHBoxLayout()
        controlBarLayout.setContentsMargins(10, 5, 10, 5)
        controlBarLayout.setSpacing(12)
        controlBar.setLayout(controlBarLayout)
        controlBar.setAutoFillBackground(True)
        palette = controlBar.palette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        controlBar.setPalette(palette)

        # Add controls to control bar
        controlBarLayout.addWidget(self.rewindBtn)
        controlBarLayout.addWidget(self.playBtn)
        controlBarLayout.addWidget(self.pauseBtn)
        controlBarLayout.addWidget(self.stopBtn)
        controlBarLayout.addWidget(self.forwardBtn)
        controlBarLayout.addWidget(self.slider, 1)
        controlBarLayout.addWidget(self.timeLabel)
        controlBarLayout.addWidget(QLabel("🔊"))
        controlBarLayout.addWidget(self.volumeSlider)
        controlBarLayout.addWidget(self.fullscreenBtn)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget, stretch=1)
        layout.addWidget(self.fileLabel)
        layout.addWidget(controlBar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        # Connections
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Media File", "", 
            "Media Files (*.mp4 *.mp3 *.avi *.mkv);;All Files (*)", options=options)
        if file_name:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.fileLabel.setText(os.path.basename(file_name))
            self.mediaPlayer.play()

    def play_media(self):
        self.mediaPlayer.play()

    def position_changed(self, position):
        self.slider.setValue(position)
        duration = self.mediaPlayer.duration()
        if duration > 0:
            current_time = QTime(0, 0, 0).addMSecs(position)
            total_time = QTime(0, 0, 0).addMSecs(duration)
            self.timeLabel.setText(f"{current_time.toString('mm:ss')} / {total_time.toString('mm:ss')}")
        else:
            self.timeLabel.setText("00:00 / 00:00")

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def toggle_fullscreen(self):
        if self.videoWidget.isFullScreen():
            self.videoWidget.setFullScreen(False)
            self.fileLabel.show()
            self.centralWidget().layout().itemAt(1).widget().show()
        else:
            self.videoWidget.setFullScreen(True)
            self.fileLabel.hide()
            self.centralWidget().layout().itemAt(1).widget().hide()

    def rewind_media(self):
        self.mediaPlayer.setPosition(max(0, self.mediaPlayer.position() - 5000))

    def forward_media(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 5000)

    def mouseDoubleClickEvent(self, event):
        if self.videoWidget.underMouse():
            self.toggle_fullscreen()

def keyPressEvent(self, event):
    if event.key() == Qt.Key_F:
        self.toggle_fullscreen()
    elif event.key() == Qt.Key_Escape and self.videoWidget.isFullScreen():
        self.toggle_fullscreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())