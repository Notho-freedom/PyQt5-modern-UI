# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacesBCtSV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar
from PySide2.QtWebEngineWidgets import QWebEngineView
import Widgets
from Widgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 432)
        MainWindow.setStyleSheet(u"*{\n"
"background-color: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"border: none;\n"
"color: #fff;\n"
"}\n"
"#centralwidget{\n"
"background-color: rgb(39, 43, 54);\n"
"}\n"
"#toggle_button_cont{\n"
"background-color: rgb(28, 37, 49);\n"
"}\n"
"#left_menu_main_container > QWidget{\n"
"border-bottom: 2px solid rgb(28, 37, 49);\n"
"}\n"
"#left_menu_main_container QPushButton{\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"}\n"
"QStackedWidget > QWidget{\n"
"background-color: rgb(20, 28, 39);\n"
"}\n"
"")
#==================================================================bigin=========
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
#==========================================Vertical==BoxLayout==and attributes======
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#==========================================header widget=========
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
#=========================horizontal boxlayout==in header= and attributes=============
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
#===========================toggle_button zone for menu= in header=======
        self.toggle_button_cont = QWidget(self.header)
        self.toggle_button_cont.setObjectName(u"toggle_button_cont")
#============================horizotalLayout====in toggle zone= and attributes====
        self.horizontalLayout_2 = QHBoxLayout(self.toggle_button_cont)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
#=================action_button::PushButton for toggle== and attribut======
        self.toggle_button = QPushButton(self.toggle_button_cont)
        self.toggle_button.setObjectName(u"toggle_button")
        self.toggle_button.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.toggle_button.setFont(font)
#====================Icon for toggle button=========
        icon = QIcon()
        icon.addFile(u":/icons/icons/grid.svg", QSize(), QIcon.Normal, QIcon.Off)
#====================setIcon=========
        self.toggle_button.setIcon(icon)
#===============Icon size=======
        self.toggle_button.setIconSize(QSize(32, 32))
#==================add toggle button in toggle container:: horizontalLayout2=========
        self.horizontalLayout_2.addWidget(self.toggle_button, 0, Qt.AlignLeft)
#=================add toggle contain in toggle zone=========
        self.horizontalLayout_3.addWidget(self.toggle_button_cont, 0, Qt.AlignLeft)

        self.widget_6 = QWidget(self.header)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(self.widget_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pushButton_8)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)


        self.horizontalLayout_6.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.widget_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_12 = QPushButton(self.frame_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.pushButton_12)

        self.restoreWindow = QPushButton(self.frame_3)
        self.restoreWindow.setObjectName(u"restoreWindow")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreWindow.setIcon(icon3)
        self.restoreWindow.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.restoreWindow)

        self.minimizeWindow = QPushButton(self.frame_3)
        self.minimizeWindow.setObjectName(u"minimizeWindow")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/minus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeWindow.setIcon(icon4)
        self.minimizeWindow.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.minimizeWindow)

        self.closeWindow = QPushButton(self.frame_3)
        self.closeWindow.setObjectName(u"closeWindow")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindow.setIcon(icon5)
        self.closeWindow.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.closeWindow)

        self.horizontalLayout_6.addWidget(self.frame_3, 0, Qt.AlignRight)

        self.horizontalLayout_3.addWidget(self.widget_6)

        self.verticalLayout.addWidget(self.header)
#============================End of Header=========

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.left_menu_main_container = QCustomSlideMenu(self.widget_2)
        self.left_menu_main_container.setObjectName(u"left_menu_main_container")
        self.left_menu_main_container.setMinimumSize(QSize(200, 350))
