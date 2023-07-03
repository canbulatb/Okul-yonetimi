from PyQt5 import QtWidgets, uic
class studentData(QtWidgets.QMainWindow):
    def __init__(self):
        super(studentData, self).__init__()
        uic.loadUi('./ui/student.ui', self)
        self.back_button.clicked.connect(self.studentDataBack)
        
    def studentDataBack(self):
        self.hide()
   