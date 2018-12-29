from PyQt4 import QtCore, QtGui
import pymysql
from res import messages
from res import messageWin
from res.vars import host, port, user, passwd, db

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
        Dialog.resize(439, 394)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(439, 394))
        Dialog.setMaximumSize(QtCore.QSize(439, 394))
        Dialog.setStyleSheet(_fromUtf8("#Dialog{\n"
"    background-image:url(:/drawable/background.jpg)\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.FieldRole, spacerItem)
        self.depName = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.depName.setFont(font)
        self.depName.setStyleSheet(_fromUtf8("border:none;\n"
"border-bottom:2px solid white;\n"
"color:white;\n"
"background-color:transparent;"))
        self.depName.setObjectName(_fromUtf8("depName"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.depName)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:white;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.year = QtGui.QSpinBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.year.setFont(font)
        self.year.setObjectName(_fromUtf8("year"))
        self.horizontalLayout_3.addWidget(self.year)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:white;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.section = QtGui.QSpinBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.section.setFont(font)
        self.section.setObjectName(_fromUtf8("section"))
        self.horizontalLayout_5.addWidget(self.section)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtGui.QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtGui.QFormLayout.FieldRole, spacerItem2)
        self.submit = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)
        self.submit.setMinimumSize(QtCore.QSize(408, 49))
        self.submit.setMaximumSize(QtCore.QSize(408, 49))
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
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.submit)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtGui.QFormLayout.FieldRole, spacerItem3)
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.submit.clicked.connect(self.Submit)

    def Submit(self):
        name = self.depName.text()
        year = self.year.value()
        section = self.section.value()      
        try:
            conn = pymysql.connect(host = host, port = port, user = user, passwd = passwd, db = db)
            cur = conn.cursor()
        except Exception as e:
            messageWin.pop_up_window(messages.SQLErrorTitle, messages.SQLError)
        try:
            query = "CREATE TABLE IF NOT EXISTS DEPARTMENT(SNO INT(3) NOT NULL AUTO_INCREMENT, NAME VARCHAR(20), YEAR VARCHAR(3), SECTION VARCHAR(3), PRIMARY KEY(SNO), UNIQUE(NAME))"
            cur.execute(query)
            try:
                cur.execute("INSERT INTO DEPARTMENT(NAME, YEAR, SECTION) VALUES(%s,%s,%s)", (str(name), str(year), str(section)))
                conn.commit()
                conn.close()
            except Exception as e:
                messageWin.pop_up_window(messages.SQLErrorTitle, messages.SQLInsertError)
        except Exception as e:
            print("error2")

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Department", None))
        self.depName.setPlaceholderText(_translate("Dialog", "Department Name", None))
        self.label.setText(_translate("Dialog", "Years:", None))
        self.label_2.setText(_translate("Dialog", "Sections/Year: ", None))
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

