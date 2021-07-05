import sqlite3
#sqlite ' ı import ettik.

vt = sqlite3.connect('vtt.sqlite')
# vtt.sqlite isimli yeni bir veritabanı dosyası oluşturalım (veya varolan bir veritabanı dosyasına bağlanalım) .


im = vt.cursor()
#Veritabanını oluşturduktan veya varolan bir veritabanı ile bağlantı kurduktan sonra, veritabanı üzerinde işlem yapabilmek için sonraki adımda bir imleç oluşturmamız gerekir.
#İmleç oluşturmak için cursor() adlı bir metottan yararlanacağız.


im.execute("""SELECT * FROM faturalar""")
# SELECT adlı SQL komutu yardımıyla bu verileri seçtik.

im.fetchmany(5)
#Bu metot, bir veritabanından seçtiğiniz verilerin istediğiniz kadarını alabilmenize imkan tanır.
veriler = im.fetchall()
#fetchall() metodu ise seçilen bu verileri alma işlevi görüyor. Yukarıda biz fetchall() metoduyla aldığımız bütün verileri veriler adlı bir değişkene atadık.
print(veriler)
# verileri yazdırdık.
