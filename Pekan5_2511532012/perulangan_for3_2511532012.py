ulang_2012 = int(input("Massukkan jumlah perulangan : "))

jumlah_2012 = 0
for i_2012 in range(1, ulang_2012+1):
    print(i_2012, end=" ")
    jumlah_2012 = jumlah_2012 + i_2012

    if i_2012 < ulang_2012:
        print(" + ", end=" ")
    else:
        print(" = ", jumlah_2012,end=" ")
print()
print("jumlah", jumlah_2012)