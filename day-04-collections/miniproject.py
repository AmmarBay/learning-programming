#Mini project: Collections

mahasiswa = {
    "nama": "Ammar",
    "jurusan": "Informatika",
    "nilai": [80, 85, 90, 75, 95]
}

#Menghitung nilai
nilai = mahasiswa["nilai"]
total = sum(nilai)
rata_rata = total / len(nilai)

#Menampilkan data mahasiswa
print("=== Data Mahasiswa ===")
print("Nama:", mahasiswa["nama"])
print("Jurusan:", mahasiswa["jurusan"])

print("=== Daftar Nilai ===")

for n in nilai:
    print(n)

print("\nTotal Nilai:", total)
print("Rata-rata Nilai:", rata_rata)

#Menentukan keterangan kelulusan
if rata_rata >= 75:
    print("Keterangan: Lulus")
else:
    print("Keterangan: Tidak Lulus")

#Set untuk mata kuliah yang diambil
mata_kuliah ={"Python", "Basis Data", "Algoritma", "Struktur Data"}

print("\n=== Mata Kuliah ===")
print(mata_kuliah)