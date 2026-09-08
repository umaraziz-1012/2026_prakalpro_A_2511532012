#deklarasi variabel
is_lulus = True
is_cumlaude = True

#Menggunakan bolean
nilai = 85
batas_lulus = 75

#Mnentukan nilai bolean dari kondisi
status_kelulusan = nilai >= batas_lulus

print("=== Check Status Kelulusan ===")
print("Nilai:", nilai)
print("apakah lulus?", status_kelulusan)
print("Status Kelulusan:", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat! Anda lulus dengan predikat cumlaude.")