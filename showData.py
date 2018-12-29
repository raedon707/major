import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pymysql
from functools import partial
from res import messages
from res import messageWin
from res.vars import host,port,user,passwd,db
import recognition
import threading, time
import sheets

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

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self, path, path2):
        recognition.start_recognition(path, path2)

class Window():
    def __init__(self):
##        QWidget.__init__(self)
##
##        layout = QVBoxLayout()
##        self.checks = []
##        self.shops = []
        data = sheets.getdata()
        for doc in data:
            print(doc)
##        query = "SELECT * FROM DEPARTMENT"
##        cur.execute(query)
##        self.c = "" 
##        data = cur.fetchall()
##        for doc in data:
##            for d in range(int(doc[2])):
##                for c in range(int(doc[3])):
##                    text = doc[1]+","+str(d+1)+","+str(c+1)
##                    self.c = QCheckBox(doc[1]+" year "+str(d+1)+" section "+str(c+1))
##                    layout.addWidget(self.c)
##                    self.checks.append(self.c)
##                    self.c.stateChanged.connect(partial(self.state_changed, text))
##        self.submit = QtGui.QPushButton("Submit")
##        layout.addWidget(self.submit)
##        self.setLayout(layout)
##
##        self.submit.clicked.connect(self.conn)
            
    def state_changed(self, shop, state):
        if state == Qt.Checked:
            self.shops.append(shop)
        else:
            try:
                self.shops.remove(shop)
            except:
                print("something went wrong")

    def conn(self):
        path2 =" "
        path = " "
        paths = []
        paths2 = []
        for data in self.shops:
            path = "recognizer/"
            path2 = ""
            data = data.split(',')
            for d in data:
                path += d+"/"
                path2 += d
            paths.append(path)
            paths2.append(path2)

        mt = MyThread()
        for i in range(len(paths)):
            mt.run(paths[i], paths2[i])
        
##if __name__ == '__main__':
##    app = QApplication(sys.argv)
##    w = Window()
##    w.show()
##    app.exec_()
