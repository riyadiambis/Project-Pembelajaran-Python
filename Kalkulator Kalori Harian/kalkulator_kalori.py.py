print("""
1. Pria
2. Wanita
""")
opsi_kelamin = int(input("Silahkan pilih opsi(1/2): "))
berat_badan = float(input("Masukkan berat badan Anda (Kg): "))
tinggi_badan = int(input("Masukkan tinggi badan Anda (cm): "))
umur = int(input("Masukkan umur Anda: "))

print("""
1. Aktivitas Minimal
2. Aktivitas Sedang
3. Aktivitas Tinggi
""")
opsi_aktivitas = int(input("Silahkan pilih opsi(1/2/3) : "))
match opsi_aktivitas:
    case "1":
        opsi_aktivitas = 1.25
    case "2":
        opsi_aktivitas = 1.36
    case "3":
        opsi_aktivitas = 1.72
    case _:
        print("Input tidak valid")

level_aktivitas = opsi_aktivitas


if opsi_kelamin == 1 or opsi1_kelamin == 2:
    if opsi_kelamin == 1:
        BMR = (10 * berat_badan) + (6.25 * tinggi_badan) - (5 * umur) + 5
    else:
        BMR = (10 * berat_badan) + (6.25 * tinggi_badan) - (5 * umur) - 161
else:
    print("Anda memasukkan angka yang salah")



Kalori_harian = level_aktivitas * BMR

print(f"Kalori harian Anda adalah : {Kalori_harian}")



