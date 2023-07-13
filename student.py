from PyQt5 import QtWidgets, uic
from teacherData import *
from query import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from studentData import *


class student(QtWidgets.QMainWindow):
    def __init__(self):
        super(student, self).__init__()
        uic.loadUi('./ui/loginstudent.ui', self)     
        self.sloginbutton.clicked.connect(self.studentDataCall)
        self.sbackbutton.clicked.connect(self.studentBack)
        self.studentData = None    


    def studentDataCall(self):
        ogrenciNo = self.snumberline.text()
        sifre=self.spasswordline.text()
        kontrol=okStudentGiris(ogrenciNo,sifre)
        if kontrol:
            if self.studentData is None:
                self.studentData = studentData(kontrol)
                self.studentData.onceki_pencere = self.onceki_pencere
            #self.teacher = teacher()    
            self.studentData.show()
            self.hide()
        
            
    def studentBack(self):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.hide()          
        
    def closeEvent(self, event):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.hide()          