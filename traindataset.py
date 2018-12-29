from PyQt4 import QtCore, QtGui
import pymysql
from res.vars import host, port, user, passwd, db
import trainer
import os
from res import messages
from res import messageWin

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
        Dialog.resize(338, 321)
        Dialog.setMinimumSize(QtCore.QSize(338, 321))
        Dialog.setMaximumSize(QtCore.QSize(338, 321))
        Dialog.setStyleSheet(_fromUtf8("#Dialog{\n"
"    background-image:url(:/drawable/background.jpg)\n"
"}"))
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
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
        self.gridLayout_2.addWidget(self.submit, 2, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:white;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.section = QtGui.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.section.setFont(font)
        self.section.setObjectName(_fromUtf8("section"))
        self.horizontalLayout_6.addWidget(self.section)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:white;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.branch = QtGui.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.branch.setFont(font)
        self.branch.setObjectName(_fromUtf8("branch"))
        self.horizontalLayout_2.addWidget(self.branch)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:white;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.year = QtGui.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.year.setFont(font)
        self.year.setObjectName(_fromUtf8("year"))
        self.horizontalLayout_4.addWidget(self.year)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        query = "SELECT NAME FROM DEPARTMENT"
        cur.execute(query)
        docs = cur.fetchall()
        for doc in docs:
            self.branch.addItem(doc[0])

        self.branch.currentIndexChanged.connect(self.change)
        self.submit.clicked.connect(self.train)

    def change(self):
        text = self.branch.currentText()
        self.year.clear()
        self.section.clear()
        query = "SELECT YEAR, SECTION FROM DEPARTMENT WHERE NAME='{}'".format(text)
        cur.execute(query)
        docs = cur.fetchone()
        for i in range(int(docs[0])):
            self.year.addItem(str(i+1))
        for i in range(int(docs[1])):
            self.section.addItem(str(i+1))

    def train(self):
        branch = self.branch.currentText()
        year = self.year.currentText()
        section = self.section.currentText()
        path = "dataset/"+str(branch)+"/"+str(year)+"/"+str(section)
        if not os.path.exists(path):
            messageWin.pop_up_window(messages.errorTitle, messages.noDirectoryError)
        else:
            path2 = "recognizer/"+str(branch)+"/"+str(year)+"/"+str(section)
            if not os.path.exists(path2):
                os.makedirs(path2)
            trainer.main(path,path2)

    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Train Dataset", None))
        self.submit.setText(_translate("Dialog", "OK!", None))
        self.label_3.setText(_translate("Dialog", "Section:", None))
        self.label.setText(_translate("Dialog", "Branch:", None))
        self.label_2.setText(_translate("Dialog", "Year:", None))

import res.resources_re

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