#====================contain menu name-icon=========
        self.verticalLayout_2 = QVBoxLayout(self.left_menu_main_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_menu_container = QWidget(self.left_menu_main_container)
        self.top_menu_container.setObjectName(u"top_menu_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_menu_container.sizePolicy().hasHeightForWidth())
        self.top_menu_container.setSizePolicy(sizePolicy1)

        self.verticalLayout_3 = QVBoxLayout(self.top_menu_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)






        self.widget_3 = QWidget(self.top_menu_container)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)

        self.dashboard_btn = QPushButton(self.widget_3)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        self.dashboard_btn.setStyleSheet(u"background-color: transparent;\n")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/slack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon6)
        self.dashboard_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.dashboard_btn)

        self.projects_btn = QPushButton(self.widget_3)
        self.projects_btn.setObjectName(u"projects_btn")
        self.projects_btn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.projects_btn.setIcon(icon7)
        self.projects_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.projects_btn)

        self.reports_btn = QPushButton(self.widget_3)
        self.reports_btn.setObjectName(u"reports_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reports_btn.setIcon(icon8)
        self.reports_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.reports_btn)

#=================my menu button===============
        self.db_btn = QPushButton(self.widget_3)
        self.db_btn.setObjectName(u"bd_btn")
        icondb = QIcon()
        icondb.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.db_btn.setIcon(icondb)
        self.db_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.db_btn)

