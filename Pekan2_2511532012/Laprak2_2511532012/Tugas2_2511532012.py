alamat_2012 = """
Kampus Unanad
kec.pauh
Kota Padang"""

token_2012 = 100+3j

lulus_2012 = True
batas_2012 = 75.0

print("=== SISTEM REGISTRASI PRAKTIKUM ALPRO 2026 ===")
nama_2012 = input("Masukkan Nama Mahasiswa : ")
kelamin_2012 = input("Masukkan Jenis Kelamin (L/P) : ")
umur_2012 = input("Masukkan Umur : ")
skor_2012 = int(input("Masukkan Skor Tes Awal : "))

print("=== DATA PRAKTIKUM DAN HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_2012 )
print("Jenis Kelamin : ",kelamin_2012)
print("Alamat Domisili : ",alamat_2012)
print("Umur : ",umur_2012)
print("Skor Awal Tes : ",skor_2012)
print("ID Token Sinyal : ",token_2012)

lulusan_2012 = skor_2012 >= batas_2012

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai : ",batas_2012)
print("Apakah Dinyatakan Lulus : ", lulus_2012)