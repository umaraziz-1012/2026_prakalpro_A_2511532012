#Masukkan nilai boelan
#input tidak peka terhadap huruf besar dan kecil
a1 = input("input nilai boolean-1 (True/False) : ").strip().lower() == "true"
a2 = input("input nilai boolean-2 (True/False) : ").strip().lower() == "true"

print("\nA1 = ", a1)
print("A2 = ", a2)

#Konjungsi bernilai true jika keduanya true
hasil_2012 = a1 and a2
print("\nOperator Konjungsi (AND)")
print("A1 and A2 = ", hasil_2012)

#Konjungsi bernilai true jika salah satu true
hasil_2012 = a1 or a2   
print("\nOperator Disjungsi (OR)")
print("A1 or A2 = ", hasil_2012)

#Negasi A1 : Membalik nilai A1
hasil_2012 = not a1
print("\nOperator Negasi A1 (NOT)")
print("not A1 = ", hasil_2012)

#Negasi A2 : Membalik nilai A2
hasil_2012 = not a2
print("\nOperator Negasi A2 (NOT)")
print("not A2 = ", hasil_2012)

#XOR : Bernilai true jika keduanya berbeda
hasil_2012 = a1 != a2
print("\nOperator XOR")
print("A1 XOR A2 = ", hasil_2012)