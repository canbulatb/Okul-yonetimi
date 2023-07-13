from PyQt5 import QtWidgets, uic
from teacherData import *
from query import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class teacher(QtWidgets.QMainWindow): 
    def __init__(self):
        super(teacher, self).__init__()
        uic.loadUi('./ui/loginteacher.ui', self) 
        self.usernameline.setText("")
        self.tpasswordline.setText("")
        
        self.tloginbutton.clicked.connect(self.teacherDataCall)
        self.tbackbutton.clicked.connect(self.teacherBack)
        self.teacherData = None
        self.kullanici=[]       
    
        
    def teacherDataCall(self):
        kullaniciAdi = self.usernameline.text()
        sifre=self.tpasswordline.text()
        self.kullanici=[]
        self.kullanici=okTeacherGiris(kullaniciAdi,sifre)
        if self.kullanici[0][1]==kullaniciAdi and self.kullanici[0][2]:  #hata var...

            self.teacherData = teacherData()
            self.teacherData.onceki_pencere = self.onceki_pencere 
            self.teacherData.tname_label.setText(self.kullanici[0][3])
            self.teacherData.aktifOgrenciId=""
            veri=okTeacherlessonWidget(self.kullanici[0][0])
            self.teacherData.kullaniciAdi=self.kullanici[0][0]
            self.teacherData.lessonWidgedFull(veri)
            self.teacherData.comboBoxAdd(self.kullanici[0][0])
            self.teacherData.comboBoxRemove(self.kullanici[0][0])
            self.teacherData.lesson_combo_2Add(self.kullanici[0][0])
            self.teacherData.lessonAddRemove()
        
                
                
            #self.teacher = teacher()   
            
            self.teacherData.show()
            self.hide()


        
    def closeEvent(self, event):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.hide()          
        
    def teacherBack(self):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.hide()
        
        
        #self.tloginbutton.clicked.connect(self.changeName) 