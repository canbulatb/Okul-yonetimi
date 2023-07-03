from PyQt5 import QtWidgets, uic

class teacherData(QtWidgets.QMainWindow): 
    def __init__(self):
        super(teacherData, self).__init__()
        uic.loadUi('./ui/teacher1.ui', self) 
        self.closebutton.clicked.connect(self.teacherDataClose)
        
    def teacherDataClose(self):
        self.hide()
   