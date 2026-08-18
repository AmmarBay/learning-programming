def tambah(a, b):
    hasil1 = a + b
    return hasil1

def kurang(a, b):
    hasil2 = a - b
    return hasil2

def kali(a, b):
    hasil3 = a * b
    return hasil3

def bagi(a, b):
    if b == 0:
        return "Tidak bisa membagi dengan nol"
    else:
        hasil4 = a / b
        return hasil4

def cek_nilai(nilai):
    if nilai > 100:
        return "Nilai tidak valid"
    elif nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    elif nilai >= 60:
        return "D"
    else:
        return "E"

def cek_status(nilai):
    if nilai >= 60:
        return "Lulus", "Selamat!"
    else:
        return "Tidak Lulus", "Coba lagi!"

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

hasil1 = tambah(angka1, angka2)
hasil2 = kurang(angka1, angka2)
hasil3 = kali(angka1, angka2)
hasil4 = bagi(angka1, angka2)

print("\nHasil Penjumlahan:", hasil1)
print("Hasil Pengurangan:", hasil2)
print("Hasil Perkalian:", hasil3)
print("Hasil Pembagian:", hasil4)

nilai = int(input("\nMasukkan nilai: "))

status, pesan = cek_status(nilai)
print("\nStatus:", status)
print("Pesan:", pesan)

def perkenalan(nama="Ammar", umur=20):
    print("\nHalo, ", nama)
    print("Umur saya adalah ", umur, "tahun")

perkenalan()
perkenalan("Budi")
perkenalan("Salwa", 18)

def biodata(nama, umur, jurusan):
    print("\nNama saya adalah", nama)
    print("Umur saya adalah", umur, "tahun")
    print("Jurusan saya adalah", jurusan)

biodata("Ammar", 20, "Teknik Informatika")

biodata(
    jurusan="Teknik Informatika",
    nama="Ammar",
    umur=20
)

def jumlahkan(*angka):
    total = sum(angka)
    return total

hasil_jumlah = jumlahkan(5, 10, 15, 20, 25)
print("\nJumlah semua angka:", hasil_jumlah)

def biodata(**data):
    print(data)

biodata(nama="Ammar", umur=20, jurusan="Teknik Informatika")

def biodata(**data):
    print("\nNama:", data["nama"])
    print("Umur:", data["umur"])
    print("Jurusan:", data["jurusan"])

biodata(
    nama="Ammar", 
    umur=20, 
    jurusan="Teknik Informatika"
)

def data_mahasiswa(*matkul, **data):
    print("\nNama:", data["nama"])
    print("Jurusan:", data["jurusan"])
    print("Mata Kuliah yang diambil:", matkul)

data_mahasiswa(
    "Python",
    "Basis Data",
    "Jaringan Komputer",
    nama="Ammar",
    jurusan="Teknik Informatika"
)

kali = lambda a, b: a * b
hasil = kali(6, 7)
print("\nHasil perkalian:", hasil)

nama = "Ammar"

def sapa():
    nama = "Budi"
    print("\nNama di dalam fungsi:", nama)
sapa()

print("Nama di luar fungsi:", nama)