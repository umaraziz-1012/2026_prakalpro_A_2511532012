from typing import Final
PI: Final = 3.14
print("pi: %f" % PI)
jari_2012 = float(input('Masukkan nilai jari-jari : '))
luas_2012 = PI * jari_2012 * jari_2012
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2012, luas_2012))