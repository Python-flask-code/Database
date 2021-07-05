import sqlite3
#sqlite ' ı import ettik.

vt = sqlite3.connect('vtt.sqlite')
# vtt.sqlite isimli yeni bir veritabanı dosyası oluşturalım (veya varolan bir veritabanı dosyasına bağlanalım) .


im = vt.cursor()
#Veritabanını oluşturduktan veya varolan bir veritabanı ile bağlantı kurduktan sonra, veritabanı üzerinde işlem yapabilmek için sonraki adımda bir imleç oluşturmamız gerekir.
#İmleç oluşturmak için cursor() adlı bir metottan yararlanacağız.


im.execute("""CREATE TABLE IF NOT EXISTS faturalar
(fatura, miktar, ilk_odeme_tarihi, son_odeme_tarihi)""")
# imlecin execute() adlı metodunu kullanarak veritabanı içinde bir tablo oluşturalım.

im.execute("""INSERT INTO faturalar VALUES
("Elektrik", 45, "23 Ocak 2010", "30 Ocak 2010")""")
# imlecin execute() adlı metodunu kullanarak tablo içine değerleri girelim.
vt.commit()
# Bu girdiğimiz verileri veritabanına işleyebilmek için commit() adlı bir metottan yararlanacağız.

im.execute("""SELECT * FROM faturalar""")
# SELECT adlı SQL komutu yardımıyla bu verileri seçtik.

veriler = im.fetchall()
#fetchall() metodu ise seçilen bu verileri alma işlevi görüyor. Yukarıda biz fetchall() metoduyla aldığımız bütün verileri veriler adlı bir değişkene atadık.
print(veriler)
# verileri yazdırdık.