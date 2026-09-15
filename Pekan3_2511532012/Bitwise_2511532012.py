print("========================")
print("3. OPERATOR BITWISE")
print("========================")

angka1_2012 = int(input("Massukkan angka bitwise-1 : "))
angka2_2012 = int(input("Massukkan angka bitwise-2 : "))

print("\n angka dalam bentuk desimal dan biner")
print("angka1 =", angka1_2012, "| biner =", bin(angka1_2012))
print("angka2 =", angka2_2012, "| biner =", bin(angka2_2012))

#Bitwise AND
hasil_2012 = angka1_2012 & angka2_2012
print("\nBitwise AND (&)")
print(angka1_2012, " & ", angka2_2012, "=", hasil_2012)
print("Biner Hasil = ",bin(hasil_2012))
print("Biner Hasil (8 Bit) = ", format(hasil_2012, "08b"))

#Bitwise XOR
hasil_2012 = angka1_2012 ^ angka1_2012
print("\nBitwise XOR (^)")
print(angka1_2012, " ^ ", angka2_2012, " = ", hasil_2012)
print("Biner Hasil = ", bin(hasil_2012))
print("Biner Hasil (8 Bit) = ", format(hasil_2012, "08b"))

#Bitwise Geser Kiri
jumlah_geser_2012 = int(input("\nMasukkan jumlah pergeseran bit : "))

hasil_2012 = angka1_2012 << jumlah_geser_2012
print("\nBitwise geser kiri (<<)")
print(angka1_2012, " << ", jumlah_geser_2012, " = ", hasil_2012)
print("Biner Hasil = ", bin(hasil_2012))
print("Biner Hasil (8 Bit) = ", format(hasil_2012, "08b"))

hasil_2012 = angka1_2012 >> jumlah_geser_2012
print("\nBitwise geser kanan (>>)")
print(angka1_2012, " >> ", jumlah_geser_2012, " = ", hasil_2012)
print("Biner Hasil = ", bin(hasil_2012))
print("Biner Hasil (8 Bit) = ", format(hasil_2012, "08b"))
