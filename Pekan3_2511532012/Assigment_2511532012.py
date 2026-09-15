angka1 = int(input("input angka-1 : "))
angka2 = int(input("input angka-2 : "))

print("\nNilai awal angka1 = ", angka1)
print("angka2 = ", angka2)

#Assigment Biasa
hasil_2012 = angka1
print("Assigment Biasa (=)")
print("Hasil = ", hasil_2012)

#Assigment Penjumlahan
hasil_2012 = angka1
hasil_2012 += angka2
print("\nAssigment Penjumlahan (+=)")
print("Hasil = ", hasil_2012)

#Assigment Pengurangan
hasil_2012 = angka1
hasil_2012 -= angka2
print("\nAssigment Pengurangan (-=)")
print("Hasil = ", hasil_2012)

#Assigment Perkalian
hasil_2012 = angka1
hasil_2012 *= angka2
print("\nAssigment Perkalian (*=)")
print("Hasil = ", hasil_2012)

#Assigment pembagian
if angka2 != 0 :
    hasil_2012 = angka1
    hasil_2012 /= angka2    
    print ("\nAssigment pembagian (/=)")
    print ("Hasil = ", hasil_2012)

    hasil_2012 = angka1
    hasil_2012 //= angka2
    print ("\nAssigment pembagian bulat (//=)")
    print ("Hasil = ", hasil_2012)

    hasil_2012 = angka1
    hasil_2012 %= angka2
    print ("\nAssigment sisa bagi (%=)")
    print ("Hasil = " , hasil_2012)
else :
    print("pembagian tidak bisa di lakukan")
    print("angka 2 tidak boleh bernilai 0")

#Assigment Pangkat
hasil_2012 = angka1
hasil_2012 **= angka2
print ("\nAssigment Perpangkatan (**=)")
print ("Hasil = ", hasil_2012)