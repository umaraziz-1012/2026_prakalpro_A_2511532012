tinggi_2012 = int(input("Masukkan tinggi segitiga: "))
for i_2012 in range(1, tinggi_2012 + 1):
    print(" " * (tinggi_2012 - i_2012), end="")
    for j_2012 in range(i_2012):
        if j_2012 == i_2012 - 1:
            print("*", end="")
        else:
            print("* ", end="")
    print()