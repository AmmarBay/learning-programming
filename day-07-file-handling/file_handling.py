with open("catatan.txt", "r") as file:
    isi = file.read()

print(isi)

with open("hasil.txt", "w") as file:
    file.write("Ini adalah hasil dari program.\n")
    file.write("Terima kasih telah menggunakan program ini.\n")

with open("hasil.txt", "a") as file:
    file.write("Baris tambahan yang ditambahkan ke file.\n")