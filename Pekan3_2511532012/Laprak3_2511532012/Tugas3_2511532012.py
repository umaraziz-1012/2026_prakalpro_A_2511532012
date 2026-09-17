# DATA PELANGGAN DAN TRANSAKSI 
print("=== SISTEM TRANSAKSI TOKO ===")
nama_2012 = input("Nama Pelanggan :")
Status_2012 = input("Status Pelanggan (Member/nonMmeber) : ").strip().lower()== "member"
Belanja_2012 = int(input("Masukkan total belanja : "))
Jumlah_2012 = int(input("Masukkan Jumlah Barang : "))
Kode_2012 = int("Masukkan Kode Promo : ").strip() == "HEMAT10"
Bayar_2012 = int(input("Masukkan total pembayaran : "))
if Bayar_2012 < Belanja_2012 :
    print ("DUIT ANDA KURANG")
else :
    print(" ")
diskon_2012 = Belanja_2012 * 10/100
print("=== DATA TRANSAKSI ===")
print(nama_2012)
print(Status_2012)
print(Belanja_2012)
print(Jumlah_2012)
print(Kode_2012)
print(" ")

print("=== HASIL VALIDASI ===")
bel_2012 = Belanja_2012>=200000
print("Belanja >= 200000 : ",bel_2012)
jum_2012 = Jumlah_2012 >= 3
print("Jumlah Belanja >= 3 : ")
mem_2012 = Status_2012 == "member"
print("Status Member : ",mem_2012)
if Belanja_2012 >=200000 and Jumlah_2012 >= 3 and Status_2012 == "member":
    Belanja_2012 = Belanja_2012 - diskon_2012
    print("Mendapatkan Diskon : True ")
else :
    print("Mendapatkan Diskon : False ")
kod_2012 = Kode_2012 = "HEMAT10"
print("Kode Promo Tresedia : ")
if Kode_2012 =="HEMAT10":
    print("Mendapatkan Promo : True")
else :
    print("Mendapatkan Promo : False")
print(" ")

print("=== HASIL PERHITUNGAN ===")
print("Diskon : Rp 25000")
print("Total Pembayaran : ",Bayar_2012)
print("Harga Setelah Diskon : ",Belanja_2012)
Rata_2012 = Belanja_2012 / Jumlah_2012
print("Rata Rata Harga Barang : ",Jumlah_2012)

print("\n=== HAK AKSES PELANGGAN ===")
Kode_Akses_2012 = 0
if Status_2012:
    Kode_Akses_2012 = Kode_Akses_2012 | 1
if Kode_2012:
    Kode_Akses_2012 = Kode_Akses_2012 | 8
if Belanja_2012 >= 200000 and Jumlah_2012 >= 3:
    Kode_Akses_2012 = Kode_Akses_2012 | 4
print("Kode Hak Akses          :", format(Kode_Akses_2012, "04b"))
Member_Access_2012 = (Kode_Akses_2012 & 1) != 0
Promo_Access_2012 = (Kode_Akses_2012 & 8) != 0
Free_Shipping_2012 = (Kode_Akses_2012 & 4) != 0
print("Member Access            :", Member_Access_2012)
print("Promo Access             :", Promo_Access_2012)
print("Free Shipping Access     :", Free_Shipping_2012)

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
Kode_Transaksi_2012 = 1 | 2 | 4 | 8
print("Kode Biner   :", format(Kode_Transaksi_2012, "04b"))
print("Kode Desimal :", Kode_Transaksi_2012)

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
Hasil_Member_2012 = Kode_Transaksi_2012 & 1
print("1111 & 0001")
print("Hasil Biner   :", format(Hasil_Member_2012, "04b"))
print("Hasil Desimal :", Hasil_Member_2012)
print("\nCek Promo")
Hasil_Promo_2012 = Kode_Transaksi_2012 & 8
print("1111 & 1000")
print("Hasil Biner   :", format(Hasil_Promo_2012, "04b"))
print("Hasil Desimal :", Hasil_Promo_2012)

print("\n=== Perbandingan Status ===")
Kode_Referensi_2012 = 11
Hasil_XOR_2012 = Kode_Transaksi_2012 ^ Kode_Referensi_2012
print("Kode Transaksi :", format(Kode_Transaksi_2012, "04b"))
print("Kode Referensi :", format(Kode_Referensi_2012, "04b"))
print("1111 ^ 1011")
print("Hasil Biner   :", format(Hasil_XOR_2012, "04b"))
print("Hasil Desimal :", Hasil_XOR_2012)

print("\n=== Shift ===")
Hasil_Shift_2012 = Kode_Transaksi_2012 << 1
print("1111 << 1")
print("Hasil Biner   :", format(Hasil_Shift_2012, "05b"))
print("Hasil Desimal :", Hasil_Shift_2012)
print("\n=== SELESAI ===")