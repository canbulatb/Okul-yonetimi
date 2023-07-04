from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Veritabanına bağlantı oluşturma
database = QSqlDatabase.addDatabase('QSQLITE')
database.setDatabaseName('okulYonetimi.db')  # Veritabanı dosyasının adını belirtin
# Veritabanıyla bağlantıyı açma
if database.open():
    print('Veritabanına bağlantı başarılı.')

    # Veritabanı üzerinde işlemler yapabilirsiniz

    # Dosyadan veri okuma
    query = QSqlQuery()
    query.exec_('SELECT * FROM tablo')  # "tablo" adlı tablodaki verileri seçin

    while query.next():
        # Verileri okuyun
        id = query.value(0)
        name = query.value(1)
        age = query.value(2)

        print(f'ID: {id}, Ad: {name}, Yaş: {age}')

    # Veritabanı bağlantısını kapatma
    database.close()
else:
    print('Veritabanına bağlantı hatası.')
