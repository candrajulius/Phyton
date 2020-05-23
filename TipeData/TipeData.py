
 # Tipe data pada number,float,Integer dan complex
a = 5
b = 8
c = a + b
d = 2.5
e = 1+2j
print(c)
print(e)
l = 'C'
print(l , " = " , type(l))
 # Tipe numerik pada phyton dibagi menjadi 3 yaitu int,float,complex

print(a, "Adalah tipe",type(a))
print(d, "Adalah type ", type(d))
print(e," Adalah complex number? ",isinstance(1+2j,complex))

x= [0] * 10005;
x[1] = 1;

for j in range(2,10001):
    x[j] = x[j-1]+x[j-2]
    print(x[10000])
print("\n")
g = 1234567890123456789
print(g)

# String
s = "Candra Julius Sinaga"
print(s[4])
print(s[0:100])

# List adalah kumpulan data yang terurut
n = [1,2,3,"candra Julius Sinaga",'C'] # membuat sebuah list pada phyton
print(n[-2:]) # membuat list dari pengambilan yang belakang dan sampai pada index ke 0
print("\n")
print(n[-1]) # pengambilan list dari index kebelakang
print("\n")
print(n[:5]) # pengambilan list dari index 0 hingga dan sebelum ke 5
print("\n")
print(n[1:3]) # membuat list yang dari index ke 1 hingga sebelum index ke 3
print("\n")
del n[2] # Fungsi dari del adalah untuk menghapus
print(n)

n[3] = "Bangsat"
print(n[:5])
# melakukan penambahan pada element list
n.append(9)
n.append(20)
n.append(30)
n.append(100)
print("Append gunanya untuk menambahkan list ")
print(n[:10])
# print(x[1:5:3])
bilangan = [1,2,3,4,5,6,7,8,9,10]
print(bilangan[1:9:2]) #membuat list dari index ke 0 hingga sebelum index ke 9

# Menggunakan Tuple
 # Tuple adalah list yang nilainya tidak bisa di ubah atau dikatakan adalah immutable dengan menggunakn ()
 # sedangkan list pada phyton menggunakan [] yang bisa diubah listnya

# Contoh Tuple
manusia = ("Candra","Julius","Ayam")
print(manusia[1])
print(manusia[:3])
# manusia[1] = "manusia"

# Menggunakan set
# Set adalah kumpulan item bersifat unik dan tanpa urutan (unordered collection) didefinisikan menggunakan {}(kurung kurawal)
# Contoh set
Saya = {1,2,3,4,5,6,5,2,1}
print(Saya)

# Dictionary pada phyton adalah kumpulan pasangan kunci-nilai (pair of key-value) yang bersifat tidak berurutan
# Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. Untuk mengakses datanya, kita harus mengetahui kuncinya (key).
# Pada Python, dictionary didefinisikan dengan kurawal dan tambahan definisi berikut:
#  Setiap elemen pair key-value dipisahkan dengan koma (,)
# Key dan Value dipisahkan dengan titik dua (:)
# ey dan Value dapat berupa tipe variabel/obyek apapun
d = {1:'Candra','Dimana':2}
print(type(d))
print("d[1] = ",d[1])
print("d[key] = ",d['Dimana'])
# 1 adalah key nya dan dimana adalah keynya
# sedangkan Candra dan 2 adalah valuenya
# Dictionary bukan termasuk dalam implementasi urutan (sequences), sehingga tidak bisa dipanggil dengan urutan indeks.
 # Misalnya dalam contoh berikut dicoba dengan indeks 2,
 # tetapi menghasilkan error (KeyError) karena tidak ada kunci (key) 2:

 #print("Kunci dari key",d[2])

 # Konversion
 # Kita dapat melakukan konversi tipe data bawaan dengan menggunakan fungsi konversi tipe bawaan (standard type) misalnya: int(), float(), str(), dll.
print(float('1'))
print(int(10.2))

# dapat melakukan konversi data list set dan tuple
print(list("hello"))
print(tuple({1,2,3,4,5}))
print(set([2,3,4,5]))

# Konversi data dic
kamu = dict([[1,2],[3,4]])
print(kamu)