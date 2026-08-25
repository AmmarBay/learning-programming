import matematika

hasil1 = matematika.tambah(10, 5)
hasil2 = matematika.kurang(10, 5)
hasil3 = matematika.kali(10, 5)

print(f"Hasil dari 10 + 5 adalah {hasil1}")
print(f"Hasil dari 10 - 5 adalah {hasil2}")
print(f"Hasil dari 10 * 5 adalah {hasil3}")

import konversi
celcius = 25
fahrenheit = konversi.celcius_ke_fahrenheit(celcius)
kelvin = konversi.celcius_ke_kelvin(celcius)
print(f"\n{celcius} derajat Celcius sama dengan {fahrenheit} derajat Fahrenheit")
print(f"{celcius} derajat Celcius sama dengan {kelvin} derajat Kelvin")

import hitung
sisi = 5
panjang = 10
lebar = 4
alas = 8
tinggi = 6

luas_persegi = hitung.luas_persegi(sisi)
luas_persegi_panjang = hitung.luas_persegi_panjang(panjang, lebar)
luas_segitiga = hitung.luas_segitiga(alas, tinggi)

print(f"\nLuas persegi dengan sisi {sisi} adalah {luas_persegi}")
print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas_persegi_panjang}")
print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga}")