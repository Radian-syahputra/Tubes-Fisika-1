DIMENSI_DASAR : list[str] = ["M", "L", "T", "I", "Θ", "N", "J"]
kecepatan : dict[str, int] = {
    "M" : 0,
    "L" : 1,
    "T" : -1,
    "I" : 0,
    "Θ" : 0,
    "N" : 0,
    "J" : 0
}

def buat_dimensi(M : int = 0, L : int = 0, T : int = 0, I : int = 0, theta : int = 0, N : int = 0, J : int = 0) -> dict[str, int] :
    return {"M": M, "L": L, "T": T, "I": I, "Θ": theta, "N": N, "J": J}

kecepatan_baru : dict[str, int] = buat_dimensi(L=1, T=-1)
print("Kecepatan Baru")
print(kecepatan_baru)

def kali(a : dict[str, int], b :dict[str, int]) -> dict[str, int] :
    hasil : dict[str, int] = {}
    for simbol in DIMENSI_DASAR :
        hasil[simbol] = a[simbol] + b[simbol]
    return hasil

massa: dict[str, int] = {"M": 1, "L": 0, "T": 0, "I": 0, "Θ": 0, "N": 0, "J": 0}
percepatan: dict[str, int] = {"M": 0, "L": 1, "T": -2, "I": 0, "Θ": 0, "N": 0, "J": 0}

print("Perkalian ")
print(kali(massa, percepatan))

# Dimensi Gaya : M¹·L¹·T⁻².

def bagi (a : dict[str, int], b: dict[str, int]) -> dict[str, int] :
    hasil : dict[str, int] = {}
    for simbol in DIMENSI_DASAR :
        hasil[simbol] = a[simbol] - b[simbol]
    return hasil

waktu : dict[str, int] = {"M": 0, "L": 0, "T": 1, "I": 0, "Θ": 0, "N": 0, "J": 0}

print("Pembagian")
print(bagi(kecepatan, waktu))

def pangkat(a : dict[str, int], n : int ) -> dict[str, int]:
    hasil : dict[str, int] = {}
    for simbol in DIMENSI_DASAR :
        hasil[simbol] = a[simbol] * n
    return hasil


panjang : dict[str, int] = {"M": 0, "L": 1, "T": 0, "I": 0, "Θ": 0, "N": 0, "J": 0}
print("Pangkat")
print(pangkat(panjang, 2))
         
# Volume
print("Volume")
print(pangkat(panjang, 3))

# Energi Kinetik
print("Energi")
print(kali(massa, pangkat(kecepatan, 2)))