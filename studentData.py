from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem


class studentData(QtWidgets.QMainWindow):
    def __init__(self,kontrol):
        super(studentData, self).__init__()
        uic.loadUi('./ui/student.ui', self)
        veri=[["Matematik","10","30"],["Fizik","10","30"],["Kimya","10","30"],["Biyoloji","10","30"],["Matematik","10","30"]]
        
        
        self.back_button.clicked.connect(self.studentDataBack)
        
        self.number_label.setText(str(kontrol[0][1]))
        self.name_label.setText(kontrol[0][3])
        self.termWidgedFull(veri)
        
        
        
        
    def studentDataBack(self):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.close()          
        
    def closeEvent(self, event):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.close()          
        
        
    def termWidgetEmpty(self):
        for i in range(5):
            self.term_widget.setItem(i, 0, QTableWidgetItem(""))
            self.term_widget.setItem(i, 1, QTableWidgetItem(""))
            self.term_widget.setItem(i, 2, QTableWidgetItem(""))
    
    def termWidgedFull(self,veri):
        self.termWidgetEmpty()
        for i in range(len(veri)):
            self.term_widget.setItem(i, 0, QTableWidgetItem(str(veri[i][0])))
            self.term_widget.setItem(i, 1, QTableWidgetItem(str(veri[i][1])))
            self.term_widget.setItem(i, 2, QTableWidgetItem(str(veri[i][2])))