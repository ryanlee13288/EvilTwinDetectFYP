# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1279, 825)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setContextMenuPolicy(Qt.ActionsContextMenu)
        MainWindow.setStyleSheet(u"background-image: url(:/img/background.jpg);\n"
"background-repeat: no-repeat\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color:none;")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 1, 1, 10)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 10, 1, 1)

        self.home_btn = QPushButton(self.centralwidget)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(211, 71))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.home_btn.setFont(font)
        self.home_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn.setStyleSheet(u"color:white;\n"
"font-weight:600;\n"
"font-size:12pt;")

        self.gridLayout.addWidget(self.home_btn, 1, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.contact_btn = QPushButton(self.centralwidget)
        self.contact_btn.setObjectName(u"contact_btn")
        self.contact_btn.setMinimumSize(QSize(211, 71))
        self.contact_btn.setFont(font)
        self.contact_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.contact_btn.setStyleSheet(u"color:white;\n"
"font-weight:600;\n"
"font-size:12pt;")

        self.gridLayout.addWidget(self.contact_btn, 1, 5, 1, 1, Qt.AlignLeft)

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMinimumSize(QSize(0, 0))
        self.logo.setMaximumSize(QSize(120, 120))
        self.logo.setCursor(QCursor(Qt.ArrowCursor))
        self.logo.setStyleSheet(u"margin-top:8px")
        self.logo.setTextFormat(Qt.AutoText)
        self.logo.setPixmap(QPixmap(u"img/logo.jpg"))
        self.logo.setScaledContents(True)

        self.gridLayout.addWidget(self.logo, 1, 9, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setMinimumSize(QSize(721, 591))
        self.stackedWidget.setMouseTracking(True)
        self.stackedWidget.setTabletTracking(False)
        self.stackedWidget.setFocusPolicy(Qt.NoFocus)
        self.stackedWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background:None;background-color: transparent\n"
"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.horizontalLayout = QHBoxLayout(self.home_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_8 = QSpacerItem(35, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.textEdit = QTextEdit(self.home_page)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(721, 591))
        self.textEdit.setStyleSheet(u"background:None;\n"
"background-color:rgb(255, 240, 208);\n"
"color:black")
        self.textEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEdit)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.detectpg_btn = QPushButton(self.home_page)
        self.detectpg_btn.setObjectName(u"detectpg_btn")
        self.detectpg_btn.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.detectpg_btn.sizePolicy().hasHeightForWidth())
        self.detectpg_btn.setSizePolicy(sizePolicy3)
        self.detectpg_btn.setMinimumSize(QSize(271, 591))
        font1 = QFont()
        font1.setPointSize(26)
        self.detectpg_btn.setFont(font1)
        self.detectpg_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.detectpg_btn.setMouseTracking(True)
        self.detectpg_btn.setAcceptDrops(False)
        self.detectpg_btn.setStyleSheet(u"QPushButton {\n"
"    color: red;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35,stop: 0 #2c02ff, stop: 1 #13fff0\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35,stop: 0 #0000b5, stop: 1 #55ffff\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #2c02ff, stop: 1 #13fff0\n"
"        );\n"
"    }\n"
"")
        self.detectpg_btn.setCheckable(False)

        self.horizontalLayout.addWidget(self.detectpg_btn)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.stackedWidget.addWidget(self.home_page)
        self.detected_Page = QWidget()
        self.detected_Page.setObjectName(u"detected_Page")
        self.verticalLayout_3 = QVBoxLayout(self.detected_Page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.label_2 = QLabel(self.detected_Page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: transparent;\n"
"background:None;")

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.detected_Page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background:None;background-color: transparent")

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.detectButton = QPushButton(self.detected_Page)
        self.detectButton.setObjectName(u"detectButton")
        self.detectButton.setEnabled(True)
        self.detectButton.setMinimumSize(QSize(391, 131))
        self.detectButton.setMaximumSize(QSize(391, 16777215))
        self.detectButton.setFont(font1)
        self.detectButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.detectButton.setMouseTracking(True)
        self.detectButton.setAcceptDrops(False)
        self.detectButton.setStyleSheet(u"QPushButton {\n"
"    color: red;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"")
        self.detectButton.setCheckable(False)

        self.verticalLayout_3.addWidget(self.detectButton, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.detected_Page)
        self.contact_page = QWidget()
        self.contact_page.setObjectName(u"contact_page")
        self.gridLayout_2 = QGridLayout(self.contact_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 0, 2, 1, 1)

        self.sendEmail = QPushButton(self.contact_page)
        self.sendEmail.setObjectName(u"sendEmail")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sendEmail.sizePolicy().hasHeightForWidth())
        self.sendEmail.setSizePolicy(sizePolicy4)
        self.sendEmail.setMinimumSize(QSize(0, 50))
        self.sendEmail.setMaximumSize(QSize(1000, 16777215))
        self.sendEmail.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendEmail.setStyleSheet(u"background:None")

        self.gridLayout_2.addWidget(self.sendEmail, 3, 2, 1, 1)

        self.label_4 = QLabel(self.contact_page)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        self.label_4.setStyleSheet(u"background:None;\n"
"color:White")

        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)

        self.label = QLabel(self.contact_page)
        self.label.setObjectName(u"label")
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"background:None;\n"
"color:White")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)

        self.textEdit_2 = QTextEdit(self.contact_page)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy3.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy3)
        self.textEdit_2.setMinimumSize(QSize(1000, 450))
        self.textEdit_2.setMaximumSize(QSize(1000, 16777215))
        self.textEdit_2.setLayoutDirection(Qt.LeftToRight)
        self.textEdit_2.setStyleSheet(u"background:None")
        self.textEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.gridLayout_2.addWidget(self.textEdit_2, 2, 2, 1, 1)

        self.lineEdit = QLineEdit(self.contact_page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(1000, 16777215))
        self.lineEdit.setStyleSheet(u"background:None")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 4, 2, 1, 1)

        self.stackedWidget.addWidget(self.contact_page)

        self.gridLayout.addWidget(self.stackedWidget, 5, 1, 1, 10)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.contact_btn.setText(QCoreApplication.translate("MainWindow", u"Contact Us", None))
        self.logo.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Phshing Attack</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Phishing is a type of social engineering attack often used to steal user data, i"
                        "ncluding login credentials and credit card numbers. It occurs when an attacker, masquerading as a trusted entity, dupes a victim into opening an email, instant message, or text message. The recipient is then tricked into clicking a malicious link, which can lead to the installation of malware, the freezing of the system as part of a ransomware attack or the revealing of sensitive information.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">An attack can have devastating results. For individuals, this includes unauthorized purchases, the stealing of funds, or identify theft. Moreover, phishing is often used to gain a foothold in corporate or governmental networks as a part of a larger attack, such as an advanced persistent threat (APT) event. In this latter scenario, employees are compromised in order to bypass security perimeters, distribute malware inside a closed enviro"
                        "nment, or gain privileged access to secured data.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">An organization succumbing to such an attack typically sustains severe financial losses in addition to declining market share, reputation, and consumer trust. Depending on scope, a phishing attempt might escalate into a security incident from which a business will have a difficult time recovering.<br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ff0000;\">**The below following link is used to detect whether there is an attack on the link:</span><span style=\" font-size:9pt;\"><br /></span><a href=\"https://yiyang2001-ultrasec-phishing-detection-app-8e0oz3.streamlit.app/\"><span style=\" font-size:8pt; text-dec"
                        "oration: underline; color:#0000ff;\">https://yiyang2001-ultrasec-phishing-detection-app-8e0oz3.streamlit.app/</span></a><span style=\" font-size:9pt;\"><br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Welcome To Evil Twin attack Detection</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">What Is Evil Twin Detection?</span><span style=\" font-size:9pt;\"><br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "img src=\":/img/evilTwinAtk.png\" width=\"667\" height=\"480\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">An evil twin attack takes place when an attacker sets up a fake Wi-Fi access point hoping that users will connect to it instead of a legitimate one. When users connect to this access point, all the data they share with the network passes through a server controlled by the attacker. An attacker can create an evil twin with a smartphone or other internet-capable device and some readily available software. Evil twin attacks are more common on public Wi-Fi networks which are unsecured and leave your personal data vulnerable.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">What this application do?</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This application is to use some specific algorithme to detect the potential dangerouse of the duplication SSID(WiFi Name) is it an evil twin attack or not. After we successfully detected, it will aleart the user is they are under evil twin attack or not.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"><br /></span></p></body></html>", None))
        self.detectpg_btn.setText(QCoreApplication.translate("MainWindow", u"Click me \n"
"Get Started", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Algerian'; font-size:48pt; font-style:italic; color:#00ffff;\">Evil Twin Detection</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#ff0000;\">**Requirement**</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00ffff;\">Need support monitor mode WiFi adaptor</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00ffff;\">Currently only supported by Linux Version"
                        "</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00ffff;\">This process takes time to process, please be patient</span></p></body></html>", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Start Detect", None))
        self.sendEmail.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Messenge</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Recipient</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"leejy_wm19@student.tar.edu.my", None))
    # retranslateUi

