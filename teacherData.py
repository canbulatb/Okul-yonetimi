from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from query import *


class teacherData(QtWidgets.QMainWindow): 
    def __init__(self,kullanciAdi):
        #veri=[["Matematik","10 A","30"],["Fizik","10 A","30"],["Kimya","10 A","30"],["Biyoloji","10 A","30"],["Matematik","10 A","30"]]
        super(teacherData, self).__init__()
        uic.loadUi('./ui/teacher1.ui', self)
        self.tname_label.setText(kullanciAdi[0][3])
        self.aktifOgrenciId=""
        veri=okTeacherlessonWidget(kullanciAdi[0][0])
        self.kullaniciAdi=kullanciAdi[0][0]
        self.lessonWidgedFull(veri)
        self.comboBoxAdd(kullanciAdi[0][0])
        self.comboBoxRemove(kullanciAdi[0][0])
        self.lesson_combo_2Add(kullanciAdi[0][0])
        
        
        self.remove_button_2.clicked.connect(self.comboBoxRemoveLesson)
        self.student_combo.currentTextChanged.connect(self.showStudentInfo)
        self.lesson_combo_2.currentTextChanged.connect(self.showStudents)
        self.edit_button.clicked.connect(self.showStudentEdit)
        self.show_button.clicked.connect(self.showStudentInfo)
        self.ok_button.clicked.connect(self.showStudents)
        self.closebutton.clicked.connect(self.teacherDataClose)
        self.add_button.clicked.connect(self.comboBoxAddLesson)
    
    def comboBoxAddLesson(self):
        ders=self.lesson_combo.currentText()
        comboBoxAddLes(ders,self.kullaniciAdi)
        veri=okTeacherlessonWidget(self.kullaniciAdi)
        self.lessonWidgedFull(veri)
        self.comboBoxRemove(self.kullaniciAdi)
        self.comboBoxAdd(self.kullaniciAdi)

    def comboBoxRemoveLesson(self):
        ders=self.lesson_combo_6.currentText()
        comboBoxRemoveLes(ders,self.kullaniciAdi)
        veri=okTeacherlessonWidget(self.kullaniciAdi)
        self.lessonWidgedFull(veri)
        self.comboBoxRemove(self.kullaniciAdi)
        self.comboBoxAdd(self.kullaniciAdi)



    def closeEvent(self, event):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.close()          
    
    def teacherDataClose(self):
        if self.onceki_pencere is not None:
            self.onceki_pencere.show()
        self.close()         

    def comboBoxAdd(self,veri):
        self.lesson_combo_6.clear()
        sonuc=okRemoveComboboxVeri(veri)
        for row in sonuc:
            self.lesson_combo_6.addItem(row[0])

    def comboBoxRemove(self,veri):
        self.lesson_combo.clear()
        sonuc=okAddComboboxVeri(veri)
        for row in sonuc:
            self.lesson_combo.addItem(str(row))
    
    
    def lessonWidgetEmpty(self):
        for i in range(5):
            self.lesson_widget.setItem(i, 0, QTableWidgetItem(""))
            self.lesson_widget.setItem(i, 1, QTableWidgetItem(""))
            self.lesson_widget.setItem(i, 2, QTableWidgetItem(""))
    
    def lessonWidgedFull(self,veri):
        self.lessonWidgetEmpty()
        for i in range(len(veri)):
            self.lesson_widget.setItem(i, 0, QTableWidgetItem(str(veri[i][0])))
            self.lesson_widget.setItem(i, 1, QTableWidgetItem(str(veri[i][1])))
            self.lesson_widget.setItem(i, 2, QTableWidgetItem(str(veri[i][2])))
    
    def lesson_combo_2Add(self, veri):
        sonuc=okRemoveComboboxVeri(veri)
        for row in sonuc:
            self.lesson_combo_2.addItem(str(row[0]))

    def showStudents(self):
        self.showStudentInfoEmpty()
        self.student_combo.clear()
        ders=self.lesson_combo_2.currentText()
        sonuc=studentListele(self.kullaniciAdi, ders)
        for row in sonuc:
            self.student_combo.addItem(row[0])
    
    def showStudentInfoEmpty(self):
        self.name.setText("")
        self.gender.setText("")
        self.birth.setText("")
        self.midterm.setText("")
        self.final_2.setText("")
        self.attendance.setText("")
        self.aktifOgrenciId=""
    
    def showStudentInfo(self):
        self.showStudentInfoEmpty()
        ogrenci=self.student_combo.currentText()
        ders=self.lesson_combo_2.currentText()
        sonuc=studentInfo(self.kullaniciAdi,ogrenci,ders)
        if len(sonuc)>0:
            self.name.setText(sonuc[0][0])
            self.gender.setText(sonuc[0][1])
            self.birth.setText(sonuc[0][2])
            self.midterm.setText(str(sonuc[0][3]))
            self.final_2.setText(str(sonuc[0][4]))
            self.attendance.setText(str(sonuc[0][5]))
            self.aktifOgrenciId=str(sonuc[0][6])
        
    
    
    
    
    def showStudentEdit(self):
        studentEdit(self)
        