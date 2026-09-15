print("========================")
print("1. Operator Keanggotaan")
print("========================")

input_data_2012 = input("Massukkan angka pisahkan dengan koma : ")
data_2012 = (int(angka.strip()) for angka in input_data_2012.split(","))

nilai_dicari_2012 = int(input("Massukkan angka yang ingin di cari : "))

hasil_2012 = nilai_dicari_2012 in data_2012
print("\nOperator Keanggotaan IN")
print(nilai_dicari_2012, "in", data_2012, " = ",hasil_2012)

hasil_2012 = nilai_dicari_2012 not in data_2012
print("\nOperator Keanggotaan NOT IN")
print(nilai_dicari_2012, "not in", data_2012, " = ",hasil_2012)

print("========================")
print("2. OPERATOR IDENTITAS")
print("========================")

objek1_2012 = data_2012
objek2_2012 = objek1_2012
objek3_2012 = data_2012.copy()

print("objek1 = ",objek1_2012)
print("objek2 = ",objek2_2012)
print("objek3 = ",objek3_2012)

hasil_2012 = objek1_2012 is objek2_2012
print("\nOperator Identitas IS")
print("objek1 is objek2 = ",hasil_2012)

hasil_2012 = objek1_2012 is not objek2_2012
print("\nOperator Identitas IS NOT")
print("objek1 is objek2 = ",hasil_2012)

print("\nPerbandingan Identitas dan Nilai Objek")
print("Objek1 is objek3 =", objek1_2012 is objek3_2012)
print("Objek1 == objek3 =", objek1_2012 == objek3_2012)

