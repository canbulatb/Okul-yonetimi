from PyQt5 import QtWidgets, uic
from studentData import *

class student(QtWidgets.QMainWindow):
    def __init__(self):
        super(student, self).__init__()
        uic.loadUi('./ui/loginstudent.ui', self)     
        self.sloginbutton.clicked.connect(self.studentDataCall)
        self.sbackbutton.clicked.connect(self.studentBack)

    def studentDataCall(self):
        self.studentData = studentData()
        self.studentData.show()
        
    def studentBack(self):
        self.hide()