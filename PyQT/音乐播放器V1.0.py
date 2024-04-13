import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSlider, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist,QMediaContent
from PyQt5.QtCore import Qt, QUrl


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('音乐播放器')
        self.setGeometry(300, 300, 300, 200)

        # 创建布局
        layout = QVBoxLayout()

        # 创建媒体播放器和播放列表
        self.player = QMediaPlayer(None, QMediaPlayer.StreamPlayback)
        self.playlist = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playlist)

        # 创建标签来显示当前播放的歌曲
        self.current_song_label = QLabel('未选择歌曲', self)
        layout.addWidget(self.current_song_label)

        # 创建按钮来打开文件对话框并选择歌曲
        self.open_button = QPushButton('打开歌曲', self)
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        # 创建播放/暂停按钮
        self.play_pause_button = QPushButton('播放/暂停', self)
        self.play_pause_button.clicked.connect(self.play_pause)
        layout.addWidget(self.play_pause_button)

        # 创建滑块来控制音量
        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.set_volume)
        layout.addWidget(self.volume_slider)

        # 设置布局
        self.setLayout(layout)

    def open_file(self):
        # 打开文件对话框并选择歌曲文件
        file_name, _ = QFileDialog.getOpenFileName(self, '打开歌曲', '', '音频文件 (*.mp3 *.wav *.ogg)')
        if file_name:
            # 将QUrl转换为QMediaContent，然后添加到播放列表并播放
            media_content = QMediaContent(QUrl.fromLocalFile(file_name))
            self.playlist.clear()
            self.playlist.addMedia(media_content)
            self.player.play()
            self.current_song_label.setText(file_name.split('/')[-1])

    def play_pause(self):
        # 切换播放/暂停状态
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.play_pause_button.setText('播放')
        else:
            self.player.play()
            self.play_pause_button.setText('暂停')

    def set_volume(self, volume):
        # 设置音量
        self.player.setVolume(volume)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MusicPlayer()
    ex.show()
    sys.exit(app.exec_())