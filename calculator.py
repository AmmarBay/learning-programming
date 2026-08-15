nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
kota = input("Masukkan nama kota: ")

print("Halo,", nama, "dengan umur", umur, "dari kota", kota)
print("Selamat Datang di Calculator CLI")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

print("===== CALCULATOR CLI =====")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Sisa bagi")
print("6. Pangkat")

pilihan = input("Pilih operasi (1-6): ")

#print("Hasil: ")
#print("Penjumlahan : ", a + b)
#print("Pengurangan : ", a - b)
#print("Perkalian : ", a * b)
#print("Pangkat : ", a ** b)

#if b == 0:
#    print("Angka yang anda masukkan tidak bisa dibagi")
#else:
#    print("Pembagian : ", a / b)
 #   print("Sisa bagi : ", a % b)

#if a > b:
#    print("Angka pertama lebih besar")
#elif a < b:
#    print("Angka kedua lebih besar ")
#else:
#    print("Kedua angka sama")

if pilihan == "1":
    print("Penjumlahan : ", a + b)
elif pilihan == "2":
    print("Pengurangan : ", a - b)
elif pilihan == "3":
    print("Perkalian : ", a * b)
elif pilihan == "4":
    if a == 0 or b == 0:
        print("Angka yang anda masukkan tidak boleh 0 untuk pembagian")
    else:
        print("Pembagian : ", a / b)
elif pilihan == "5":
    if a == 0 or b == 0:
        print("Angka yang anda masukkan tidak boleh 0 untuk sisa bagi")
    else:
        print("sisa bagi : ", a % b)
elif pilihan == "6":
    print("Pangkat : ", a ** b)
else:
    print("Pilihan tidak tersedia")