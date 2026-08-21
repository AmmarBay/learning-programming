nama = "Ammar"
jurusan = "Teknik Informatika"

print("Nama:", nama)
print("Jurusan:", jurusan)

print("\nNama huruf besar:", nama.upper())
print("Nama huruf kecil:", nama.lower())
print("Nama dengan huruf besar di awal:", nama.title())

print ("\nPanjang nama:", len(nama))
print("Panjang jurusan:", len(jurusan))

print("\nIndexing:")
print("Huruf pertama nama:", nama[0])
print("Huruf kedua nama:", nama[1])
print("Huruf terakhir nama:", nama[-1])

print("\nSlicing:")
print("Huruf pertama sampai ketiga nama:", nama[0:3])
print("Huruf kedua terakhir nama:", nama[-2:])
print("Nama tanpa huruf terakhir:", nama[:-1])

teks = "  Saya belajar Python  "

print("\nHapus spasi di awal dan akhir:", teks.strip())
print("Ganti kata 'Python' dengan 'Java':", teks.replace("Python", "Java"))
print("Pisahkan kata-kata:", teks.split())
print("Cek apakah 'Python' ada dalam teks:", "Python" in teks)