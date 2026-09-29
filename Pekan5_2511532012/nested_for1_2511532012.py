batas_2012 =  int(input("Masukkan Nilai Batas : "))
for line_2012 in range(1, batas_2012 + 1):
    for j in range(1,(-1 * line_2012 + batas_2012)+1):
        print(".", end=" ")
    print(line_2012)
