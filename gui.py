# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'braycycle.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_13.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.gammaSB = QDoubleSpinBox(self.centralwidget)
        self.gammaSB.setObjectName(u"gammaSB")
        self.gammaSB.setMinimum(0.100000000000000)
        self.gammaSB.setMaximum(5.000000000000000)
        self.gammaSB.setSingleStep(0.020000000000000)
        self.gammaSB.setValue(1.400000000000000)

        self.horizontalLayout_4.addWidget(self.gammaSB)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.cpSB = QDoubleSpinBox(self.centralwidget)
        self.cpSB.setObjectName(u"cpSB")
        self.cpSB.setDecimals(3)
        self.cpSB.setMinimum(0.010000000000000)
        self.cpSB.setMaximum(5.000000000000000)
        self.cpSB.setSingleStep(0.010000000000000)
        self.cpSB.setValue(1.005000000000000)

        self.horizontalLayout_5.addWidget(self.cpSB)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_12)

        self.rSB = QDoubleSpinBox(self.centralwidget)
        self.rSB.setObjectName(u"rSB")
        self.rSB.setDecimals(3)
        self.rSB.setMinimum(0.010000000000000)
        self.rSB.setMaximum(1.000000000000000)
        self.rSB.setSingleStep(0.010000000000000)
        self.rSB.setValue(0.287000000000000)

        self.horizontalLayout_6.addWidget(self.rSB)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_14)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.InletPressurehorizontalLayout = QHBoxLayout()
        self.InletPressurehorizontalLayout.setObjectName(u"InletPressurehorizontalLayout")
        self.InletPressureSlider = QSlider(self.centralwidget)
        self.InletPressureSlider.setObjectName(u"InletPressureSlider")
        self.InletPressureSlider.setMinimum(10)
        self.InletPressureSlider.setMaximum(1000)
        self.InletPressureSlider.setValue(100)
        self.InletPressureSlider.setOrientation(Qt.Horizontal)

        self.InletPressurehorizontalLayout.addWidget(self.InletPressureSlider)

        self.InletPressureSB = QDoubleSpinBox(self.centralwidget)
        self.InletPressureSB.setObjectName(u"InletPressureSB")
        self.InletPressureSB.setDecimals(0)
        self.InletPressureSB.setMinimum(10.000000000000000)
        self.InletPressureSB.setMaximum(1000.000000000000000)
        self.InletPressureSB.setValue(100.000000000000000)

        self.InletPressurehorizontalLayout.addWidget(self.InletPressureSB)


        self.verticalLayout_2.addLayout(self.InletPressurehorizontalLayout)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.InletTempSlider = QSlider(self.centralwidget)
        self.InletTempSlider.setObjectName(u"InletTempSlider")
        self.InletTempSlider.setMinimum(200)
        self.InletTempSlider.setMaximum(1000)
        self.InletTempSlider.setValue(300)
        self.InletTempSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.InletTempSlider)

        self.InletTempSB = QDoubleSpinBox(self.centralwidget)
        self.InletTempSB.setObjectName(u"InletTempSB")
        self.InletTempSB.setDecimals(0)
        self.InletTempSB.setMinimum(200.000000000000000)
        self.InletTempSB.setMaximum(1000.000000000000000)
        self.InletTempSB.setValue(300.000000000000000)

        self.horizontalLayout_7.addWidget(self.InletTempSB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pressureRatioSlider = QSlider(self.centralwidget)
        self.pressureRatioSlider.setObjectName(u"pressureRatioSlider")
        self.pressureRatioSlider.setMinimum(1)
        self.pressureRatioSlider.setMaximum(30)
        self.pressureRatioSlider.setValue(6)
        self.pressureRatioSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.pressureRatioSlider)

        self.PressureRatioSB = QDoubleSpinBox(self.centralwidget)
        self.PressureRatioSB.setObjectName(u"PressureRatioSB")
        self.PressureRatioSB.setDecimals(1)
        self.PressureRatioSB.setMinimum(1.000000000000000)
        self.PressureRatioSB.setMaximum(30.000000000000000)
        self.PressureRatioSB.setValue(6.000000000000000)

        self.horizontalLayout_8.addWidget(self.PressureRatioSB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_2.addWidget(self.label_15)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.inputVolSlider = QSlider(self.centralwidget)
        self.inputVolSlider.setObjectName(u"inputVolSlider")
        self.inputVolSlider.setMinimum(100)
        self.inputVolSlider.setMaximum(50000)
        self.inputVolSlider.setValue(5000)
        self.inputVolSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.inputVolSlider)

        self.inputVolSB = QDoubleSpinBox(self.centralwidget)
        self.inputVolSB.setObjectName(u"inputVolSB")
        self.inputVolSB.setDecimals(0)
        self.inputVolSB.setMinimum(100.000000000000000)
        self.inputVolSB.setMaximum(50000.000000000000000)
        self.inputVolSB.setSingleStep(100.000000000000000)
        self.inputVolSB.setValue(5000.000000000000000)

        self.horizontalLayout_10.addWidget(self.inputVolSB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.T3Slider = QSlider(self.centralwidget)
        self.T3Slider.setObjectName(u"T3Slider")
        self.T3Slider.setMinimum(300)
        self.T3Slider.setMaximum(500)
        self.T3Slider.setValue(320)
        self.T3Slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.T3Slider)

        self.T3SB = QDoubleSpinBox(self.centralwidget)
        self.T3SB.setObjectName(u"T3SB")
        self.T3SB.setDecimals(0)
        self.T3SB.setMinimum(300.000000000000000)
        self.T3SB.setMaximum(500.000000000000000)
        self.T3SB.setValue(320.000000000000000)

        self.horizontalLayout_9.addWidget(self.T3SB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_9)

        self.Eff_label = QLabel(self.centralwidget)
        self.Eff_label.setObjectName(u"Eff_label")

        self.verticalLayout_4.addWidget(self.Eff_label)

        self.COP_label = QLabel(self.centralwidget)
        self.COP_label.setObjectName(u"COP_label")

        self.verticalLayout_4.addWidget(self.COP_label)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.save_PB = QPushButton(self.centralwidget)
        self.save_PB.setObjectName(u"save_PB")

        self.verticalLayout_2.addWidget(self.save_PB)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.PV_plot_layout = QHBoxLayout()
        self.PV_plot_layout.setObjectName(u"PV_plot_layout")

        self.verticalLayout_3.addLayout(self.PV_plot_layout)

        self.TS_plot_layout = QHBoxLayout()
        self.TS_plot_layout.setObjectName(u"TS_plot_layout")

        self.verticalLayout_3.addLayout(self.TS_plot_layout)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reverse Brayton Cycle Calculator", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Standard Variables", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Gamma", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"C_p", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Input Variables", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Inlet Pressure", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Inlet Temperature", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pressure Ratio", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Input Volume", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Temperature after heat exchange", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.Eff_label.setText(QCoreApplication.translate("MainWindow", u"Efficiency", None))
        self.COP_label.setText(QCoreApplication.translate("MainWindow", u"Coefficient of performance", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.save_PB.setText(QCoreApplication.translate("MainWindow", u"Save to Database", None))
    # retranslateUi

