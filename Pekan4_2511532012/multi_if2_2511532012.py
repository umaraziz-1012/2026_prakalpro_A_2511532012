total_belanja_2012 = float(input("Masukkan total belanja (Rp): "))

input_member_2012 = input("Apakah Anda member? (y/n): ").strip().lower()
is_member_2012 = input_member_2012 in ['y', "ya"]

input_promo_2012 = input("Apakah kode promo valid? (y/n): ").strip().lower()
kode_promo_valid_2012 = input_promo_2012 in ["y", "ya"]

total_diskon_persen_2012 = 0

if total_belanja_2012 > 100000:
    total_diskon_persen_2012 += 10

if is_member_2012:
    total_diskon_persen_2012 += 5
    
if kode_promo_valid_2012:
    total_diskon_persen_2012 += 15
    
nominal_diskon_2012 = total_belanja_2012 * (total_diskon_persen_2012 / 100)
total_bayar_2012 = total_belanja_2012 - nominal_diskon_2012

print("\n--- [ RINCIAN PEMBAYARAN ] ---")
print(f"Total Diskon : {total_diskon_persen_2012}% (Rp{nominal_diskon_2012:,.0f})")
print(f"Total Bayar  : Rp{total_bayar_2012:,.0f}")

print(f"Total diskon yang anda dapatkan: Rp{total_diskon_persen_2012}%")