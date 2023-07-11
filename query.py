from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sqlite3 

def sorgula(sorgu):
    conn = sqlite3.connect('okulYonetimi.db')
    database = conn.cursor()
    database.execute(sorgu)
    conn.commit()
    liste = database.fetchall()
    print(liste)
    database.close() 
    return liste



def okTeacherGiris(kullaniciAdi,sifre):
    sorgu='SELECT * FROM teacher WHERE kullanici_adi = \''+kullaniciAdi+'\' AND sifre = \''+sifre+'\''
    sonuc=sorgula(sorgu)
    return sonuc

def okTeacherlessonWidget(kullanici):
    sorgu="""SELECT ders_adi, class_adi, kapasite
            FROM ogretmen_data
            LEFT JOIN lesson on ogretmen_data.ders_id= lesson.id
            LEFT JOIN teacher on ogretmen_data.teacher_id= teacher.id
            where ogretmen_data.teacher_id="""+str(kullanici)
    sonuc=sorgula(sorgu)
    return sonuc

def okRemoveComboboxVeri(kullanici):
    sorgu="""SELECT ders_adi, class_adi, kapasite
            FROM ogretmen_data
            LEFT JOIN lesson on ogretmen_data.ders_id= lesson.id
            LEFT JOIN teacher on ogretmen_data.teacher_id= teacher.id
            where ogretmen_data.teacher_id="""+str(kullanici)
    sonuc=sorgula(sorgu)
       
    return sonuc
    
    
def okAddComboboxVeri(kullanici):
    sorgu="""SELECT id
        FROM lesson
        EXCEPT 
        SELECT ders_id FROM ogretmen_data 
        where teacher_id="""+str(kullanici)
    sonuc=sorgula(sorgu)
    
    sorgu2="""SELECT * FROM lesson"""
    sonuc2=sorgula(sorgu2)
    yeniDers=[]
    for i in range(len(sonuc2)):
        for j in range(len(sonuc)):
            if sonuc2[i][0]==sonuc[j][0]:
                yeniDers.append(sonuc2[i][1])
    print(yeniDers)
    
    return yeniDers
    
def studentListele(kullanici, ders):
    sorgu="""SELECT ogrenci_adi
        FROM ogrenci_data
        LEFT JOIN teacher on teacher.id= ogrenci_data.teacher_id 
        LEFT JOIN student on student.id= ogrenci_data.student_id
        LEFT JOIN lesson on lesson.id= ogrenci_data.ders_id
        where teacher.id="""+str(kullanici)+""" AND lesson.ders_adi=\""""+ders+"\""
    sonuc=sorgula(sorgu)
    return sonuc
    
    
def studentInfo(kullanici, ogrenci,ders):
    sorgu="""SELECT ogrenci_adi, ogrenci_cinsiyet, dogum_tarihi, ara_sinav, final, devamsizlik,student_id
        FROM ogrenci_data
        LEFT JOIN teacher on teacher.id= ogrenci_data.teacher_id 
        LEFT JOIN student on student.id= ogrenci_data.student_id
        LEFT JOIN lesson on lesson.id= ogrenci_data.ders_id
        WHERE teacher.id="""+str(kullanici)+""" AND lesson.ders_adi=\""""+ders+"""\"
        AND ogrenci_adi=\""""+ogrenci+"""\""""
    sonuc=sorgula(sorgu)
    return sonuc

def comboBoxAddLes(ders, kullanici):
    dersSorgu="SELECT id FROM lesson WHERE ders_adi=\""+ders+"\""
    dersSonuc=sorgula(dersSorgu)
    sorgu="""INSERT INTO ogretmen_data (teacher_id,ders_id)
            VALUES("""+str(kullanici)+""", """+str(dersSonuc[0][0])+"""); """
    sonuc=sorgula(sorgu)
    return sonuc

def comboBoxRemoveLes(ders, kullanici):
    dersSorgu="SELECT id FROM lesson WHERE ders_adi=\""+ders+"\""
    dersSonuc=sorgula(dersSorgu)
    sorgu="DELETE FROM ogretmen_data WHERE teacher_id="+str(kullanici)+" AND ders_id="+str(dersSonuc[0][0])
    sonuc=sorgula(sorgu)
    return sonuc




