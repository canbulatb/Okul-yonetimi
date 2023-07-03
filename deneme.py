#İlk başta kütüphanelerimizi çağırıyoruz.
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal #Bu veriyi sayfadan sayfaya aktarmak için lazım olacak.
import sys

#Bu ilk sayfamızın sınıfı, buradan başlayalım.
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./ui/entry.ui', self)  #Sayfamızı yüklüyoruz.
        self.dialog = secondPage() #İkinci sayfamızın sınıfı, bunu çağırabilmek
                                  #için kullanacağız.
        self.StudentButton.clicked.connect(self.openSecondPage) #Tıklayınca ikinci
                                                                   #sayfa yönlendirecek.
        #self.dialog.mySignal.connect(self.changeData) #İkinci sayfamızdaki veri değiştiğinde
                                                #ve butona tıklanıldığında burası çalışacak.
    
    def openSecondPage(self): #ikinci sayfayi acabilmek icin bunu kullaniyoruz.
        self.dialog.show()
    
    def changeData(self, data): #Veri değiştiğinde label adlı yazı bölgemize
        self.label.setText(data) #değerimizi atıyoruz.

class secondPage(QtWidgets.QMainWindow): #ikinci sayfanin sinifi burada bulunmaktadir.
    
    mySignal = pyqtSignal(str)
    
    def __init__(self):
        super(secondPage, self).__init__()
        uic.loadUi('./ui/loginstudent.ui', self)  #İkinci sayfamızı buradan açıyoruz.
        
        self.sloginbutton.clicked.connect(self.changeName) #Butona tıkladığımızda
                                                      #fonksiyon çalışıyor.
    
    def changeName(self):
        data = self.dataEdit.text() #Verimizi ilk başta alıyoruz.
        print("new name: " + data) #Test için yazdırdım ben konsolda.
        self.mySignal.emit(data) #Şimdi verimizle beraber sinyal gönderiyoruz alıcıya. 
        #                         13. satırda alıcımız bulunmakta. 

#Bu kısım ilk başta çalışmaktadır.
app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()