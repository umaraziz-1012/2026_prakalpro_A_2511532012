total_belanja_2012 =  float(input("Massukkan Total Belanja : Rp."))

member_2012 = input("Apakah Sudah Member (y/n): ").strip().lower()
is_member_2012 = member_2012 in ["y", "ya"]

promo_2012 = input("Apakah Kode Promo Valid : ").strip().lower()
kode_promo_valid_2012 = promo_2012 in ["y", "ya"]

total_diskon_presen_2012 = 0

if total_belanja_2012 > 100000:
    total_diskon_presen_2012 += 10

if is_member_2012:
    total_diskon_presen_2012 += 5

if kode_promo_valid_2012:
    total_diskon_presen_2012 += 15

nominal_diskon_2012 = total_belanja_2012 * (total_diskon_presen_2012/100)
total_bayar_2012 = total_belanja_2012 - nominal_diskon_2012

print("\n--- RINCIAN PEMBAYARAN ---")
print(f"Total Diskon : {total_diskon_presen_2012}%(RP{nominal_diskon_2012})")
print(f"Total Bayar : Rp{total_bayar_2012:,.0f}")

print(f"Total Diskon Yang Di Dapatkan ; {total_diskon_presen_2012}%")
