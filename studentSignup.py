from PyQt4 import QtCore, QtGui
import pymysql
from res import messages
from res import messageWin
from res.vars import host, port, user, passwd, db
import detection

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
        Dialog.resize(616, 802)
        Dialog.setStyleSheet(_fromUtf8("#Dialog{\n"
"    background-image:url(:/drawable/background.jpg)\n"
"}"))
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(68)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.phone = QtGui.QLineEdit(Dialog)
        self.phone.setStyleSheet(_fromUtf8("#phone{\n"
"    background-color:transparent;\n"
"    border:none;\n"
"    border-bottom:2px solid white;\n"
"    color:white;\n"
"}"))
        self.phone.setObjectName(_fromUtf8("phone"))
        self.gridLayout_2.addWidget(self.phone, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.name = QtGui.QLineEdit(Dialog)
        self.name.setStyleSheet(_fromUtf8("#name{\n"
"    background-color:transparent;\n"
"    border:none;\n"
"    border-bottom:2px solid white;\n"
"    color:white;\n"
"}"))
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout_2.addWidget(self.name, 0, 1, 1, 1)
        self.enumber = QtGui.QLineEdit(Dialog)
        self.enumber.setStyleSheet(_fromUtf8("#enumber{\n"
"    background-color:transparent;\n"
"    border:none;\n"
"    border-bottom:2px solid white;\n"
"    color:white;\n"
"}"))
        self.enumber.setObjectName(_fromUtf8("enumber"))
        self.gridLayout_2.addWidget(self.enumber, 1, 1, 1, 1)
        self.email = QtGui.QLineEdit(Dialog)
        self.email.setStyleSheet(_fromUtf8("#email{\n"
"    background-color:transparent;\n"
"    border:none;\n"
"    border-bottom:2px solid white;\n"
"    color:white;\n"
"}"))
        self.email.setObjectName(_fromUtf8("email"))
        self.gridLayout_2.addWidget(self.email, 2, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:white;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.branch = QtGui.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.branch.setFont(font)
        self.branch.setObjectName(_fromUtf8("branch"))
        self.horizontalLayout.addWidget(self.branch)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:white;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.year = QtGui.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.year.setFont(font)
        self.year.setObjectName(_fromUtf8("year"))
        self.horizontalLayout_3.addWidget(self.year)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:white;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.section = QtGui.QComboBox(Dialog)
        self.section.setObjectName(_fromUtf8("section"))
        self.horizontalLayout_5.addWidget(self.section)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 6, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.submit = QtGui.QPushButton(Dialog)
        self.submit.setStyleSheet(_fromUtf8("#submit{\n"
"    background-color:rgb(29,113,184);\n"
"    background-repeat:none;\n"
"    border-radius:20px;\n"
"    color: white;\n"
"    padding: 15px 32px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 16px;\n"
"} \n"
"#submit:hover{\n"
"    background-color:royalBlue;\n"
"    color:white;\n"
"}\n"
"#submit:pressed{\n"
"    background-color:rgb(0, 99, 153);\n"
"    color:white;\n"
"}"))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.gridLayout_3.addWidget(self.submit, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        query = "SELECT NAME FROM DEPARTMENT"
        cur.execute(query)
        docs = cur.fetchall()
        for d in docs:
            self.branch.addItem(d[0])
        self.branch.currentIndexChanged.connect(self.change)

        self.submit.clicked.connect(self.Submit)

    def change(self):
        self.year.clear()
        self.section.clear()
        text = self.branch.currentText()
        query = "SELECT YEAR,SECTION FROM DEPARTMENT WHERE NAME='{}'".format(text)
        cur.execute(query)
        docs = cur.fetchone()
        for i in range(int(docs[0])):
            self.year.addItem(str(i+1))

        for i in range(int(docs[1])):
            self.section.addItem(str(i+1))

    def Submit(self):
        name = self.name.text()
        enrollment_no = self.enumber.text()
        email = self.email.text()
        phone = self.phone.text()
        branch = self.branch.currentText()
        year = self.year.currentText()
        section = self.section.currentText()

        if name == "" or enrollment_no == "" or email == "" or phone == "":
            messageWin.pop_up_window(messages.errorTitle, messages.emptyFieldError)
        else:
            try:
                conn = pymysql.connect(host = host, port = port, user = user, passwd = passwd, db = db)
                cur = conn.cursor()
            except Exception as e:
                messageWin.pop_up_window(messages.SQLErrorTitle, messages.SQLError)

            table_name = str(branch+year+section)
            print(table_name)
            try:
                query = "CREATE TABLE IF NOT EXISTS "+table_name+"(SNO INT(3) NOT NULL AUTO_INCREMENT, NAME VARCHAR(30), ENROLLMENT VARCHAR(20), EMAIL VARCHAR(40), PHONE VARCHAR(20), BRANCH VARCHAR(10), YEAR VARCHAR(2), SECTION VARCHAR(3), UNIQUE(ENROLLMENT), PRIMARY KEY(SNO))"
                cur.execute(query)
            except Exception as e:
                print("error2")
            try:
                cur.execute("INSERT INTO "+table_name+"(NAME, ENROLLMENT, EMAIL, PHONE, BRANCH, YEAR, SECTION) VALUES(%s,%s,%s,%s,%s,%s,%s)",(str(name), str(enrollment_no), str(email), str(phone), str(branch), str(year), str(section)))
                conn.commit()
                try:
                    detection.start_detection(name, year, section, enrollment_no, branch)
                    messageWin.pop_up_window(messages.successTitle, messages.successMessage)
                except Exception as e:
                    messageWin.pop_up_window(messages.errorTitle, messages.errorMessage)
            except Exception as e:
                messageWin.pop_up_window(messages.SQLErrorTitle, messages.SQLInsertError)
            conn.close()    

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.phone.setPlaceholderText(_translate("Dialog", "Phone", None))
        self.name.setPlaceholderText(_translate("Dialog", "Full name", None))
        self.enumber.setPlaceholderText(_translate("Dialog", "Enrollment Number, last 3 digits", None))
        self.email.setPlaceholderText(_translate("Dialog", "Email", None))
        self.label.setText(_translate("Dialog", "Branch:", None))
        self.label_2.setText(_translate("Dialog", "Year:", None))
        self.label_3.setText(_translate("Dialog", "Section:", None))
        self.submit.setText(_translate("Dialog", "Submit", None))

import res.resources_re

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

