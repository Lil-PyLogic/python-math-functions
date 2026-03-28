import math

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

def hitung_luas_lingkaran(jari_jari):
    
    luas = math.pi * (jari_jari ** 2)
    return luas

hasil_pp = hitung_luas_persegi_panjang(10, 5)
hasil_lingkaran = hitung_luas_lingkaran(7)

print(f"Luas Persegi Panjang: {hasil_pp}")
print(f"Luas Lingkaran: {hasil_lingkaran:.2f}")
