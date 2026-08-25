print(" === Hitung Nilai Mahasiswa ===")

import nilai

nilai_mahasiswa = [80, 85, 90, 75, 95]
total_nilai = nilai.hitung_total_nilai(nilai_mahasiswa)
rata_rata_nilai = nilai.hitung_rata_rata_nilai(nilai_mahasiswa)
keterangan = nilai.tentukan_grade(rata_rata_nilai)

print(f"\nNilai Mahasiswa :{nilai_mahasiswa} ")
print(f"Total Nilai     : {total_nilai}")
print(f"Rata-rata Nilai : {rata_rata_nilai}")
print(f"Status          : {keterangan}")