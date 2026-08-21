print("=== PROGRAM PENGOLAH NAMA ===")
nama = input("Masukkan nama Anda: ")

nama = nama.strip()

print("\n=== HASIL PENGOLAHAN NAMA ===")
print("Nama:", nama)
print("Nama huruf besar               :", nama.upper())
print("Nama huruf kecil               :", nama.lower())
print("Nama dengan huruf besar di awal:", nama.title())
print("Panjang nama                   :", len(nama))
print("Huruf pertama nama             :", nama[0])
print("Huruf terakhir nama            :", nama[-1])

if " " in nama:
    print("Nama terdiri dari beberapa kata.")
else:
    print("Nama terdiri dari satu kata.")