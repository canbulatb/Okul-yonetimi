from PyQt5 import QtWidgets, uic
from teacherData import *
from query import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class teacher(QtWidgets.QMainWindow): 
    def __init__(self):
        super(teacher, self).__init__()
        uic.loadUi('./ui/loginteacher.ui', self) 
        self.tloginbutton.clicked.connect(self.teacherDataCall)
        self.tbackbutton.clicked.connect(self.teacherBack)
    
        
    def teacherDataCall(self):
        kullaniciAdi = self.usernameline.text()
        sifre=self.tpasswordline.text()
        kontrol=okTeacherGiris(kullaniciAdi,sifre)
        if kontrol:
            print(kontrol)
            self.teacherData = teacherData(kontrol)
            self.teacherData.show()
        
            
        
    def teacherBack(self):
        self.hide()
        
        
        #self.tloginbutton.clicked.connect(self.changeName) 