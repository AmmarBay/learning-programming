nama = ["Ammar", "Budi", "Salwa", "Andi"]
nama[1] = "Rizky"
nama[3] = "Fajar"
nama.append("Doni")
nama.append("Siti")
nama.remove("Doni")
nama.pop(2)

print(nama)
print("Jumlah nama:", len(nama))

print("\nDaftar nama:")
for n in nama:
    print(n)

nilai = [80,85,90,75,95]

total = sum(nilai)
rata_rata = total / len(nilai)

print("\nData nilai:", nilai)
print("Total nilai:", total)
print("Rata-rata nilai:", rata_rata)

if rata_rata >= 75:
    print("Keterangan: Lulus")
else:
    print("Keterangan: Tidak Lulus")

buah = ("apel", "jeruk", "mangga", "pisang")
print("\nDaftar buah:")
for b in buah:
    print(b)

mahasiswa = {
    "nama": "Ammar",
    "umur": 20,
    "jurusan": "Informatika"
}
print("\nData mahasiswa:")
print("Nama:", mahasiswa["nama"])
print("Umur:", mahasiswa["umur"])
print("Jurusan:", mahasiswa["jurusan"])

mahasiswa["umur"] = 21
print("\nUmur mahasiswa setelah diubah:", mahasiswa["umur"])

#set
angka ={1, 2, 3, 3, 4, 4, 5}

print("\nData Set:")
print(angka)

angka.add(6)
print("Set setelah ditambahkan angka 6:", angka)

angka.remove(2)
print("Set setelah dihapus angka 2:", angka)