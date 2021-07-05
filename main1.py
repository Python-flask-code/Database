import sqlite3
#sqlite ' ı import ettik.
vt = sqlite3.connect("vtt.sqlite")
# vtt.sqlite isimli yeni bir veritabanı dosyası oluşturalım (veya varolan bir veritabanı dosyasına bağlanalım) .

im = vt.cursor()
#Veritabanını oluşturduktan veya varolan bir veritabanı ile bağlantı kurduktan sonra, veritabanı üzerinde işlem yapabilmek için sonraki adımda bir imleç oluşturmamız gerekir.
#İmleç oluşturmak için cursor() adlı bir metottan yararlanacağız.

im.execute("""CREATE TABLE IF NOT EXISTS
    personel (isim, soyisim, sehir, eposta)""")
# imlecin execute() adlı metodunu kullanarak veritabanı içinde bir tablo oluşturalım.

im.execute("""INSERT INTO personel VALUES
    ("Orçun", "Kunek", "Adana", "okunek@gmail.com")""")
# imlecin execute() adlı metodunu kullanarak tablo içine değerleri girelim.


vt.commit()
# Bu girdiğimiz verileri veritabanına işleyebilmek için commit() adlı bir metottan yararlanacağız.