#==============================================

        self.verticalLayout_3.addWidget(self.widget_3, 0, Qt.AlignTop)
























        self.toolBox = QToolBox(self.top_menu_container)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QToolBox{\n"
"   background-color: rgb(20, 28, 39);\n"
"   text-align: left;\n"
"   border: 1px solid rgb(20, 28, 39);\n"
"}\n"
"QPushButton{\n"
"   background-color: transparent;\n"
"   border: 2px solid transparent;\n"
"   padding: 10px 5px;\n"
"   border-radius: 5px;\n"
"   text-align: left;\n"
"}\n"
"")





        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 250, 547))

        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        #===============================================================================
        self.pushButton_f = QPushButton(self.frame_10)
        self.pushButton_f.setObjectName(u"pushButton_12")
        self.pushButton_f.setText(QCoreApplication.translate("MainWindow", u"Facebook", None))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/facebook.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_f.setIcon(icon2)
        self.pushButton_f.setIconSize(QSize(24, 24))
        self.verticalLayout_8.addWidget(self.pushButton_f)
        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)
        #===============================================================================
        self.pushButton_y = QPushButton(self.frame_10)
        self.pushButton_y.setObjectName(u"pushButton_12")
        self.pushButton_y.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/youtube.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_y.setIcon(icon2)
        self.pushButton_y.setIconSize(QSize(24, 24))
        self.verticalLayout_8.addWidget(self.pushButton_y)
        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)
        #===============================================================================
        self.pushButton_i = QPushButton(self.frame_10)
        self.pushButton_i.setObjectName(u"pushButton_12")
        self.pushButton_i.setText(QCoreApplication.translate("MainWindow", u"Instagram", None))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/instagram.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_i.setIcon(icon2)
        self.pushButton_i.setIconSize(QSize(24, 24))
        self.verticalLayout_8.addWidget(self.pushButton_i)
        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)
        #===============================================================================
        self.pushButton_w = QPushButton(self.frame_10)
        self.pushButton_w.setObjectName(u"pushButton_12")
        self.pushButton_w.setText(QCoreApplication.translate("MainWindow", u"Whatsapp", None))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/message-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_w.setIcon(icon2)
        self.pushButton_w.setIconSize(QSize(24, 24))
        self.verticalLayout_8.addWidget(self.pushButton_w)
        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)
        #===============================================================================
        self.pushButton_d = QPushButton(self.frame_10)
        self.pushButton_d.setObjectName(u"pushButton_12")
        self.pushButton_d.setText(QCoreApplication.translate("MainWindow", u"Dribbble", None))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/dribbble.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_d.setIcon(icon2)
        self.pushButton_d.setIconSize(QSize(24, 24))
        self.verticalLayout_8.addWidget(self.pushButton_d)
        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)
        #===============================================================================
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon3, u"Social Media")









        self.map_page = QWidget()
        self.map_page.setObjectName(u"page")
        self.map_page.setGeometry(QRect(0, 0, 250, 547))

        self.verticalLayout_m7 = QVBoxLayout(self.map_page)
        self.verticalLayout_m7.setSpacing(0)
        self.verticalLayout_m7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_m7.setContentsMargins(0, 0, 0, 0)

        self.frame_m10 = QFrame(self.map_page)
        self.frame_m10.setObjectName(u"frame_10")
        self.frame_m10.setFrameShape(QFrame.StyledPanel)
        self.frame_m10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_m8 = QVBoxLayout(self.frame_m10)
        self.verticalLayout_m8.setSpacing(0)
        self.verticalLayout_m8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_m8.setContentsMargins(0, 0, 0, 0)
        #===============================================================================
        self.pushButton_m1 = QPushButton(self.frame_m10)
        self.pushButton_m1.setObjectName(u"pushButton_m1")
        iconm2 = QIcon()
        iconm2.addFile(u":/icons/icons/map-pin.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_m1.setIcon(iconm2)
        self.pushButton_m1.setIconSize(QSize(24, 24))
        self.pushButton_m1.setText(QCoreApplication.translate("MainWindow", u"Earth", None))
        self.verticalLayout_m8.addWidget(self.pushButton_m1)
        self.verticalLayout_m7.addWidget(self.frame_m10, 0, Qt.AlignTop)
        #===============================================================================
        self.pushButton_m2 = QPushButton(self.frame_m10)
        self.pushButton_m2.setObjectName(u"pushButton_m1")
        iconm2 = QIcon()
        iconm2.addFile(u":/icons/icons/map.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_m2.setIconSize(QSize(24, 24))
        self.pushButton_m2.setIcon(iconm2)
        self.pushButton_m2.setText(QCoreApplication.translate("MainWindow", u"Osm Map", None))
        self.verticalLayout_m8.addWidget(self.pushButton_m2)
        self.verticalLayout_m7.addWidget(self.frame_m10, 0, Qt.AlignTop)
        #===============================================================================
        self.pushButton_m3 = QPushButton(self.frame_m10)
        self.pushButton_m3.setObjectName(u"pushButton_m1")
        iconm2 = QIcon()
        iconm2.addFile(u":/icons/icons/navigation.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_m3.setIconSize(QSize(24, 24))
        self.pushButton_m3.setIcon(iconm2)
        self.pushButton_m3.setText(QCoreApplication.translate("MainWindow", u"Map Tracer", None))
        self.verticalLayout_m8.addWidget(self.pushButton_m3)
        self.verticalLayout_m7.addWidget(self.frame_m10, 0, Qt.AlignTop)
        #===============================================================================

        iconm3 = QIcon()
        iconm3.addFile(u":/icons/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.map_page, iconm3, u"Location Tools")











        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 250, 547))

        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)
        self.verticalLayout_9.addWidget(self.label_4, 0, Qt.AlignTop)
        icon33 = QIcon()
        icon33.addFile(u":/icons/icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon33, u"Users")

        self.verticalLayout_3.addWidget(self.toolBox, 0)


























        self.verticalLayout_2.addWidget(self.top_menu_container)
























        self.bottom_menu_container = QWidget(self.left_menu_main_container)
        self.bottom_menu_container.setObjectName(u"bottom_menu_container")
        self.verticalLayout_5 = QVBoxLayout(self.bottom_menu_container)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.bottom_menu_container)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.verticalLayout_6.addWidget(self.label)

        self.notifications_btn = QPushButton(self.widget_5)
        self.notifications_btn.setObjectName(u"notifications_btn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notifications_btn.setIcon(icon9)
        self.notifications_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.notifications_btn)

        self.connect_btns = QPushButton(self.widget_5)
        self.connect_btns.setObjectName(u"connect_btns")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_btns.setIcon(icon10)
        self.connect_btns.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.connect_btns)

        self.settings_btns = QPushButton(self.widget_5)
        self.settings_btns.setObjectName(u"settings_btns")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btns.setIcon(icon11)
        self.settings_btns.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.settings_btns)


        self.verticalLayout_5.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.bottom_menu_container)


        self.horizontalLayout.addWidget(self.left_menu_main_container, 0, Qt.AlignLeft)

