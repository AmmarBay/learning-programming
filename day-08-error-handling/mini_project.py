print("==== Kalkulator Pembagian ====")

try:
    angka_pertama = int(input("Masukkan angka pertama: "))
    angka_kedua = int(input("Masukkan angka kedua: "))
    hasil = angka_pertama / angka_kedua
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
except ZeroDivisionError:
    print("Terjadi kesalahan: Pembagian dengan nol tidak diperbolehkan.")
else:
    print(f"Hasil pembagian {angka_pertama} / {angka_kedua} = {hasil}")
finally:
    print("Terima kasih telah menggunakan kalkulator pembagian.")