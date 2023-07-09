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
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.close()          
        
    def closeEvent(self, event):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.close()          