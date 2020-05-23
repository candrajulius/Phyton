 #Sebelumnya pada pembahasan urutan (sequences), Anda sudah mengetahui bahwa slicing digunakan untuk urutan.
 # Salah satu fungsi yang paling bermanfaat untuk List atau String adalah len() yang akan menghitung panjang atau banyaknya elemen dari
 # List (untuk String menjadi menghitung jumlah karakternya).
l = [1,2,3,4,5,6,6,7,7]
s = set(l)
x = "Hello Candra"
print(s)
print(len(s))
print(l)
print(len(l)) # Len berfungsi untuk menghitung panjang dari string
# print(set(x))
print(x)
print(len(x))

#Penggabungan dan Replikasi
#Pada List juga dimungkinkan adanya penggabungan (+) dan replikasi (*).
p = [1,2,3,4,5] + ['A','B','C','D']
print(p)

l = ['A','B','C','D'] * 3
print(l)

# Fungsi pengali juga dapat Anda manfaatkan untuk inisialisasi List.
arr = [0] * 10
print(len(arr))
print(arr)

# Range
 # Fungsi range() memberikan deret bilangan dengan pola tertentu. Untuk melakukan perulangan (misalnya for) dalam mengakses elemen list,
 # Anda dapat menggunakan fungsi range() pada Python.
 # Lebih detail mengenai operasi perulangan akan dibahas pada modul Perulangan dan Kontrol Perulangan.
 # Fungsi range dapat memiliki 1-3 parameter:
 # Range dengan 1 parameter n: membuat deret bilangan yang dimulai dari 0, sebanyak n bilangan.
for i in range(9):
    print(i)
print("\n")
    # Range dengan 2 parameter n,p: membuat deret bilangan yang dimulai dari n, hingga sebelum p (bilangan p tidak ikut).
    # Sering disebut sebagai inklusif n (deret dimulai bilangan n) dan eksklusif p (deret tidak menyertakan bilangan p).
for j in range(3,9):
   print(j)
   # Range dengan 3 parameter n,p,q: membuat deret bilangan yang dimulai dari n,
   # hingga sebelum p (bilangan p tidak ikut), dengan setiap elemennya memiliki selisih q.
t = [_ for _ in range (1,9,2)]
print(t)

# in dan not in
 # Untuk mengetahui sebuah nilai atau objek ada dalam list, Anda dapat menggunakan operator in dan not in.
 # Fungsi ini akan mengembalikan nilai boolean True atau False.
 # Contohnya adalah sebagai berikut:
candra =  ["cnadra","Bangsat","Kamu"]
print("Bangsat" in candra) # in menyatakan boolean terhadap dengan sebuah variabel dengan nilai yang ada dalam variabel tersebut dan keluarnnya berupa True dan False
print("Manusia" in candra)
k = "Bangsat" not in candra
print(k)
print("Saya" not in candra)

# Memberikan nilai (assignment) untuk lebih dari 1 variabel sekaligus
 # Anda dapat memberikan nilai ke beberapa variabel sekaligus dari element List atau Tuple. Sehingga tanpa perlu menandai satu-per-satu seperti
cat = ["fat","orange","loud"]
size = cat[0]
color = cat[1]
dispostion = cat[2]
print(size)
print(color)
print(dispostion)

# penyederhanaan dari tipe list dengan menggunakan tuple
cat = ['fat','red','20'] # from list
panjang,lebar,warna = cat
print(cat)
bear = ['Gemuk','Merah',10]
berat,hijau,tinggi = bear
print(bear)

# Tip: Penggunaan assignment pada multi variabel ini dapat Anda gunakan untuk menukar nilai dua atau lebih variabel:
a, b = 'Candra','Julius'
a,b = b,a
print(a)
print(b)
# Sort dapat diurutkan menggunakan list
x = [1,23,45,21,52,100]
print(sorted(x))
print(x.sort())

# Memebuat urutannya menjadi terbalik
x.sort(reverse=True)
print(x)

manusia = ['A','B','d','C']
manusia.sort(key=str.lower)
print(manusia)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)

# Manipulasi String
# String atau teks adalah salah satu bentuk data yang akan Anda olah dalam program.
 # Anda dapat melakukan penggabungan, pemisahan, sub-string, penambahan/pengurangan spasi, konversi huruf kapital, format strings, dan sebagainya.
 # Python mengetahui bahwa pada Bob\’s, sebelum petik terdapat backslash (\) yang menandakan petik tunggal merupakan bagian dari string dan bukan merupakan akhir dari string.
 # Escape character \' dan \" memungkinkan Anda untuk memasukkan karakter ' dan '' dalam bagian string. Beberapa contoh Escape Character
# \'          Single quote
# \"          Double quote
# \t          Tab
# \n         Newline (line break)
# \\          Backslash

# Contoh dari string eschape chracter
print("Hello My name is Candra \n How are you?\nI\'m doing fine")
print('\n')
multi_Line = """ Hello my name is Candra 
How are you ? 
i am fine """
print(multi_Line)

# Raw Strings
 # Sebaliknya, Python juga menyediakan cara untuk memasukkan string sesuai dengan apapun input atau teks yang diberikan.
 # Metode ini dinamakan Raw Strings. Umumnya digunakan untuk regex atau beberapa implementasi lain yang sangat bergantung pada keberadaan backslash. Untuk menjadikan raw string,
 # tambahkan huruf r sebelum pembuka string:

print(r'That is Carol\'s cat')

