from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def sorgula(sorgu):
    database = QSqlDatabase.addDatabase('QSQLITE')
    database.setDatabaseName('okulYonetimi.db')
    if database.open():
        print('Veritabanına bağlantı başarılı.')
        query = QSqlQuery()
        query.prepare(sorgu)    
        query.exec_()
    
        while query.next():
            id = query.value(0)
            kullaniciAdi = query.value(1)
            age = query.value(2)
            isim=query.value(3)
        print(isim)
        database.close() 
        return isim




def okTeacherGiris(kullaniciAdi,sifre):
    sorgu='SELECT * FROM teacher WHERE kullanici_adi = \''+kullaniciAdi+'\' AND sifre = \''+sifre+'\''
    sonuc=sorgula(sorgu)
    
    return sonuc
    
    
