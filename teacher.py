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
        self.teacherData = None        
    
        
    def teacherDataCall(self):
        kullaniciAdi = self.usernameline.text()
        sifre=self.tpasswordline.text()
        kontrol=okTeacherGiris(kullaniciAdi,sifre)
        if kontrol:
            if self.teacherData is None:
                self.teacherData = teacherData(kontrol)
                self.teacherData.onceki_pencere = self 
            #self.teacher = teacher()    
            self.teacherData.show()
            self.hide()

        
    def closeEvent(self, event):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.close()          
        
    def teacherBack(self):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.close()
        
        
        #self.tloginbutton.clicked.connect(self.changeName) 