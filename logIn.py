from PyQt4 import QtCore, QtGui
from res import messages
from res import messageWin
import pymysql
from res.vars import host, port, user, passwd, db
import res.vars
import mainWindow
import selectClass

try:
    conn = pymysql.connect(host = host, port = port, user = user, passwd = passwd, db = db)
    cur = conn.cursor()
except Exception as e:
    messageWin.pop_up_window(messages.SQLErrorTitle, messages.SQLError)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(625, 900)
        Dialog.setMinimumSize(QtCore.QSize(625, 900))
        Dialog.setMaximumSize(QtCore.QSize(625, 900))
        font = QtGui.QFont()
        font.setPointSize(9)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("#Dialog{\n"
"    background-image:url(:/drawable/background.jpg);\n"
"    background-repeat:none;\n"
"}\n"
"\n"
"\n"
""))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.userName = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.userName.setFont(font)
        self.userName.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"color: white;\n"
"background-image:url(:/drawable/user.png); \n"
"background-repeat: no-repeat;\n"
"padding: 10px 5px 5px 40px;\n"
"border:none;\n"
"border-bottom: 2px solid rgb(255, 255, 255);"))
        self.userName.setObjectName(_fromUtf8("userName"))
        self.gridLayout.addWidget(self.userName, 3, 1, 1, 1)
        self.password = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.password.setFont(font)
        self.password.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"color: white;\n"
"background-image: url(:/drawable/password.png); \n"
"background-repeat: no-repeat;\n"
"padding: 10px 5px 5px 40px;\n"
"border: none;\n"
"border-bottom: 2px solid white;"))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.horizontalLayout_2.addWidget(self.password)
        self.showPassword = QtGui.QPushButton(Dialog)
        self.showPassword.setMaximumSize(QtCore.QSize(40, 30))
        self.showPassword.setStyleSheet(_fromUtf8("#showPassword{\n"
"    background-color:transparent;\n"
"    background-image:url(:/drawable/showpass.png);\n"
"    background-repeat:none;\n"
"}\n"
"#showPassword:pressed{\n"
"    background-image:url(:/drawable/hidepass.png)\n"
"}"))
        self.showPassword.setText(_fromUtf8(""))
        self.showPassword.setFlat(True)
        self.showPassword.setObjectName(_fromUtf8("showPassword"))
        self.horizontalLayout_2.addWidget(self.showPassword)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:gray;"))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.signUp = QtGui.QLabel(Dialog)
        self.signUp.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.signUp.setFont(font)
        self.signUp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signUp.setStyleSheet(_fromUtf8("color:rgb(54,169,225);"))
        self.signUp.setObjectName(_fromUtf8("signUp"))
        self.gridLayout_3.addWidget(self.signUp, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color:gray;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 4, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 9, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.login = QtGui.QPushButton(Dialog)
        self.login.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.login.setFont(font)
        self.login.setStyleSheet(_fromUtf8("#login{\n"
"    background-color:rgb(29,113,184);\n"
"    background-repeat:none;\n"
"    border-radius:25px;\n"
"    color: white;\n"
"    padding: 15px 32px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"} \n"
"#login:hover{\n"
"    background-color:royalBlue;\n"
"    color:white;\n"
"}\n"
"#login:pressed{\n"
"    background-color:rgb(0, 99, 153);\n"
"    color:white;\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/drawable/login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login.setIcon(icon1)
        self.login.setObjectName(_fromUtf8("login"))
        self.horizontalLayout_4.addWidget(self.login)
        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.gridLayout.addItem(spacerItem4, 4, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 6, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 10, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 8, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.label = QtGui.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/drawable/logo.png")))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.showPassword.pressed.connect(self.on_pressed)
        self.showPassword.released.connect(self.on_released)
        
        self.login.clicked.connect(self.Login)

        self.MainWindow = QtGui.QMainWindow()
        self.Dialog = QtGui.QDialog()
        
    def on_pressed(self):
        self.password.setEchoMode(QtGui.QLineEdit.Normal)

    def on_released(self):
        self.password.setEchoMode(QtGui.QLineEdit.Password)

    def Login(self):
        username = self.userName.text()
        password = self.password.text()
        if username == "" or password == "":
            messageWin.pop_up_window(messages.errorTitle, messages.emptyFieldError)
        else:
            if username == res.vars.adminID and password == res.vars.adminPass:
                self.ui = mainWindow.Ui_MainWindow()
                self.ui.setupUi(self.MainWindow)
                self.MainWindow.show()

            else:
                query = "SELECT CLASSES, COORDINATED_CLASSES FROM TEACHERS WHERE ID='{0}' AND PASSWORD='{1}'".format(username, password)
                cur.execute(query)
                data = cur.fetchone()
                if data is None:
                    messageWin.pop_up_window(messages.SQLErrorTitle, messages.noUserFound)
                else:
                    classes = data[0].split(',')
                    coordClasses = data[1].split(',')
                    count = 0
                    
                    branch = []
                    year = []
                    section = []
                    b = y = s = ""
                    for doc in classes:
                        b = y = s = ""
                        doc = doc.strip()
                        count = 0
                        for i in range(len(doc)):
                            if doc[i] == '-':
                                count += 1
                            elif count == 0:
                                b += doc[i]
                            elif count == 1:
                                y += doc[i]
                            elif count == 2:
                                s += doc[i]
                        branch.append(b)
                        year.append(y)
                        section.append(s)

                    self.ui = selectClass.Ui_Dialog(self.removeDuplicate(branch), self.removeDuplicate(year), self.removeDuplicate(section))
                    self.ui.setupUi(self.Dialog)
                    self.Dialog.show()

    def removeDuplicate(self, nameList):
        final_list = []
        for name in nameList:
            if name not in final_list:
                final_list.append(name)

        return final_list
            
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Login", None))
        self.password.setPlaceholderText(_translate("Dialog", "Password", None))
        self.label_2.setText(_translate("Dialog", "Don\'t have an account?", None))
        self.signUp.setText(_translate("Dialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">Signup</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "Here.", None))
        self.login.setText(_translate("Dialog", "Login", None))
        self.userName.setPlaceholderText(_translate("Dialog", "Username", None))

import res.resources_re

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

#509295857977-g8m0003on1v1f7ovq80gmvj8kilguboj.apps.googleusercontent.com
#6k3PNls9Fa4eKLoQtZu4ug5N
