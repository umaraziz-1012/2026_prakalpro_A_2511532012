# Name : Umar Abdul Aziz
# Nim  : 2511532012
# Question 6 

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

full_name = "Umar Abdul Aziz"
nim = "2511532012"

name = full_name.strip()
spasi = name.find(" ")

if spasi == -1:
    first_name = name
else:
    first_name = name[:spasi]

username = first_name.lower() + nim[-3:]

print (username)
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
