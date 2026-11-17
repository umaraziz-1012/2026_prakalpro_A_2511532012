# Name : Umar Abdul Aziz
# Nim  : 2511532012
# Question 5

username = input("Username: ")

if ((len(username)) < 5):
    print("Invalid: at least 5 characters")

elif(not username.isalnum()):
    print("Invalid: letters and digits only")

elif(not username[0].isalpha()):
    print("Invalid: must start with a letter")
    
else:
    print("Valid")

Nim = "2511532012"
if ((len(Nim)) == 9):
    print("Invalid NIM")
else:
    print(Nim[:-2])
    print("Year 20" + Nim[-2:])