from PyQt5 import QtWidgets, uic
from teacherData import *

class teacher(QtWidgets.QMainWindow): 
    def __init__(self):
        super(teacher, self).__init__()
        uic.loadUi('./ui/loginteacher.ui', self) 
        self.tloginbutton.clicked.connect(self.teacherDataCall)
        self.tbackbutton.clicked.connect(self.teacherBack)

    def teacherDataCall(self):
        self.teacherData = teacherData()    
        self.teacherData.show()
        
    def teacherBack(self):
        self.hide()
        
        
        #self.tloginbutton.clicked.connect(self.changeName) 