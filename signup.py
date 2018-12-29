from PyQt4 import QtCore, QtGui
from res import messages
from res import messageWin
import pymysql
from res.vars import host, port, user, passwd, db

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
        Dialog.resize(500, 900)
        Dialog.setMinimumSize(QtCore.QSize(500, 900))
        Dialog.setMaximumSize(QtCore.QSize(500, 900))
        Dialog.setStyleSheet(_fromUtf8("#Dialog{\n"
"    background-image:url(:/drawable/background.jpg)\n"
"}"))
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:white;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.department = QtGui.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.department.setFont(font)
        self.department.setObjectName(_fromUtf8("department"))
        self.horizontalLayout_2.addWidget(self.department)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:white;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.dob = QtGui.QDateEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.dob.setFont(font)
        self.dob.setObjectName(_fromUtf8("dob"))
        self.horizontalLayout.addWidget(self.dob)
        self.gridLayout_3.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.cclasses = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.cclasses.setFont(font)
        self.cclasses.setStyleSheet(_fromUtf8("#cclasses{\n"
"    color:white;\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    border-bottom:2px solid white;\n"
"}"))
        self.cclasses.setObjectName(_fromUtf8("cclasses"))
        self.gridLayout_3.addWidget(self.cclasses, 9, 1, 1, 1)
        self.password = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.password.setFont(font)
        self.password.setStyleSheet(_fromUtf8("#password{\n"
"    color:white;\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    border-bottom:2px solid white;\n"
"}"))
        self.password.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout_3.addWidget(self.password, 4, 1, 1, 1)
        self.id = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.id.setFont(font)
        self.id.setStyleSheet(_fromUtf8("#id{\n"
"    color:white;\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    border-bottom:2px solid white;\n"
"}"))
        self.id.setObjectName(_fromUtf8("id"))
        self.gridLayout_3.addWidget(self.id, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.name = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.name.setFont(font)
        self.name.setStyleSheet(_fromUtf8("#name{\n"
"    color:white;\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    border-bottom:2px solid white;\n"
"}"))
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout_3.addWidget(self.name, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.email = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.email.setFont(font)
        self.email.setStyleSheet(_fromUtf8("#email{\n"
"    border:none;\n"
"    color:white;\n"
"    background-color:transparent;\n"
"    border-bottom:2px solid white;\n"
"}"))
        self.email.setObjectName(_fromUtf8("email"))
        self.gridLayout_3.addWidget(self.email, 2, 1, 1, 1)
        self.classes = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.classes.setFont(font)
        self.classes.setStyleSheet(_fromUtf8("#classes{\n"
"    color:white;\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    border-bottom:2px solid white;\n"
"}"))
        self.classes.setObjectName(_fromUtf8("classes"))
        self.gridLayout_3.addWidget(self.classes, 8, 1, 1, 1)
        self.phone = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.phone.setFont(font)
        self.phone.setStyleSheet(_fromUtf8("#phone{\n"
"    border:none;\n"
"    color:white;\n"
"    background-color:transparent;\n"
"    border-bottom:2px solid white;\n"
"}"))
        self.phone.setObjectName(_fromUtf8("phone"))
        self.gridLayout_3.addWidget(self.phone, 3, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:white;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.role = QtGui.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        self.role.setFont(font)
        self.role.setObjectName(_fromUtf8("role"))
        self.horizontalLayout_3.addWidget(self.role)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 7, 1, 1, 1)
        self.registerFacult = QtGui.QPushButton(Dialog)
        self.registerFacult.setStyleSheet(_fromUtf8("#registerFacult{\n"
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
"#registerFacult:hover{\n"
"    background-color:royalBlue;\n"
"    color:white;\n"
"}\n"
"#registerFacult:pressed{\n"
"    background-color:rgb(0, 99, 153);\n"
"    color:white;\n"
"}"))
        self.registerFacult.setObjectName(_fromUtf8("registerFacult"))
        self.gridLayout_3.addWidget(self.registerFacult, 10, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        try:
            query = "SELECT NAME FROM DEPARTMENT"
            cur.execute(query)
            department_name = cur.fetchall()
        except Exception as e:
            print("something went wrong")

        role_list = ['Teacher', 'Coordinator', 'HOD']
        for doc in department_name:
            self.department.addItems(doc)
        self.role.addItems(role_list)

        self.registerFacult.clicked.connect(self.register)

    def register(self):
        name = self.name.text()
        teacherid = self.id.text()
        email = self.email.text()
        phone = self.phone.text()
        password = self.password.text()
        dob = self.dob.date()
        department = self.department.currentText()
        role = self.role.currentText()
        classes = self.classes.text()
        cclasses = self.cclasses.text()
        dob = dob.toPyDate()
        
        if(name == "" or teacherid == "" or email == "" or phone == "" or password == ""):
            messageWin.pop_up_window(messages.errorTitle, messages.emptyFieldError)
        else:
            try:
                query = "CREATE TABLE IF NOT EXISTS TEACHERS(SNO INT(3) NOT NULL AUTO_INCREMENT, NAME VARCHAR(30), ID VARCHAR(30), EMAIL_ID VARCHAR(40), MOBILE_NO VARCHAR(13), DOB VARCHAR(10), CLASSES VARCHAR(100), COORDINATED_CLASSES VARCHAR(100), PASSWORD VARCHAR(50), DEPARTMENT VARCHAR(5), ROLE VARCHAR(10), UNIQUE (ID), PRIMARY KEY (SNO))"
                cur.execute(query)
                try:
                    cur.execute("INSERT INTO TEACHERS(NAME, ID, EMAIL_ID, MOBILE_NO, DOB, CLASSES, COORDINATED_CLASSES, PASSWORD, DEPARTMENT, ROLE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (str(name), str(teacherid), str(email), str(phone), str(dob), str(classes), str(cclasses), str(password), str(department), str(role)))
                    conn.commit()
                except Exception as e:
                    messageWin.pop_up_window(messages.SQLErrorTitle, messages.SQLInsertError)
                    conn.close()
            except Exception as e:
                print("error2")            

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Department:", None))
        self.label.setText(_translate("Dialog", "DOB:", None))
        self.cclasses.setPlaceholderText(_translate("Dialog", "Coordinated classes", None))
        self.password.setPlaceholderText(_translate("Dialog", "Password", None))
        self.id.setPlaceholderText(_translate("Dialog", "ID", None))
        self.name.setPlaceholderText(_translate("Dialog", "Name", None))
        self.email.setPlaceholderText(_translate("Dialog", "E-mail", None))
        self.classes.setPlaceholderText(_translate("Dialog", "Classes", None))
        self.phone.setPlaceholderText(_translate("Dialog", "Phone", None))
        self.label_3.setText(_translate("Dialog", "Role:", None))
        self.registerFacult.setText(_translate("Dialog", "Signup", None))

import res.resources_re

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