def studentEdit(self):
    virgul=False
    if self.midterm.text()!="":
        v="ara_sinav="+self.midterm.text()
        virgul=True
    if self.final_2.text()!="":
        f="final="+self.final_2.text()
        if virgul:
            f=", "+f
        virgul=True
    if self.attendance.text()!="":
        d="devamsizlik="+self.attendance.text()
        if virgul:
            d=", "+d
        
        
    k=self.aktifOgrenciId
    sorgu="UPDATE ogrenci_data SET "+v+" "+f+" "+d+" WHERE id="+k
    sonuc=sorgula(sorgu)
    return sonuc

def lessonAddRemoveQuery(kullaniciAdi):
    sorgu="""SELECT teacher_id, ders_adi
        FROM ogretmen_data
        LEFT JOIN lesson on lesson.id = ogretmen_data.ders_id"""
        #WHERE teacher_id="""+str(kullaniciAdi)
    sonuc=sorgula(sorgu)
    return sonuc

def showStudentLessonQuery(ders,kullaniciAdi):
    sorgu="""SELECT ogrenci_adi,  student_id
        FROM ogrenci_data
        LEFT JOIN teacher on teacher.id= ogrenci_data.teacher_id 
        LEFT JOIN student on student.id= ogrenci_data.student_id
        LEFT JOIN lesson on lesson.id= ogrenci_data.ders_id
		WHERE teacher_id=\""""+str(kullaniciAdi)+"\" AND ders_adi=\""+ders+"\""
    sonuc=sorgula(sorgu)
    print(sonuc)
    return sonuc


def ogrencileriGetir():
    sorgu="""SELECT id, ogrenci_adi FROM student"""
    sonuc=sorgula(sorgu)
    return sonuc

def ogrenciDersiAliyormu(kullaniciAdi,ogrenci,ders):
    sorgu="""SELECT ogrenci_adi,  student_id
        FROM ogrenci_data
        LEFT JOIN teacher on teacher.id= ogrenci_data.teacher_id 
        LEFT JOIN student on student.id= ogrenci_data.student_id
        LEFT JOIN lesson on lesson.id= ogrenci_data.ders_id
        WHERE ders_adi=\""""+ders+"\""+"AND student_id="+str(ogrenci)
		#WHERE teacher_id="""+str(kullaniciAdi)+" AND ders_adi=\""+ders+"\""+"AND student_id="+str(ogrenci)
    sonuc=sorgula(sorgu)
    print(sonuc)
    return sonuc

def dersKapasitesi(ders):
    sorgu="SELECT id, ders_adi, kapasite FROM lesson WHERE ders_adi=\""+ders+"\""
    sonuc=sorgula(sorgu)
    return sonuc
def kayitliOgrenciSayisi(ders):
    sorgu="""SELECT COUNT (ders_adi)
        FROM ogrenci_data
        LEFT JOIN teacher on teacher.id= ogrenci_data.teacher_id 
        LEFT JOIN student on student.id= ogrenci_data.student_id
        LEFT JOIN lesson on lesson.id= ogrenci_data.ders_id
        WHERE ders_adi=\""""+ders+"\""
    sonuc=sorgula(sorgu)
    print(sonuc)
    return sonuc

def ogrenciyiDerseEkle(kullanici,ogrenci,ders):
    sorgu="""INSERT INTO ogrenci_data (teacher_id,student_id, ders_id)
            VALUES("""+str(kullanici)+", "+str(ogrenci)+", "+str(ders)+"); "
    sonuc=sorgula(sorgu)
    return sonuc

def ogrenciyiDerstenCikar(kullanici,ogrenci,ders):
    sorgu="""DELETE FROM ogrenci_data WHERE ders_id="""+str(ders)+"""
        AND student_id="""+str(ogrenci)
    sonuc=sorgula(sorgu)
    return sonuc


def okStudentGiris(ogrenciNo,sifre):
    sorgu='SELECT * FROM student WHERE ogrenci_no = \''+ogrenciNo+'\' AND sifre = \''+sifre+'\''
    sonuc=sorgula(sorgu)
    return sonuc