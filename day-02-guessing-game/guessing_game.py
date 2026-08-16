import random

while True:

    angka_rahasia = random.randint(1, 10)
    maks_percobaan = 5
    percobaan = 0

    print("Selamat datang di permainan tebak angka!")
    print("Tebak angka rahasia antara 1 sampai 10.")
    print("Anda memiliki", maks_percobaan, "percobaan untuk menebak angka rahasia.")

    while percobaan < maks_percobaan:
        tebakan = int(input("Tebak angka: "))
        percobaan += 1

        kesempatan = maks_percobaan - percobaan

        if tebakan > angka_rahasia:
            print("Tebakan Anda terlalu tinggi.")
        elif tebakan < angka_rahasia:
            print("Tebakan Anda terlalu rendah.")
        else:
            print("Selamat! Anda menebak angka yang benar.")
            print("Jumlah percobaan:", percobaan)
            break
            
        print("Kesempatan tersisa:", kesempatan)

    else:
        print("Maaf, Anda telah kehabisan percobaan.")
        print("Angka rahasia adalah:", angka_rahasia)
        print("Jumlah percobaan:", percobaan)

    main_lagi = input("Apakah Anda ingin bermain lagi? (ya/tidak): ")

    if main_lagi.lower() != 'ya':
        print("Terima kasih telah bermain! Sampai jumpa.")
        break