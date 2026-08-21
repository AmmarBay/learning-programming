print("Angka 1 sampai 10:")
for i in range(1, 11):
    print(i)

angka = 1
while angka <= 5:
    print("\nangka:", angka)
    angka += 1

for i in range(1, 6):
    if i == 3:
        print("Angka 3 ditemukan!")
        break
    print("\nAngka:", i)

for i in range(1, 6):
    if i == 3:
        print("Angka 3 dilewati!")
        continue
    print("\nAngka:", i)

while True:
    nama = input("\nMasukkan nama Anda (ketik 'exit' untuk keluar): ")
    if nama.lower() == "exit":
        print("Program selesai.")
        break
    print("Halo,", nama, "! Selamat datang di program ini.")

nama = []

while True:
    data = input("\nMasukkan nama (ketik 'exit' untuk keluar): ")
    if data == "exit":
        print("Program selesai.")
        break
    nama.append(data)
print("\nDaftar nama yang dimasukkan:")

for n in nama:
    print(n)