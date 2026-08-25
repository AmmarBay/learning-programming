def hitung_total_nilai(nilai):
    total = sum(nilai)
    return total

def hitung_rata_rata_nilai(nilai):
    total = hitung_total_nilai(nilai)
    rata_rata = total / len(nilai)
    return rata_rata

def tentukan_grade(rata_rata):
    if rata_rata >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"