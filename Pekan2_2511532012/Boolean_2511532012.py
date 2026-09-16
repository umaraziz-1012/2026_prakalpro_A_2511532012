#deklarasi variabel
is_lulus_2012 = True
is_cumlaude_2012 = True

#Menggunakan bolean
nilai_2012 = 85
batas_lulus_2012 = 75

#Mnentukan nilai bolean dari kondisi
status_kelulusan = nilai_2012 >= batas_lulus_2012

print("=== Check Status Kelulusan ===")
print("Nilai:", nilai_2012)
print("apakah lulus?", status_kelulusan)
print("Status Kelulusan:", status_kelulusan)
if is_lulus_2012 and is_cumlaude_2012:
    print("Selamat! Anda lulus dengan predikat cumlaude.")