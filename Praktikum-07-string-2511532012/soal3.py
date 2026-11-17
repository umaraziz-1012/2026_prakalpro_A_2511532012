# Name : Umar Abdul Aziz
# Nim  : 2511532012
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

text = "Umar Abdul Aziz"
text = text.lower()
count = 0
for char in text:
    if char in "aiueo":
        count += 1
print("Vowels:", count)
