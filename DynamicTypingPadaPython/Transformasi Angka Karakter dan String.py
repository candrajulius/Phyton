# Misalnya untuk nomor nota atau nomor antrian, Anda akan menemui kebutuhan menambahkan awalan 0
# (0001 untuk angka 1, 0101 untuk angka 101, dan sebagainya).
# Anda dapat menggunakan fungsi zfill(). Catatannya adalah angka harus dikonversi ke string terlebih dahulu:

x = 1
print(type(x))

x = 0.123
print(str(x).zfill(4))

# Transformasi karakter dan String dan karakter
# upper untuk membuat string menjadi huruf besar
# lower untuk membuat string menjadi huruf kecil

p = 'Candra Julius Sinaga'
print(p.upper()) # menggunakan upeprcase huruf besar
print(p.lower()) # menggunakan lowercase huruf kecil
print(p.isupper()) # menegecek apakah ada huruf kecil pada variabel
print(p.islower()) # mengecek apakah ada huruf besar pada variabel
print("\n")
# bisa menggunakan kata langsung tidak menggunakan variabel
print('1234'.islower())
print('candra julius sinaga'.islower())
print("CANDRA JULIUS SINAGA".isupper())

# isalpha() mengembalikan True jika string berisi hanya huruf dan tidak kosong.
# isalnum() mengembalikan True jika string berisi hanya huruf atau angka, dan tidak kosong.
# isdecimal() mengembalikan True jika string berisi hanya angka/numerik dan tidak kosong.
# isspace() mengembalikan True jika string berisi hanya spasi, tab, newline, atau whitespaces lainnya dan tidak kosong.
# istitle() mengembalikan True jika string berisi kata yang diawali huruf kapital dan dilanjutkan dengan huruf kecil seterusnya.
 # Contoh
print('hello'.isalpha())
print('1234'.isalpha())
print('1234'.isdecimal())

print('candra julius sinaga'.isalnum(),'Candra'.istitle(),'1234 '.isspace())

# Membuat sebuah perulangan boolean
while True:
    print("Masukkan Umur kamu = ")
    candra = input()
    if candra.isdecimal():
        break
    else:
        print("Tolong masukkan sebuah angka untuk umur")
        # while True:
        #     print("Masukkan sebuah passoword baru (Hanya surat dan nomor )")
        #     password = input()
        #     if password.isalnum():
        #         break
        #     else:
        #         print("Password hanya dapat membuat surat dan nomor")
        #         break

#Metode startswith() dan endswith() dari String
 # Fungsi startswith() dan endswith() akan mengembalikan nilai True berdasarkan nilai awalan atau akhiran string. Contohnya sebagai berikut:
print('Hello Kamu'.startswith('Hello'))
print('Candra Julius Sinaga'.endswith("Sinaga"))

# Metode join() dan split() dari String
# Fungsi join() berguna saat Anda memiliki sejumlah string yang perlu digabungkan. Contohnya sebagai berikut:
print(','.join(['kucing','Tikus','Kelelawar']))
print(' '.join(['My','name', 'is', 'Candra']))
print('ABC'.join(["Candra","Bangsat","Siapa"]))


print('My name is candra'.split('name'))
print('CandraABCBangsatABCSiapa'.split('ABC'))
    
# Teks rata kanan/kiri/tengah dengan rjust(), ljust(), dan center()
# Anda dapat merapikan pencetakan teks di layar dengan rjust(), ljust() atau center(). rjust() dan ljust() akan menambahkan spasi pada string untuk membuatnya sesuai (misalnya rata kiri atau rata kanan). 
# Argumennya berupa integer yang merupakan panjang teks secara keseluruhan (bukan jumlah spasi yang ditambahkan):
    
print('Hello'.rjust(10))
print('Candra'.rjust(20))
print('Candra'.rjust(20,'*')) # Membuat rata kanan dan menggantikannya dengan * dengan jarak parameter nilai yang dibuat

# Contohnya: 'Hello'.rjust(10) dapat diartikan sebagai kita ingin menuliskan Hello dalam mode rata kanan dengan total panjang string 10.
# Karena panjang ‘Hello’ adalah 5 karakter, maka 5 spasi akan ditambahkan di sebelah kiri. Selain spasi,
# Anda juga bisa menambahkan karakter lain dengan mengisikan parameter kedua pada fungsi rjust() atau ljust():

print('Hello'.ljust(20,'-')) # Memebuat rata kiri sesuai dengan parameter angka dan menggantikannya dengan -
print('Candra'.center(20,'*'))
# Hapus Whitespace dengan strip(), rstrip(), dan lstrip()
# Saat Anda menerima string sebagai parameter, seringkali masih terdapat karakter whitespace (spasi, tab, dan newline) di bagian awal dan atau akhir string yang dimaksud.
# Metode strip() akan menghapus
# whitespace pada bagian awal atau akhir string. lstrip() dan rstrip() akan menghapus sesuai dengan namanya, awal saja atau akhir saja:

spam = '  Hello Wolrd'
print(spam.strip())
julius = 'SpamSpamBaconSpamEggsSpamSpam'
manusia = "                                 bangsat kali kau "
print(julius.strip('ampS')) # strip berfungsi untuk menghilangkan spasi atau whispasce dan karakter dengan membuat inisisasi
print(manusia.strip()) # Menghilangkan spasi
kamu = str("candra julius sinaga").replace('julius','bangsat') # Menggantikan julius dengan bangsat
print(kamu)
siapa = str("geek of geek geek geek geek").replace("geek","geeksOfGeeks",3) # Membuat parameter 3 dan menggantikannya dengan geekofgeeks samppai 3
print(siapa)