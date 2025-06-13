# -*- coding: utf-8 -*-
# 进度条
from PyQt5.QtWidgets import QDialog, QLabel, QProgressBar, QPushButton, QVBoxLayout, QHBoxLayout


class ProgressBar(QDialog):
    def __init__(self, parent=None):
        super(ProgressBar, self).__init__(parent)

        self.resize(350, 100)
        self.setWindowTitle(self.tr("视频保存进度信息"))

        self.TipLabel = QLabel(self.tr("当前帧/总帧数:0/0"))
        self.FeatLabel = QLabel(self.tr("保存进度:"))

        self.FeatProgressBar = QProgressBar(self)
        self.FeatProgressBar.setMinimum(0)
        self.FeatProgressBar.setMaximum(100)  # 总进程换算为100
        self.FeatProgressBar.setValue(0)  # 进度条初始值为0

        TipLayout = QHBoxLayout()
        TipLayout.addWidget(self.TipLabel)

        FeatLayout = QHBoxLayout()
        FeatLayout.addWidget(self.FeatLabel)
        FeatLayout.addWidget(self.FeatProgressBar)

        self.cancelButton = QPushButton('取消保存', self)

        buttonlayout = QHBoxLayout()
        buttonlayout.addStretch(1)
        buttonlayout.addWidget(self.cancelButton)

        layout = QVBoxLayout()
        layout.addLayout(FeatLayout)
        layout.addLayout(TipLayout)
        layout.addLayout(buttonlayout)
        self.setLayout(layout)
        self.cancelButton.clicked.connect(self.onCancel)
        # self.show()

    def setValue(self, start, end, progress):
        self.TipLabel.setText(self.tr("当前帧/总帧数:" + "   " + str(start) + "/" + str(end)))
        self.FeatProgressBar.setValue(progress)

    def onCancel(self, event):
        self.close()