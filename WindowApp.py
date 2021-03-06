from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QLabel, QMainWindow, QSlider, QSizePolicy, QStatusBar, QSystemTrayIcon, QWidget
from screen_dimmer import *


class TrayApp(QSystemTrayIcon):

    def __init__(self):
        super(TrayApp, self).__init__()
        self.window = WindowApp()
        self.window.setup_ui(self.window)
        self.setup_system_tray()

    def setup_system_tray(self):
        # Adding item on the menu bar
        self.setIcon(QIcon("Screen_Dimmer_Logo.ico"))
        self.setVisible(True)
        self.activated.connect(self.window.show)
        self.setToolTip("Screen Dimmer - Made by Jackson Elia")


class WindowApp(QMainWindow):

    def __init__(self):
        super(WindowApp, self).__init__()

    def setup_ui(self, MainWindow):
        self.setWindowIcon(QIcon("Screen_Dimmer_Logo.ico"))
        MainWindow.setObjectName("MainWindow")
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(40, 40, 40)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider_1 = QSlider(self.centralwidget)
        self.horizontalSlider_1.setGeometry(QRect(150, 130, 500, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_1.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_1.setSizePolicy(sizePolicy)
        self.horizontalSlider_1.setStyleSheet("")
        self.horizontalSlider_1.setOrientation(Qt.Horizontal)
        self.horizontalSlider_1.setObjectName("horizontalSlider")
        self.horizontalSlider_1.valueChanged.connect(lambda: change_all_brightness(self.horizontalSlider_1.value() + 1)),
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setGeometry(QRect(150, 100, 501, 20))
        font = QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: white")
        self.label_1.setObjectName("label")
        self.horizontalSlider_2 = QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QRect(150, 210, 500, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.valueChanged.connect(lambda: sbc.set_brightness(self.horizontalSlider_2.value() + 1, 0))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(150, 180, 501, 20))
        font = QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        self.horizontalSlider_3 = QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QRect(150, 270, 500, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_3.setSizePolicy(sizePolicy)
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.valueChanged.connect(lambda: sbc.set_brightness(self.horizontalSlider_3.value() + 1, 1))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(150, 240, 501, 20))
        font = QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        self.horizontalSlider_4 = QSlider(self.centralwidget)
        # 150, 390, 500, 20
        self.horizontalSlider_4.setGeometry(QRect(150, 330, 500, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_4.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_4.setSizePolicy(sizePolicy)
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_4.valueChanged.connect(lambda: sbc.set_brightness(self.horizontalSlider_4.value() + 1, 2))
        self.label_4 = QLabel(self.centralwidget)
        # 150, 360, 501, 20
        self.label_4.setGeometry(QRect(150, 300, 501, 20))
        font = QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white")
        self.label_4.setObjectName("label_4")
        self.horizontalSlider_5 = QSlider(self.centralwidget)
        # 150, 330, 500, 20
        self.horizontalSlider_5.setGeometry(QRect(150, 390, 500, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_5.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_5.setSizePolicy(sizePolicy)
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.horizontalSlider_5.valueChanged.connect(lambda: sbc.set_brightness(self.horizontalSlider_5.value() + 1, 3))
        self.label_5 = QLabel(self.centralwidget)
        # 150, 300, 501, 20
        self.label_5.setGeometry(QRect(150, 360, 501, 20))
        font = QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white")
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setGeometry(QRect(150, 420, 501, 20))
        font = QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white")
        self.label_6.setObjectName("label_6")
        self.horizontalSlider_6 = QSlider(self.centralwidget)
        self.horizontalSlider_6.setGeometry(QRect(150, 450, 500, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_6.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_6.setSizePolicy(sizePolicy)
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.horizontalSlider_6.valueChanged.connect(lambda: sbc.set_brightness(self.horizontalSlider_6.value() + 1, 4))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # Custom method that disabled sliders based on how many displays there is
        self.disable_sliders(get_displays())

    def retranslate_ui(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Screen Dimmer"))
        self.label_1.setText(_translate("MainWindow", "Adjust All Monitors"))
        self.label_2.setText(_translate("MainWindow", "Monitor #1"))
        self.label_3.setText(_translate("MainWindow", "Monitor #2"))
        self.label_4.setText(_translate("MainWindow", "Monitor #3"))
        self.label_5.setText(_translate("MainWindow", "Monitor #4"))
        self.label_6.setText(_translate("MainWindow", "Monitor #5"))

    def disable_sliders(self, number_of_displays):
        match number_of_displays:
            case 1:
                self.horizontalSlider_3.setVisible(False)
                self.horizontalSlider_4.setVisible(False)
                self.horizontalSlider_5.setVisible(False)
                self.horizontalSlider_6.setVisible(False)
                self.label_3.setVisible(False)
                self.label_4.setVisible(False)
                self.label_5.setVisible(False)
                self.label_6.setVisible(False)
                self.setFixedHeight(360)
            case 2:
                self.horizontalSlider_4.setVisible(False)
                self.horizontalSlider_5.setVisible(False)
                self.horizontalSlider_6.setVisible(False)
                self.label_4.setVisible(False)
                self.label_5.setVisible(False)
                self.label_6.setVisible(False)
                self.setFixedHeight(420)
            case 3:
                self.horizontalSlider_5.setVisible(False)
                self.horizontalSlider_6.setVisible(False)
                self.label_5.setVisible(False)
                self.label_6.setVisible(False)
                self.setFixedHeight(480)
            case 4:
                self.horizontalSlider_6.setVisible(False)
                self.label_6.setVisible(False)
                self.setFixedHeight(540)
            case 5:
                # Window is set up by default for 5 displays
                pass
