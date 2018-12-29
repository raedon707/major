from PyQt4 import QtCore, QtGui
import signup
import studentSignup
import addDepartment
import traindataset

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(938, 795)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuStart = QtGui.QMenu(self.menubar)
        self.menuStart.setObjectName(_fromUtf8("menuStart"))
        self.menuRegistration = QtGui.QMenu(self.menubar)
        self.menuRegistration.setObjectName(_fromUtf8("menuRegistration"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuAdd = QtGui.QMenu(self.menuSettings)
        self.menuAdd.setObjectName(_fromUtf8("menuAdd"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCollege_Configure = QtGui.QAction(MainWindow)
        self.actionCollege_Configure.setObjectName(_fromUtf8("actionCollege_Configure"))
        self.actionTeacher_Registration = QtGui.QAction(MainWindow)
        self.actionTeacher_Registration.setObjectName(_fromUtf8("actionTeacher_Registration"))
        self.actionStudent_registration = QtGui.QAction(MainWindow)
        self.actionStudent_registration.setObjectName(_fromUtf8("actionStudent_registration"))
        self.actionAdd_department = QtGui.QAction(MainWindow)
        self.actionAdd_department.setObjectName(_fromUtf8("actionAdd_department"))
        self.actionAdd_Section = QtGui.QAction(MainWindow)
        self.actionAdd_Section.setObjectName(_fromUtf8("actionAdd_Section"))
        self.actionAdd_Department = QtGui.QAction(MainWindow)
        self.actionAdd_Department.setObjectName(_fromUtf8("actionAdd_Department"))
        self.actionAdd_Department_2 = QtGui.QAction(MainWindow)
        self.actionAdd_Department_2.setObjectName(_fromUtf8("actionAdd_Department_2"))
        self.actionAdd_Section_2 = QtGui.QAction(MainWindow)
        self.actionAdd_Section_2.setObjectName(_fromUtf8("actionAdd_Section_2"))
        self.actionStart_Recognizing = QtGui.QAction(MainWindow)
        self.actionStart_Recognizing.setObjectName(_fromUtf8("actionStart_Recognizing"))
        self.actionConfigure_College_Database = QtGui.QAction(MainWindow)
        self.actionConfigure_College_Database.setObjectName(_fromUtf8("actionConfigure_College_Database"))
        self.actionConfigure_College_database = QtGui.QAction(MainWindow)
        self.actionConfigure_College_database.setObjectName(_fromUtf8("actionConfigure_College_database"))
        self.actionAdd_Department_3 = QtGui.QAction(MainWindow)
        self.actionAdd_Department_3.setObjectName(_fromUtf8("actionAdd_Department_3"))
        self.actionAdd_Section_3 = QtGui.QAction(MainWindow)
        self.actionAdd_Section_3.setObjectName(_fromUtf8("actionAdd_Section_3"))
        self.actionTrain_Dataset = QtGui.QAction(MainWindow)
        self.actionTrain_Dataset.setObjectName(_fromUtf8("actionTrain_Dataset"))
        self.actionTeacher_Registration_2 = QtGui.QAction(MainWindow)
        self.actionTeacher_Registration_2.setObjectName(_fromUtf8("actionTeacher_Registration_2"))
        self.actionStudent_registration_2 = QtGui.QAction(MainWindow)
        self.actionStudent_registration_2.setObjectName(_fromUtf8("actionStudent_registration_2"))
        self.actionStart_Detection = QtGui.QAction(MainWindow)
        self.actionStart_Detection.setObjectName(_fromUtf8("actionStart_Detection"))
        self.menuStart.addAction(self.actionStart_Detection)
        self.menuRegistration.addAction(self.actionTeacher_Registration_2)
        self.menuRegistration.addAction(self.actionStudent_registration_2)
        self.menuAdd.addAction(self.actionAdd_Department_3)
        self.menuAdd.addAction(self.actionAdd_Section_3)
        self.menuSettings.addAction(self.actionConfigure_College_database)
        self.menuSettings.addAction(self.menuAdd.menuAction())
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionTrain_Dataset)
        self.menubar.addAction(self.menuStart.menuAction())
        self.menubar.addAction(self.menuRegistration.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.actionTeacher_Registration_2.triggered.connect(self.teacher)
        self.actionStudent_registration_2.triggered.connect(self.student)
        self.actionAdd_Department_3.triggered.connect(self.department)
        self.actionTrain_Dataset.triggered.connect(self.training)
        self.menuStart.triggered.connect(self.startCapture)

    def teacher(self):
        self.Dialog = QtGui.QDialog()
        self.ui = signup.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def student(self):
        self.Dialog = QtGui.QDialog()
        self.ui = studentSignup.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def department(self):
        self.Dialog = QtGui.QDialog()
        self.ui = addDepartment.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
    
    def training(self):
        self.Dialog = QtGui.QDialog()
        self.ui = traindataset.Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def startCapture(self):
        import startDetection
        self.ui = startDetection.Window()
        self.ui.show()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuStart.setTitle(_translate("MainWindow", "start", None))
        self.menuRegistration.setTitle(_translate("MainWindow", "Registration", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuAdd.setTitle(_translate("MainWindow", "Add", None))
        self.actionCollege_Configure.setText(_translate("MainWindow", "Configure College database", None))
        self.actionTeacher_Registration.setText(_translate("MainWindow", "Teacher Registration", None))
        self.actionStudent_registration.setText(_translate("MainWindow", "Student registration", None))
        self.actionAdd_department.setText(_translate("MainWindow", "Add department", None))
        self.actionAdd_Section.setText(_translate("MainWindow", "Add Section", None))
        self.actionAdd_Department.setText(_translate("MainWindow", "Add Department", None))
        self.actionAdd_Department_2.setText(_translate("MainWindow", "Add Department", None))
        self.actionAdd_Section_2.setText(_translate("MainWindow", "Add Section", None))
        self.actionStart_Recognizing.setText(_translate("MainWindow", "Start Recognizing", None))
        self.actionConfigure_College_Database.setText(_translate("MainWindow", "Configure College Database", None))
        self.actionConfigure_College_database.setText(_translate("MainWindow", "Configure College database", None))
        self.actionAdd_Department_3.setText(_translate("MainWindow", "Add Department", None))
        self.actionAdd_Section_3.setText(_translate("MainWindow", "Add Section", None))
        self.actionTrain_Dataset.setText(_translate("MainWindow", "Train Dataset", None))
        self.actionTeacher_Registration_2.setText(_translate("MainWindow", "Teacher Registration", None))
        self.actionStudent_registration_2.setText(_translate("MainWindow", "Student registration", None))
        self.actionStart_Detection.setText(_translate("MainWindow", "Start detection", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