#=========main body======================
        self.main_body = QWidget(self.widget_2)
        self.main_body.setObjectName(u"main_body")
        self.main_body.sizePolicy().setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)

        self.verticalLayout_7 = QVBoxLayout(self.main_body)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.stackedWidget = QtWidgets.QStackedWidget(self.main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")


        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setFamily(u"URW Gothic")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 589, 236))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.webEngineView = QWebEngineView(self.scrollAreaWidgetContents)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy2)
        self.webEngineView.setMinimumSize(QSize(0, 0))
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_14.addWidget(self.webEngineView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page)

# debut de la page 2:: projets

        self.page_2 = QWidget()#déclaration de la page
        self.page_2.setObjectName(u"page_2")#nom d'element de la page

        self.verticalLayout_9 = QVBoxLayout(self.page_2)#container de la page 2
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")#nom du container


        self.label_4 = QLabel(self.page_2)# premier widget ou élement de proget dans le container
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)# application des propriétés 
        self.label_4.setAlignment(Qt.AlignCenter)#alignement

        self.verticalLayout_9.addWidget(self.label_4) #ajoute à la page

        self.stackedWidget.addWidget(self.page_2)# finalisation et ajout de l'élement dans la box principale





        
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_10 = QVBoxLayout(self.page_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_11 = QVBoxLayout(self.page_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.page_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_6)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_12 = QVBoxLayout(self.page_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.page_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_13 = QVBoxLayout(self.page_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.page_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.stackedWidget.addWidget(self.page_6)


# debut de la page db:: projets

        self.page_db = QWidget()#déclaration de la page
        self.page_db.setObjectName(u"page_db")#nom d'element de la page

        self.verticalLayout_db = QVBoxLayout(self.page_db)#container de la page 2
        self.verticalLayout_db.setObjectName(u"verticalLayout_db")#nom du container


        self.label_db = QLabel(self.page_db)# premier widget ou élement de proget dans le container
        self.label_db.setObjectName(u"label_db")
        self.label_db.setAlignment(Qt.AlignCenter)#alignement
        self.label_db.setText("yo")

        self.verticalLayout_db.addWidget(self.label_db) #ajoute à la page

        self.stackedWidget.addWidget(self.page_db)# finalisation et ajout de l'élement dans la box principale


























        self.earth_page = QWidget()
        self.earth_page.setObjectName(u"page")
        self.verticalLayout_8_earth = QVBoxLayout(self.earth_page)
        self.verticalLayout_8_earth.setObjectName(u"verticalLayout_8")

        self.label_3_earth = QLabel(self.earth_page)
        self.label_3_earth.setObjectName(u"label_3")
        self.label_3_earth.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setFamily(u"URW Gothic")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3_earth.setFont(font2)
        self.label_3_earth.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8_earth.addWidget(self.label_3_earth)

        self.scrollArea_earth_ = QScrollArea(self.earth_page)
        self.scrollArea_earth_.setObjectName(u"scrollArea")
        self.scrollArea_earth_.setWidgetResizable(True)
        self.scrollArea_earth_WidgetContents = QWidget()
        self.scrollArea_earth_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollArea_earth_WidgetContents.setGeometry(QRect(0, 0, 589, 236))
        self.verticalLayout_14_earth = QVBoxLayout(self.scrollArea_earth_WidgetContents)
        self.verticalLayout_14_earth.setObjectName(u"verticalLayout_14")
        self.webEngineView_earth = QWebEngineView(self.scrollArea_earth_WidgetContents)
        self.webEngineView_earth.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_earth.sizePolicy().hasHeightForWidth())
        self.webEngineView_earth.setSizePolicy(sizePolicy2)
        self.webEngineView_earth.setMinimumSize(QSize(0, 0))
        self.webEngineView_earth.setUrl(QUrl(u"http://localhost/genesis/discutions/index.php"))

        self.verticalLayout_14_earth.addWidget(self.webEngineView_earth)

        self.scrollArea_earth_.setWidget(self.scrollArea_earth_WidgetContents)

        self.verticalLayout_8_earth.addWidget(self.scrollArea_earth_)

        self.stackedWidget.addWidget(self.earth_page)

        navigationButtons(self.stackedWidget,self.pushButton_m1,self.earth_page)










        self.osm_page = QWidget()
        self.osm_page.setObjectName(u"page")
        self.verticalLayout_8_osm = QVBoxLayout(self.osm_page)
        self.verticalLayout_8_osm.setObjectName(u"verticalLayout_8")

        self.label_3_osm = QLabel(self.osm_page)
        self.label_3_osm.setObjectName(u"label_3")
        self.label_3_osm.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setFamily(u"URW Gothic")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3_osm.setFont(font2)
        self.label_3_osm.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8_osm.addWidget(self.label_3_osm)

        self.scrollArea_osm_ = QScrollArea(self.osm_page)
        self.scrollArea_osm_.setObjectName(u"scrollArea")
        self.scrollArea_osm_.setWidgetResizable(True)
        self.scrollArea_osm_WidgetContents = QWidget()
        self.scrollArea_osm_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollArea_osm_WidgetContents.setGeometry(QRect(0, 0, 589, 236))
        self.verticalLayout_14_osm = QVBoxLayout(self.scrollArea_osm_WidgetContents)
        self.verticalLayout_14_osm.setObjectName(u"verticalLayout_14")
        self.webEngineView_osm = QWebEngineView(self.scrollArea_osm_WidgetContents)
        self.webEngineView_osm.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_osm.sizePolicy().hasHeightForWidth())
        self.webEngineView_osm.setSizePolicy(sizePolicy2)
        self.webEngineView_osm.setMinimumSize(QSize(0, 0))
        self.webEngineView_osm.setUrl(QUrl(u"https://www.openstreetmap.org/"))

        self.verticalLayout_14_osm.addWidget(self.webEngineView_osm)

        self.scrollArea_osm_.setWidget(self.scrollArea_osm_WidgetContents)

        self.verticalLayout_8_osm.addWidget(self.scrollArea_osm_)

        self.stackedWidget.addWidget(self.osm_page)

        navigationButtons(self.stackedWidget,self.pushButton_m2,self.osm_page)













        self.mt_page = QWidget()
        self.mt_page.setObjectName(u"page")
        self.verticalLayout_8_mt = QVBoxLayout(self.mt_page)
        self.verticalLayout_8_mt.setObjectName(u"verticalLayout_8")

        self.label_3_mt = QLabel(self.mt_page)
        self.label_3_mt.setObjectName(u"label_3")
        self.label_3_mt.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setFamily(u"URW Gothic")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3_mt.setFont(font2)
        self.label_3_mt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8_mt.addWidget(self.label_3_mt)

        self.scrollArea_mt_ = QScrollArea(self.mt_page)
        self.scrollArea_mt_.setObjectName(u"scrollArea")
        self.scrollArea_mt_.setWidgetResizable(True)
        self.scrollArea_mt_WidgetContents = QWidget()
        self.scrollArea_mt_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollArea_mt_WidgetContents.setGeometry(QRect(0, 0, 589, 236))
        self.verticalLayout_14_mt = QVBoxLayout(self.scrollArea_mt_WidgetContents)
        self.verticalLayout_14_mt.setObjectName(u"verticalLayout_14")
        self.webEngineView_mt = QWebEngineView(self.scrollArea_mt_WidgetContents)
        self.webEngineView_mt.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_mt.sizePolicy().hasHeightForWidth())
        self.webEngineView_mt.setSizePolicy(sizePolicy2)
        self.webEngineView_mt.setMinimumSize(QSize(0, 0))

        self.verticalLayout_14_mt.addWidget(self.webEngineView_mt)

        self.scrollArea_mt_.setWidget(self.scrollArea_mt_WidgetContents)

        self.verticalLayout_8_mt.addWidget(self.scrollArea_mt_)

        self.stackedWidget.addWidget(self.mt_page)

        navigationButtons(self.stackedWidget,self.pushButton_m3,self.mt_page)














        self.f_page = QWidget()
        self.f_page.setObjectName(u"page")
        self.verticalLayout_8_f = QVBoxLayout(self.f_page)
        self.verticalLayout_8_f.setObjectName(u"verticalLayout_8")

        self.label_3_f = QLabel(self.f_page)
        self.label_3_f.setObjectName(u"label_3")
        self.label_3_f.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setFamily(u"URW Gothic")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3_f.setFont(font2)
        self.label_3_f.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8_f.addWidget(self.label_3_f)

        self.scrollArea_f_ = QScrollArea(self.f_page)
        self.scrollArea_f_.setObjectName(u"scrollArea")
        self.scrollArea_f_.setWidgetResizable(True)
        self.scrollArea_f_WidgetContents = QWidget()
        self.scrollArea_f_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollArea_f_WidgetContents.setGeometry(QRect(0, 0, 589, 236))
        self.verticalLayout_14_f = QVBoxLayout(self.scrollArea_f_WidgetContents)
        self.verticalLayout_14_f.setObjectName(u"verticalLayout_14")
        self.webEngineView_f = QWebEngineView(self.scrollArea_f_WidgetContents)
        self.webEngineView_f.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_f.sizePolicy().hasHeightForWidth())
        self.webEngineView_f.setSizePolicy(sizePolicy2)
        self.webEngineView_f.setMinimumSize(QSize(0, 0))
        self.webEngineView_f.setUrl(QUrl(u"https://facebook.com"))

        self.verticalLayout_14_f.addWidget(self.webEngineView_f)

        self.scrollArea_f_.setWidget(self.scrollArea_f_WidgetContents)

        self.verticalLayout_8_f.addWidget(self.scrollArea_f_)

        self.stackedWidget.addWidget(self.f_page)

        navigationButtons(self.stackedWidget,self.pushButton_f,self.f_page)














        self.y_page = QWidget()
        self.y_page.setObjectName(u"page")
        self.verticalLayout_8_y = QVBoxLayout(self.y_page)
        self.verticalLayout_8_y.setObjectName(u"verticalLayout_8")




        self.cpu_frame = QFrame(self.y_page)
        self.cpu_frame.setObjectName(u"cpu_frame")
        self.cpu_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_frame.setFrameShadow(QFrame.Raised)

        self.hlayout_5 = QHBoxLayout(self.cpu_frame)
        self.hlayout_5.setObjectName(u"hlayout_5")

        self.lineEdit2 = QLineEdit(self.frame)
        self.lineEdit2.setObjectName(u"lineEdit")
        self.hlayout_5.addWidget(self.lineEdit2,0,Qt.AlignLeft)
        self.lineEdit2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set url and Download..", None))
        self.lineEdit2.setStyleSheet("border: 1px solid rgb(7 ,98 ,160);width: 160%;padding: 10px;border-radius:15px;")
        

        self.pushButton_down = QPushButton(self.cpu_frame)
        self.pushButton_down.setObjectName(u"pushButton_12")
        self.pushButton_down.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.pushButton_down.setStyleSheet("background-color: white;color: rgb(7 ,98 ,160);border: 1px solid rgb(7 ,98 ,160);width: 20%;padding: 10px;border-radius:15px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_down.setIcon(icon2)
        self.pushButton_down.setIconSize(QSize(30, 30))
        self.hlayout_5.addWidget(self.pushButton_down)







        self.verticalLayout_8_y.addWidget(self.cpu_frame)

        self.scrollArea_y_ = QScrollArea(self.y_page)
        self.scrollArea_y_.setObjectName(u"scrollArea")
        self.scrollArea_y_.setWidgetResizable(True)
        self.scrollArea_y_WidgetContents = QWidget()
        self.scrollArea_y_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollArea_y_WidgetContents.setGeometry(QRect(0, 0, 589, 236))
        self.verticalLayout_14_y = QVBoxLayout(self.scrollArea_y_WidgetContents)
        self.verticalLayout_14_y.setObjectName(u"verticalLayout_14")
        self.webEngineView_y = QWebEngineView(self.scrollArea_y_WidgetContents)
        self.webEngineView_y.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_y.sizePolicy().hasHeightForWidth())
        self.webEngineView_y.setSizePolicy(sizePolicy2)
        self.webEngineView_y.setMinimumSize(QSize(0, 0))
        self.webEngineView_y.setUrl(QUrl(u"https://youtube.com"))

        self.verticalLayout_14_y.addWidget(self.webEngineView_y)

        self.scrollArea_y_.setWidget(self.scrollArea_y_WidgetContents)

        self.verticalLayout_8_y.addWidget(self.scrollArea_y_)

        self.stackedWidget.addWidget(self.y_page)

        navigationButtons(self.stackedWidget,self.pushButton_y,self.y_page)














        self.i_page = QWidget()
        self.i_page.setObjectName(u"page")
        self.verticalLayout_8_i = QVBoxLayout(self.i_page)
        self.verticalLayout_8_i.setObjectName(u"verticalLayout_8")

        self.label_3_i = QLabel(self.i_page)
        self.label_3_i.setObjectName(u"label_3")
        self.label_3_i.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setFamily(u"URW Gothic")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3_i.setFont(font2)
        self.label_3_i.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8_i.addWidget(self.label_3_i)

        self.scrollArea_i_ = QScrollArea(self.i_page)
        self.scrollArea_i_.setObjectName(u"scrollArea")
        self.scrollArea_i_.setWidgetResizable(True)
        self.scrollArea_i_WidgetContents = QWidget()
        self.scrollArea_i_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollArea_i_WidgetContents.setGeometry(QRect(0, 0, 589, 236))
        self.verticalLayout_14_i = QVBoxLayout(self.scrollArea_i_WidgetContents)
        self.verticalLayout_14_i.setObjectName(u"verticalLayout_14")
        self.webEngineView_i = QWebEngineView(self.scrollArea_i_WidgetContents)
        self.webEngineView_i.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_i.sizePolicy().hasHeightForWidth())
        self.webEngineView_i.setSizePolicy(sizePolicy2)
        self.webEngineView_i.setMinimumSize(QSize(0, 0))
        self.webEngineView_i.setUrl(QUrl(u"https://instagram.com"))

        self.verticalLayout_14_i.addWidget(self.webEngineView_i)

        self.scrollArea_i_.setWidget(self.scrollArea_i_WidgetContents)

        self.verticalLayout_8_i.addWidget(self.scrollArea_i_)

        self.stackedWidget.addWidget(self.i_page)

        navigationButtons(self.stackedWidget,self.pushButton_i,self.i_page)














        self.w_page = QWidget()
        self.w_page.setObjectName(u"page")
        self.verticalLayout_8_w = QVBoxLayout(self.w_page)
        self.verticalLayout_8_w.setObjectName(u"verticalLayout_8")

        self.label_3_w = QLabel(self.w_page)
        self.label_3_w.setObjectName(u"label_3")
        self.label_3_w.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setFamily(u"URW Gothic")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3_w.setFont(font2)
        self.label_3_w.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8_w.addWidget(self.label_3_w)

        self.scrollArea_w_ = QScrollArea(self.w_page)
        self.scrollArea_w_.setObjectName(u"scrollArea")
        self.scrollArea_w_.setWidgetResizable(True)
        self.scrollArea_w_WidgetContents = QWidget()
        self.scrollArea_w_WidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollArea_w_WidgetContents.setGeometry(QRect(0, 0, 589, 236))
        self.verticalLayout_14_w = QVBoxLayout(self.scrollArea_w_WidgetContents)
        self.verticalLayout_14_w.setObjectName(u"verticalLayout_14")
        self.webEngineView_w = QWebEngineView(self.scrollArea_w_WidgetContents)
        self.webEngineView_w.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineView_w.sizePolicy().hasHeightForWidth())
        self.webEngineView_w.setSizePolicy(sizePolicy2)
        self.webEngineView_w.setMinimumSize(QSize(0, 0))
        self.webEngineView_w.setUrl(QUrl(u"https://web.whatsapp.com"))

        self.verticalLayout_14_w.addWidget(self.webEngineView_w)

        self.scrollArea_w_.setWidget(self.scrollArea_w_WidgetContents)

        self.verticalLayout_8_w.addWidget(self.scrollArea_w_)

        self.stackedWidget.addWidget(self.w_page)

        navigationButtons(self.stackedWidget,self.pushButton_w,self.w_page)














        self.d_page = QWidget()
        self.d_page.setObjectName(u"page")
        self.verticalLayout_8_d = QVBoxLayout(self.d_page)
        self.verticalLayout_8_d.setObjectName(u"verticalLayout_8")

        self.label_3_d = QLabel(self.d_page)
        self.label_3_d.setObjectName(u"label_3")
        self.label_3_d.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setFamily(u"URW Gothic")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3_d.setFont(font2)
        self.label_3_d.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8_d.addWidget(self.label_3_d)

        self.scrollArea_d_ = QScrollArea(self.d_page)
        self.scrollArea_d_.setObjectName(u"scrollArea")
        self.scrollArea_d_.setWidgetResizable(True)
        self.scrollArea_d_didgetContents = QWidget()
        self.scrollArea_d_didgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollArea_d_didgetContents.setGeometry(QRect(0, 0, 589, 236))
        self.verticalLayout_14_d = QVBoxLayout(self.scrollArea_d_didgetContents)
        self.verticalLayout_14_d.setObjectName(u"verticalLayout_14")
        self.webEngineVied_d = QWebEngineView(self.scrollArea_d_didgetContents)
        self.webEngineVied_d.setObjectName(u"webEngineView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.webEngineVied_d.sizePolicy().hasHeightForWidth())
        self.webEngineVied_d.setSizePolicy(sizePolicy2)
        self.webEngineVied_d.setMinimumSize(QSize(0, 0))
        self.webEngineVied_d.setUrl(QUrl(u"https://dribbble.com"))

        self.verticalLayout_14_d.addWidget(self.webEngineVied_d)

        self.scrollArea_d_.setWidget(self.scrollArea_d_didgetContents)

        self.verticalLayout_8_d.addWidget(self.scrollArea_d_)

        self.stackedWidget.addWidget(self.d_page)

        navigationButtons(self.stackedWidget,self.pushButton_d,self.d_page)




















        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.widget_2)




        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")

        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.frame_2 = QFrame(self.widget_7)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.size_grip = QFrame(self.widget_7)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(20, 20))
        self.size_grip.setMaximumSize(QSize(20, 20))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.size_grip)


        self.verticalLayout.addWidget(self.widget_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_button.setText(QCoreApplication.translate("MainWindow", u"PROJECT MANAGER", None))
        self.pushButton_8.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_12.setText("")
        self.restoreWindow.setText("")
        self.minimizeWindow.setText("")
        self.closeWindow.setText("")
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.projects_btn.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
        self.reports_btn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.db_btn.setText(QCoreApplication.translate("MainWindow", u"DataBase", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.notifications_btn.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.connect_btns.setText(QCoreApplication.translate("MainWindow", u"Connect Apps", None))
        self.settings_btns.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>DASHBOARD</p><p><span style=\" font-size:8pt; font-weight:600;\">Projects Location</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"VOS PROJECTS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"REPORTS", None))
        self.label_db.setText(QCoreApplication.translate("MainWindow", u"DataBase", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"NOTIFICATIONS", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CONNECT APPS", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Creative UI Inc.", None))
    # retranslateUi

