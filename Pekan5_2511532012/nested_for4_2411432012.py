tinggi_2012 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2012 % 2 != 0:
    print("Tinggi harus bilangan genap")
else:
    a_2012 = tinggi_2012
    c_2012 = a_2012
    lebar_2012 = (2 * tinggi_2012) - 2
    
    for i_2012 in range(1, tinggi_2012 + 1):
        b_2012 = c_2012 + 1
        
        for j_2012 in range(1, lebar_2012+1):
            
            if i_2012 == 1 or i_2012 == tinggi_2012:
                if j_2012 == 1 or j_2012 == lebar_2012:
                    print("#", end="")
                else:
                    print("=", end="")
            else: 
                if j_2012 == 1 or j_2012 == lebar_2012:
                    print("|", end="")
                else:
                    if j_2012 == c_2012:
                        print("<", end="")
                    elif j_2012 == b_2012:
                        print(">", end="")
                    elif j_2012 == (lebar_2012 - c_2012):
                        print("<", end="")
                    elif j_2012 == (lebar_2012 - c_2012 + 1):
                        print(">", end="")
                    elif j_2012 > b_2012 and j_2012 < (lebar_2012 - c_2012):
                        print(".", end="")
                    else:
                        print(" ", end="")
                        
        print()
            
        a_2012 -= 2
        
        if a_2012 <= 0:
            c_2012 = (-a_2012) + 2
        else:
            c_2012 = a_2012