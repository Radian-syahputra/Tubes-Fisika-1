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
        print(simbol)
    return hasil

waktu : dict[str, int] = {"M": 0, "L": 0, "T": 1, "I": 0, "Θ": 0, "N": 0, "J": 0}

print("Pembagian")
print(bagi(kecepatan, waktu))
