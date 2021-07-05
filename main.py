import sqlite3

vt = sqlite3.connect("vtt.sqlite")

im = vt.cursor()
im.execute("""CREATE TABLE IF NOT EXISTS
    personel (isim, soyisim, sehir, eposta)""")

im.execute("""INSERT INTO personel VALUES
    ("Orçun", "Kunek", "Adana", "okunek@gmail.com")""")

vt.commit()