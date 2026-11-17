# Name : Umar Abdul Aziz
# Nim  : 2511532012
# Question 7 

name = "Umar Abdul Aziz"
nim = "2511532012"

name = name.strip()
spasi = name.find(" ")

if spasi == -1:
    first_name = name
else:
    first_name = name[:spasi]

username = first_name.lower() + nim[-3:]

intake = "20" + nim[:2] 

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)

print(f"{'Name':<10}: {name.title()}")
print(f"{'Nim':<10}: {nim}")
print(f"{'UserName':<10}: {username}")
print(f"{'Intake':<10}: {intake}")

print("=" * 30)