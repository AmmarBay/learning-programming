print("=== Kasir Sederhana ===")

barang = []
harga = []
total = 0

while True:
    nama_barang = input("\nMasukkan nama barang (ketik 'exit' untuk keluar): ")
    if nama_barang.lower() == "exit":
        break
    barang.append(nama_barang)

    harga_barang = int(input("Masukkan harga barang: "))
    harga.append(harga_barang)
    total += harga_barang

print("\n=== Struk Pembelian ===")
for i in range(len(barang)):
    print(f"{barang[i]} - Rp {harga[i]}")

print(f"\nTotal: Rp {total}")

if total > 100000:
    diskon = total * 0.1
else:
    diskon = 0

total_setelah_diskon = total - diskon

print(f"Diskon 10%: Rp {diskon}")
print(f"Total setelah diskon: Rp {total_setelah_diskon}")