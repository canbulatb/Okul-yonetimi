from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem


class teacherData(QtWidgets.QMainWindow): 
    def __init__(self,kullanciAdi):
        veri=[["Matematik","10 A","30"],["Fizik","10 A","30"],["Kimya","10 A","30"],["Biyoloji","10 A","30"],["Matematik","10 A","30"]]
        super(teacherData, self).__init__()
        uic.loadUi('./ui/teacher1.ui', self)
        self.tname_label.setText(kullanciAdi)
        self.lessonWidgedFull(veri)
        self.closebutton.clicked.connect(self.teacherDataClose)
        
    def teacherDataClose(self):
        self.hide()
    
    def lessonWidgetEmpty(self):
        for i in range(5):
            self.lesson_widget.setItem(i, 0, QTableWidgetItem(""))
            self.lesson_widget.setItem(i, 1, QTableWidgetItem(""))
            self.lesson_widget.setItem(i, 2, QTableWidgetItem(""))
            
    def lessonWidgedFull(self,veri):
        self.lessonWidgetEmpty()
        for i in range(5):
            self.lesson_widget.setItem(i, 0, QTableWidgetItem(str(veri[i][0])))
            self.lesson_widget.setItem(i, 1, QTableWidgetItem(str(veri[i][1])))
            self.lesson_widget.setItem(i, 2, QTableWidgetItem(str(veri[i][2])))
    
    