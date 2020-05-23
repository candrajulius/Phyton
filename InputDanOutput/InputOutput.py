import sys

print("Number of argument: ", len(sys.argv), "arguments")
print("Argument List: ",str(sys.argv))
print(sys.argv[1])

print("Candra Julius Sinaga") # Input yang sederhana
 # Input yang menggunakan format string
Nama = "Candra Julius Sinaga"
#Cara pertama dengan menggabungkan nama variabel
print("Nama saya adalaha Candra Julius Sinaga")
print("Nama saya adalah ",Nama) # Cara pertama dengan menggabungkan variabel
print("nama saya adalah " + Nama) # Menggunakan cencottenasi atau penggabungan string dengan menggunakan tanda "+"
print("Nama saya adalah , %s" %Nama) # Menggunakan string format
nama1 = "candra"
umur = 20
lahir = "Medan"
print("nama saya adalah %s dan umur saya %d lahir saya %s " %(nama1,umur,lahir)) # Menggunakan string format
# %s - String
# %d - Integers
# %f - Bilangan Pecahan
# %.<digit>f - Bilangan pecahan dengan sejumlah digit angka dibelakang koma.
# %x/%X - Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)

# Contoh dari hexa
a,b  = 10,11
print(a,b)
print("a: %x dan b : %X" %(a,b))

 # Contoh dari input
 # Untuk memungkinkan user memberikan input pada program Anda, gunakan fungsi input(), dengan argumen dalam kurung () adalah
# teks yang ingin ditampilkan (prompt) dan variabel sebelum tanda sama dengan (=) adalah penampung hasil dari input pengguna:

num = input("Masukkan nomor anda : ")
print(float(num)) # mengkonversi kan sebuah inputan dari user ke float
print(int(num)) # mengkonversikan sebuah inputan dari user ke int
print(str(num)) # mengkonversikan sebuah inputan dari user ke string
# print(chr(num)) # mengkonversikan sebuah inputan dari user ke character

nama = input("Masukkan nama kamu = ")
print(str(nama))
# perkalian = input("2 + 3  = " )
# print(int("2+3"))
print(eval("10 + 12 ")) # fungsi eval berfungsi untuk menyelesaikan expresi matematika

