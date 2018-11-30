# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tractorpull_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import threading
import time

#Global Variables
CURRENTVALUE = 0
POWER = 0
DIRECTION = "N/A"
SPEED = 0
OBSTICLE = "False"
TRAILER = "True"
START = "False"
ERROR = "0"
FRAME_CHANGE_FLAG_1 = 0
ERROR_FLAG = 0
        

ip = "172.22.20.18"


class Ui_tractorpull_main(object):
    def setupUi(self, tractorpull_main):
    
        #parameters of the main window..colour/shape/size etc
        tractorpull_main.setObjectName("tractorpull_main")
        tractorpull_main.resize(560, 459)

        #MenuBar doesn't work, playing around with it
        self.centralWidget = QtWidgets.QWidget(tractorpull_main)
        self.centralWidget.setObjectName("centralWidget")
        tractorpull_main.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(tractorpull_main)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 608, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuTractorPull = QtWidgets.QMenu(self.menuBar)
        self.menuTractorPull.setObjectName("menuTractorPull")
        tractorpull_main.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(tractorpull_main)
        self.mainToolBar.setObjectName("mainToolBar")
        tractorpull_main.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(tractorpull_main)
        self.statusBar.setObjectName("statusBar")
        tractorpull_main.setStatusBar(self.statusBar)
        self.actionSoft_Reset = QtWidgets.QAction(tractorpull_main)
        self.actionSoft_Reset.setObjectName("actionSoft_Reset")
        self.actionShut_it_all_Down = QtWidgets.QAction(tractorpull_main)
        self.actionShut_it_all_Down.setObjectName("actionShut_it_all_Down")
        self.menuTractorPull.addAction(self.actionSoft_Reset)
        self.menuTractorPull.addSeparator()
        self.menuBar.addAction(self.menuTractorPull.menuAction())
       
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        tractorpull_main.setPalette(palette)
        self.MAIN = QtWidgets.QWidget(tractorpull_main)
        self.MAIN.setObjectName("MAIN")

        #Warning Frame 
        self.Frame_Warning = QtWidgets.QFrame(self.MAIN)
        self.Frame_Warning.setGeometry(QtCore.QRect(60, 140, 441, 251))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Frame_Warning.setFont(font)
        self.Frame_Warning.setStyleSheet("border-color: rgb(170, 0, 0);\n"
                                         "background-color: rgb(255,255,255);")
        self.Frame_Warning.setFrameShape(QtWidgets.QFrame.Box)
        self.Frame_Warning.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Frame_Warning.setLineWidth(5)
        self.Frame_Warning.setObjectName("Frame_Warning")
        self.Warning = QtWidgets.QLabel(self.Frame_Warning)
        self.Warning.setGeometry(QtCore.QRect(140, 10, 151, 61))

        #Warning Label on the Warning Frame
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Warning.setFont(font)
        self.Warning.setStyleSheet("color: rgb(255, 0, 0);")
        self.Warning.setObjectName("Warning")

        #Obsticle warning text on top of the Warning Frame
        self.Obsticle_Dectection_Warning = QtWidgets.QLabel(self.Frame_Warning)
        self.Obsticle_Dectection_Warning.setGeometry(QtCore.QRect(30, 100, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Obsticle_Dectection_Warning.setFont(font)
        self.Obsticle_Dectection_Warning.setObjectName("Obsticle_Dectection_Warning")

        #Trailer connection warning text on top of the Warning Frame
        self.Trailer_Not_Detected = QtWidgets.QLabel(self.Frame_Warning)
        self.Trailer_Not_Detected.setGeometry(QtCore.QRect(130, 70, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Trailer_Not_Detected.setFont(font)
        self.Trailer_Not_Detected.setObjectName("Trailer_Not_Detected")

        #Pushbutton to signal that the warning has been acknowledged
        self.YES = QtWidgets.QPushButton(self.Frame_Warning)
        self.YES.setGeometry(QtCore.QRect(130, 180, 171, 51))
        self.YES.setObjectName("YES")

        #Frame used to hide / show the trailer warnings
        self.Trailer_Warning_Hide = QtWidgets.QFrame(self.Frame_Warning)
        self.Trailer_Warning_Hide.setGeometry(QtCore.QRect(70, 60, 291, 31))
        self.Trailer_Warning_Hide.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Trailer_Warning_Hide.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Trailer_Warning_Hide.setObjectName("Trailer_Warning_Hide")

        #Frame used to hide / show the obsticle warnings
        self.Obsticle_Warning_Hide = QtWidgets.QFrame(self.Frame_Warning)
        self.Obsticle_Warning_Hide.setGeometry(QtCore.QRect(20, 100, 381, 71))
        self.Obsticle_Warning_Hide.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Obsticle_Warning_Hide.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Obsticle_Warning_Hide.setObjectName("Obsticle_Warning_Hide")
        self.Obsticle_Removal = QtWidgets.QLabel(self.Obsticle_Warning_Hide)
        self.Obsticle_Removal.setGeometry(QtCore.QRect(160, 40, 91, 21))

        #Text telling user to remove the detected obsticle
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Obsticle_Removal.setFont(font)
        self.Obsticle_Removal.setObjectName("Obsticle_Removal")

        #default status of all frames and labels on the warning_frame... show/hide
        self.Trailer_Warning_Hide.lower()
        self.Obsticle_Warning_Hide.lower()
        self.Warning.lower()
        self.Obsticle_Dectection_Warning.lower()
        self.Trailer_Not_Detected.lower()
        self.YES.raise_()

        #Frame containing Current, Directin and Battery widgets
        self.Frame_Value = QtWidgets.QFrame(self.MAIN)
        self.Frame_Value.setGeometry(QtCore.QRect(10, 20, 541, 381))
        self.Frame_Value.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Frame_Value.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_Value.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Value.setObjectName("Frame_Value")
        self.Direction = QtWidgets.QLabel(self.Frame_Value)
        self.Direction.setGeometry(QtCore.QRect(20, 90, 91, 21))

        #Direction label on the Value Frame
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Direction.setFont(font)
        self.Direction.setObjectName("Direction")
        self.Current = QtWidgets.QLabel(self.Frame_Value)
        self.Current.setGeometry(QtCore.QRect(20, 60, 71, 31))

        #Current label on the Value Frame
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Current.setFont(font)
        self.Current.setObjectName("Current")
        self.BatteryPower = QtWidgets.QProgressBar(self.Frame_Value)
        self.BatteryPower.setGeometry(QtCore.QRect(390, 70, 141, 21))
    

        #Details of Battery Power 'Progress Bar'...colour/shape/size etc
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.BatteryPower.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BatteryPower.setFont(font)
        self.BatteryPower.setProperty("value", 24)
        self.BatteryPower.setObjectName("BatteryPower")

        #Label to display the Current Value
        self.Curent_Value = QtWidgets.QLabel(self.Frame_Value)
        self.Curent_Value.setGeometry(QtCore.QRect(120, 70, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Curent_Value.setFont(font)
        self.Curent_Value.setObjectName("Curent_Value")

        #label to title the 'progress bar' as battery power
        self.Battery = QtWidgets.QLabel(self.Frame_Value)
        self.Battery.setGeometry(QtCore.QRect(420, 93, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Battery.setFont(font)
        self.Battery.setObjectName("Battery")

        #Label to display the direction
        self.Direction_Value = QtWidgets.QLabel(self.Frame_Value)
        self.Direction_Value.setGeometry(QtCore.QRect(120, 90, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Direction_Value.setFont(font)
        self.Direction_Value.setObjectName("Direction_Value")

        #Frame containing the start 'screen'
        self.Start_Hide_Frame = QtWidgets.QFrame(self.MAIN)
        self.Start_Hide_Frame.setGeometry(QtCore.QRect(0, 0, 561, 421))
        self.Start_Hide_Frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Start_Hide_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Start_Hide_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Start_Hide_Frame.setObjectName("Start_Hide_Frame")
        self.Start_PB = QtWidgets.QPushButton(self.Start_Hide_Frame)
        self.Start_PB.setGeometry(QtCore.QRect(170, 150, 191, 91))

        #parameters of the start button.... colour/shape/size etc
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Start_PB.setPalette(palette)

        #Text appearing on the start pushbutton
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Start_PB.setFont(font)
        self.Start_PB.setAutoFillBackground(False)
        self.Start_PB.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.Start_PB.setObjectName("Start_PB")

        #default status of all frames on the main window... show/hide
        self.Start_Hide_Frame.raise_()
        self.Frame_Value.lower()
        self.Frame_Warning.lower()

        #parameters of the Error Message Frame
        self.Error_Msg_Frame = QtWidgets.QFrame(self.Frame_Value)
        self.Error_Msg_Frame.setGeometry(QtCore.QRect(10, 10, 521, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Error_Msg_Frame.setPalette(palette)
        self.Error_Msg_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.Error_Msg_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Error_Msg_Frame.setLineWidth(4)
        self.Error_Msg_Frame.setMidLineWidth(2)
        self.Error_Msg_Frame.setObjectName("Error_Msg_Frame")
        self.Error = QtWidgets.QLabel(self.Error_Msg_Frame)
        self.Error.setGeometry(QtCore.QRect(10, 10, 81, 31))

        #Text Label to display the title Error:
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Error.setFont(font)
        self.Error.setObjectName("Error")

        #Text label to display the error message
        self.Error_Msg = QtWidgets.QLabel(self.Error_Msg_Frame)
        self.Error_Msg.setGeometry(QtCore.QRect(80, 10, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Error_Msg.setFont(font)
        self.Error_Msg.setObjectName("Error_Msg")

        #pushbutton to shut everything down
        #self.centralWidget = QtWidgets.QWidget(tractorpull_main)
        #self.centralWidget.setObjectName("centralWidget")
        self.Shutdown = QtWidgets.QPushButton(self.MAIN)
        self.Shutdown.setGeometry(QtCore.QRect(505, 355, 41, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.Shutdown.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Shutdown.setFont(font)
        self.Shutdown.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "selection-color: rgb(255, 255, 255);")
        self.Shutdown.setObjectName("Shutdown")
        self.Shutdown.hide()
        
        #initilization of application
        tractorpull_main.setCentralWidget(self.MAIN)
        self.retranslateUi(tractorpull_main)
        QtCore.QMetaObject.connectSlotsByName(tractorpull_main)

        #start button event... connected to Start_Pushed slot
        self.Start_PB.clicked.connect(self.Start_Pushed)

        #acknowledge button event... connected to yes_pushed slot
        self.YES.clicked.connect(self.yes_pushed)

        #exit button event...connected to Exit_PB slot
        self.Shutdown.clicked.connect(self.Exit_PB)
        
        #update all labels and frames with data revceived through the server connections
        #... event is repeatedly triggered by run time timer
        self.Update()


        #playing with a menubar
        #extractAction = QtWidgets.QAction("Kill It!!", self)
        #extractAction.setShortcut("ESC")
        #mainMenu = self.menuBar()
        #fileMenu = mainMenu.addMenu('&File')
        #fileMenu.addAction(extractAction)
        
    #Method containning initilization of application   
    def retranslateUi(self, tractorpull_main):
        _translate = QtCore.QCoreApplication.translate
        tractorpull_main.setWindowTitle(_translate("tractorpull_main", "Tractor Pull"))
        #self.setWindowIcon(QtGui.QIcon(''))
        self.Warning.setText(_translate("tractorpull_main", "WARNING"))
        self.Obsticle_Dectection_Warning.setText(_translate("tractorpull_main", "Obsticle Dectect: Manual Removal Needed"))
        self.Trailer_Not_Detected.setText(_translate("tractorpull_main", "Trailer Not Dectected"))
        self.YES.setText(_translate("tractorpull_main", "YES"))
        self.Obsticle_Removal.setText(_translate("tractorpull_main", "Conintue?"))
        self.Direction.setText(_translate("tractorpull_main", "Direction:"))
        self.Current.setText(_translate("tractorpull_main", "Current:"))
        self.Curent_Value.setText(_translate("tractorpull_main", "Current_Value"))
        self.Battery.setText(_translate("tractorpull_main", "Battery"))
        self.Direction_Value.setText(_translate("tractorpull_main", "Direction_Value"))
        self.Shutdown.setText(_translate("tractorpull_main", "EXIT"))
        self.Start_PB.setText(_translate("tractorpull_main", "START"))
        self.Error.setText(_translate("tractorpull_main", "Error:"))
        self.Error_Msg.setText(_translate("tractorpull_main", "Error_Msg"))
        self.Shutdown.setText(_translate("tractorpull_main", "EXIT"))

        
        #self.menuTractorPull.setTitle(_translate("tractorpull_main", "Kill Features"))
        #self.actionSoft_Reset.setText(_translate("tractorpull_main", "Its grown a Brain and gone AWOL. Quick Kill it!"))
        #self.actionShut_it_all_Down.setText(_translate("tractorpull_main", "Shut it all Down"))

        
    #Slot containing details of what happens when Start PB is clicked
    def Start_Pushed(self):
        global START
        global FRAME_CHANGE_FLAG_1
        print("start pressed\n\r")
        #publish.single("Start", "True", hostname=ip)
        
        #if START == "True":
            #print ("starting\n\r")
        publish.single("Start", "True", hostname=ip)
        self.Start_Hide_Frame.lower()
        self.Shutdown.show()
        FRAME_CHANGE_FLAG_1 = 1
        #else:
            #print("waiting for publish\n\r")

    def Exit_PB(self):
        publish.single("Reset", "True", hostname=ip)
        #publish.single("Shutdown", "True", hostname=ip)

        global CURRENTVALUE
        global POWER
        global DIRECTION
        global SPEED
        global OBSTICLE
        global TRAILER
        global START
        global ERROR
        global FRAME_CHANGE_FLAG_1
        global ERROR_FLAG

        #resets all variables to default values
        CURRENTVALUE = 0
        POWER = 0
        DIRECTION = "N/A"
        SPEED = 0
        OBSTICLE = "False"
        TRAILER = "True"
        START = "False"
        ERROR = "0"
        FRAME_CHANGE_FLAG_1 = 0
        ERROR_FLAG = 0

        #resets all frames to original position
        self.Trailer_Warning_Hide.lower()
        self.Obsticle_Warning_Hide.lower()
        self.Warning.lower()
        self.Obsticle_Dectection_Warning.lower()
        self.Trailer_Not_Detected.lower()
        self.Start_Hide_Frame.raise_()
        self.Shutdown.show()
        self.Error_Msg_Frame.hide()
 
    #Slot containing details of what happens when YES PB is clicked
    def yes_pushed(self):
        global TRAILER
        global OBSTICLE
        
        if (TRAILER == "False") or (OBSTICLE == "True"):
            #publish.single("Start", "True", hostname=ip)
            
            publish.single("Reset", "True", hostname=ip)
        self.Frame_Warning.lower()
        self.Obsticle_Dectection_Warning.lower()
        self.Trailer_Not_Detected.lower()
        publish.single("Reset", "True", hostname=ip)

    #Method containing details of what and how often the UI is updated with current information              
    def Update(self):
        global TRAILER
        global START
        global SPEED
        global OBSTICLE
        global ERROR
        global FRAME_CHANGE_FLAG_1

        #takes contents of variables and sets it as the label
        self.Curent_Value.setText( str(CURRENTVALUE) + " A" )
        self.Direction_Value.setText( str(DIRECTION) )
        self.BatteryPower.setProperty("value", POWER)
        self.Error_Msg.setText( str(ERROR) )

        #determines if a warning message has been received
        if (FRAME_CHANGE_FLAG_1 == 1) and ((TRAILER == "False") or (OBSTICLE == "True")):

            #shows the Frame Warning
            self.Frame_Warning.raise_()

            #determines and shows what warning has occured
            if (TRAILER == "False"):
                self.Trailer_Not_Detected.raise_()
            else:
                self.Trailer_Not_Detected.lower()
                
            if (OBSTICLE == "True"):
                self.Obsticle_Dectection_Warning.raise_()
            else:
                self.Obsticle_Dectection_Warning.lower()
                
        else:
            self.Frame_Warning.lower()
            self.Obsticle_Dectection_Warning.lower()
            self.Trailer_Not_Detected.lower()
            
        #determines if an Error Message has been received
        if (ERROR == "Finished") and (FRAME_CHANGE_FLAG_1 == 1):
            
            self.Trailer_Warning_Hide.lower()
            self.Obsticle_Warning_Hide.lower()
            self.Warning.lower()
            self.Obsticle_Dectection_Warning.lower()
            self.Trailer_Not_Detected.lower()
            self.Start_Hide_Frame.raise_()
            self.Shutdown.show()
            self.Error_Msg_Frame.hide()
            
            FRAME_CHANGE_FLAG_1 = 0
     
            
            
        else:
            self.Error_Msg_Frame.show()
         
        #Run time timer to call the function again in 3 seconds   
        QtCore.QTimer.singleShot(20, self.Update)
        

#function that connects to the server (mosquitto broker) via topics
#and listens for messages
def on_connect(client, userdata, flags, rc):
    print("On connect")
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Compass")
    client.subscribe("Current")
    client.subscribe("Obsticle")
    client.subscribe("Trailer")
    client.subscribe("Speed")
    client.subscribe("Start")
    client.subscribe("Error")
    client.subscribe("Power")
    client.subscribe("Process")
    client.subscribe("Reset")

#function that determines what happens to the received messages
def on_message(client, userdata, msg):
    global DIRECTION
    global CURRENTVALUE
    global OBSTICLE
    global SPEED
    global START
    global TRAILER
    global ERROR
    global POWER
    
    print (msg.topic)
    print( msg.payload.decode() )
    if msg.topic == "Speed":
        #payload either 0, 1, or 2
        SPEED = msg.payload.decode()
        print(SPEED)
        
    if msg.topic == "Current":
        CURRENTVALUE = msg.payload.decode()
        #float(CURRENTVALUE)
        #CURRENTVALUE = round( )
        print(CURRENTVALUE)
        
    if msg.topic == "Compass":
        DIRECTION = str( msg.payload.decode() )
        print(DIRECTION)

    if msg.topic == "Obsticle":
        #payload either TRUE or FALSE
        OBSTICLE = msg.payload.decode()
        print(OBSTICLE)

    if msg.topic == "Trailer":
        #payload either TRUE or FALSE
        TRAILER = msg.payload.decode()
        print(TRAILER)

    if msg.topic == "Start":
        #payload either TRUE or FALSE
        START = msg.payload.decode()
        print(START)

    if msg.topic == "Error":
        ERROR = str( msg.payload.decode() )
        print(ERROR)

    if msg.topic == "Power":
        POWER = msg.payload.decode()
        print(POWER)


#function handling connection to the server, cannot leave it in listening
#state, will only listen for a partial time to allow the UI to execute
#the Update method
def mqttThings():

    while True:
        lock.acquire()
        client.loop_start()
        client.loop_stop()
        lock.release()
        time.sleep(0.1)


if __name__ == "__main__":

    lock = threading.Lock()
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(ip, 1883, 60)
    
    #needed to make the connection to the server into a thread so other process could
    #still run
    tmqtt = threading.Thread(target = mqttThings)
    tmqtt.start()

    #initilization of UI
    app = QtWidgets.QApplication(sys.argv)
    tractorpull_main = QtWidgets.QMainWindow()
    ui = Ui_tractorpull_main()
    ui.setupUi(tractorpull_main)
    tractorpull_main.show()     
    sys.exit(app.exec_())

    

    
 
   
    

   
    


