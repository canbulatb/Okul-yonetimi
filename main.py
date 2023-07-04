from PyQt5 import QtWidgets, uic
from student  import *
from teacher  import *

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./ui/entry.ui', self)  #Sayfamızı yüklüyoruz.
        self.StudentButton.clicked.connect(self.studentOpen) 
        self.TeacherButton.clicked.connect(self.teacherOpen)

    def studentOpen(self):
        self.student = student()
        self.student.show()
        self.close()
                
    def teacherOpen(self):
        self.teacher = teacher()    
        self.teacher.show()
        self.close()
app = QtWidgets.QApplication([])
window = Ui()
window.show()
app.exec_()





