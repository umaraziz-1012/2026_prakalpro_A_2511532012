angka1 = int(input("input angka-1 : "))
angka2 = int(input("input angka-2 : "))

#Penjumlahan
hasil_2012 = angka1 + angka2
print("\nOperator Penjumlahan")
print("Hasil = " ,hasil_2012)

#Pengurangan 
hasil_2012 = angka1 - angka2
print("\nOperator Pengurangan")
print("Hasil = ", hasil_2012)

#Perkalian
hasil_2012 = angka1 * angka2
print("\nOperator Perkalian")
print("Hasil = ", hasil_2012)

#Pembagian
if angka2 != 0:
    hasil_2012 = angka1 / angka2
    print("\nOperator Pembagian")
    print("Hasil = ", hasil_2012)

    hasil_2012 = angka1 // angka2
    print("\nOperator Pembagian Bulat")
    print("Hasil = ", hasil_2012)

    hasil_2012 = angka1 % angka2
    print("\nOperator Sisa Bagi")
    print("Hasil = ", hasil_2012)           
else :
    print("Angka kedua tidak boleh bernilai nol")

#Pangkat
hasil_2012  = angka1 ** angka2
print("\nOperator Pangkat")
print("Hasil = ", hasil_2012)
