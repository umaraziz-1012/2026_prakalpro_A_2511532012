ukuran_2012 = int(input("Masukkan Ukuran: "))

print("#" + "=" * (4 * ukuran_2012 + 5) + "#")

for baris_2012 in range(ukuran_2012, 0, -1):
    print("| ", end="")
    print(" " * (2 * (ukuran_2012 - baris_2012)), end="")

    for angka_2012 in range(baris_2012, 0, -1):
        print(angka_2012, end=" ")
    print("<*>", end="")

    for angka_2012 in range(1, baris_2012 + 1):
        print(" " + str(angka_2012), end="")
    print(" " * (2 * (ukuran_2012 - baris_2012)), end="")
    print(" |")

print("| " + " " * (2 * ukuran_2012 + 1) + "<*>" + " " * (2 * ukuran_2012 + 1) + " |")

for baris_2012 in range(1, ukuran_2012 + 1):
    print("| ", end="")
    print(" " * (2 * (ukuran_2012 - baris_2012)), end="")
    for angka_2012 in range(baris_2012, 0, -1):
        print(angka_2012, end=" ")
    print("<*>", end="")

    for angka_2012 in range(1, baris_2012 + 1):
        print(" " + str(angka_2012), end="")
    print(" " * (2 * (ukuran_2012 - baris_2012)), end="")
    print(" |")

print("#" + "=" * (4 * ukuran_2012 + 5) + "#")