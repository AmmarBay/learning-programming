def data_mahasiswa(nama, umur, jurusan):
    print("\n=== Biodata Mahasiswa ===")
    print("Nama:", nama)
    print("Umur:", umur)
    print("Jurusan:", jurusan)

def hitung_nilai(*nilai):
    total = sum(nilai)
    rata_rata = total / len(nilai)

    return total, rata_rata

def cek_status(rata_rata):
    if rata_rata >= 75:
        return "Lulus", "Selamat, Anda lulus!"
    else:
        return "Tidak Lulus", "Maaf, Anda tidak lulus."

data_mahasiswa(
    "Ammar", 
    20, 
    "Teknik Informatika"
)

total, rata_rata = hitung_nilai(80, 85, 90)

print("\n=== Hasil Perhitungan Nilai ===")
print("Total Nilai:", total)
print("Rata-rata Nilai:", rata_rata)

status, pesan = cek_status(rata_rata)

print("\n=== Status Kelulusan ===")
print("Status:", status)
print("Pesan:", pesan)