umur_2012 = int(input("Masukkan Umur Anda : "))
sim_2012 = input("Apakah Anda Sudah memiliki SIM (y/n) : ")[0]

if umur_2012 >= 17 and sim_2012 =='y':
	print("anda sudah dewasa dan boleh bawak motor")
	
elif umur_2012 >= 17 and sim_2012 !='y':
    print("anda sudah dewasa tapi tidak boleh bawak motor")

elif umur_2012 < 17 and sim_2012 =='y':
      print("Umur Belum Cukup Untuk Punya SIM")

else :
      print("Anda Belum Dewasa dan Belum Boleh Bawak Motor")
print("Progeram Selesai")