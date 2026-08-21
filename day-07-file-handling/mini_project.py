print("=== CATATAN BELAJAR ===")

catatan = input("Masukkan catatan Anda: ")
with open("catatan_belajar.txt", "a") as file:
    file.write(catatan + "\n")

print("\nCatatan berhasil disimpan ke file 'catatan_belajar.txt'.")

print("\n=== ISI CATATAN BELAJAR ===")
with open("catatan_belajar.txt", "r") as file:
    isi = file.read()
print(isi)