from PyQt5 import QtWidgets, uic
from student  import *
from teacher  import *

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./ui/entry.ui', self)  #Sayfamızı yüklüyoruz.
        self.StudentButton.clicked.connect(self.studentOpen) 
        self.TeacherButton.clicked.connect(self.teacherOpen)
        self.teacher = None
        self.student = None


    def studentOpen(self):
        if self.student is None:
            self.student = student()
            self.student.onceki_pencere = self 
        self.student.show()
        self.hide()         
    def teacherOpen(self):
        if self.teacher is None:
            self.teacher = teacher()
            self.teacher.onceki_pencere = self 
        #self.teacher = teacher()    
        self.teacher.show()
        self.hide()


app = QtWidgets.QApplication([])
window = Ui()
window.show()
app.exec_()





