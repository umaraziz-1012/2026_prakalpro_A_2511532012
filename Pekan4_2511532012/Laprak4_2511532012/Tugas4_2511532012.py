print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_2012 = input("Masukkan Nama Pengunjung : ")
umur_2012 = int(input("Masukkan Umur : "))
sim_2012 = input("Memilikii SIM C (y/n) : ").strip().lower()[0]


print(""" 
== Paket Wahana ==
    1. Safari Rimba         (Rp 50,000)
    2. Arung Jeram          (Rp 75,000)
    3. Motor ATV Ekstrim    (Rp 120,000)
    4. Roller Coaster Kilat (Rp 100,000)
    5. All-Access VIP       (Rp 220,000) """)
pilihan_2012 = int(input("Pilihan Paket Wahana (1-5) : "))
match pilihan_2012:
    case 1:
        print("Wahana Safari Rimba | Harga Satuan: Rp 50.000")
        harga_2012 = 50.000
    case 2:
        print("Wahana Arung Jeram | Harga Satuan: Rp 75.000")
        harga_2012 = 75.000
    case 3:
        print("Wahana Motor ATV Ekstrim | Harga Satuan: Rp 120.000")
        harga_2012 = 120.000
    case 4:
        print("Wahana Roller Coaster Kilat | Harga Satuan: Rp 100.000")
        harga_2012 = 100.000
    case 5:
        print("Wahana All-Access VIP | Harga Satuan: Rp 220.000")
        harga_2012 = 220.000
    case _:
        print("Paket wahana tidak valid!")    
        exit()

jumlah_2012 = int(input("Total Tiket Yang Di beli : "))
if jumlah_2012 <= 0 :
    print("KUOTA TIDAK VALID !!")

member_2012 = input("Apakah Anda Member (y/n) : ")
is_member_2012 = member_2012 in ['y', "ya"]
promo_2012 = input("Apakah Kode Promo Valid (y/n) : ")
kode_promo_valid_2012 = promo_2012 in ["y", "ya"]

print("--- KELAYAKAN PENGENDARA WAHANA ---")
if umur_2012 >= 17 and sim_2012 =='y':
	print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif umur_2012 >= 17 and sim_2012 !='y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)")
elif umur_2012 < 17 and sim_2012 =='y':
    print("Identitas tidak valid: Belum cukup umur memiliki SIM.")
else :
    print("Anda belum cukup umur dan tidak boleh bawa motor ATV.")

total_diskon_2012 = 0
total_2012 = jumlah_2012 * harga_2012
if total_2012 >= 200000:
    total_diskon_2012 += 10
if is_member_2012:
    total_diskon_2012 += 5
if kode_promo_valid_2012:
    total_diskon_2012 +=15
if jumlah_2012 >= 5:
    total_diskon_2012 += 5

nominal_diskon_2012 = total_2012 * (total_diskon_2012 / 100)
total_bayar_2012 = total_2012 - nominal_diskon_2012


print("--- RINCIAN PEMBAYARAN ---")
print(f"Subtotal Belanja : Rp {total_2012:,.0f}")
print(f"Total Diskon : {total_diskon_2012}% (Rp{nominal_diskon_2012:,.0f})")
print(f"Total Bayar  : Rp{total_bayar_2012:,.0f}")
if total_bayar_2012 > 300000:
    print("Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else :
    print("Catatan Layanan  : Terima kasih telah berkunjung.")
print("Program Selesai")