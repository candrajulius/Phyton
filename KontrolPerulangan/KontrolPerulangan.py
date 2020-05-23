
# Penggunaan break pada phyton
import sys

for letter in 'pyhton':
    if  letter == 'h':
        break
    print("Current letter {}".format(letter))

print("\n")
# Contoh 2 dari break
var = 10
while var > 0:
    print("Current variabel {}".format(var))
    var = var - 1
    if  var == 5:
        break

# Continue
for l in 'Candra':
    if  l == 'r':
        continue
    print("Variabel in candra is {}".format(l))
# Contoh kedua dari continue

for a in {1,2,3,4,-2,-5,-4}:
    if a <= 0:
        continue
    print("element positif adalah {}".format(a))
# Contoh ketiga penggunaan dari continue
var = 10
while var > 0:
    var = var - 1
    if  var == 5:
        continue
    print("Current variabel value: {}".format(var))
# Contoh else setelah for
# else setelah for digunakn untuk mencari item yang tidak ditemukan atau solusi ketika suatu logic tidak
# berfungsi maka akan dikeluarkan solusi dari else setelah for
# for item in container:
#     if search_something:
#         process(item)
#         break
# else:
#     no_such_thing()

for saya in range(2,10):
    for x in range(2,saya):
        if saya % x == 0:
            print(saya,"equals",x,'*',saya/x)
            break
else:
    print(saya,"Adalah sebuah bilangan prima")

    # else setelah while
n = 5
while n > 0:
    n = n -1
    if  n == 2:
        break
    print(n)
else:
    print('looping anda telah berakhir')

print("\n")
# Contoh Pass
# Pass statement dilakukan pada saat operasi bernilai null(kosong) tidak ada yang terjadi saat ia dipanggil
# Contohnya
for leeter in 'pyhton':
    if leeter == 'h':
        pass
    print("This is pass block")
    print("Current leter: {}".format(leeter))

print("\n")
 # maksud dari statement ini adalah mengatakan pada variabel letter di sebuah variabel phyton
 # dan bertanya apakah di String pyhton ada menggunakan kata yang besar
 # jika ada maka kata itu akan dilewatkan dan akan terus mengulang dengan kata yang selanjutnya
for leter in 'Phyton':
    if leter.isupper():
        pass
    else:
        print('lower letter : {}'.format(leter))

# Mengatasi sebuah error pada logika
# data = ''
# while (data!='exit'):
#     try:
#         data = input("please enter in a integer (type to exit)")
#         print('got integer: {}'.format(int(data)))
#     except:
#         if  data == 'exit':
#             pass
#             break
#         else:
#             print('error {}'.format(sys.exc_info()[0]))


 # List Comprehension (membuat list dengan inline loop dan if)

print("\n")
 # cara 1
numbers = [1,2,3,4,5]
squeres = []
for n in numbers:
    squeres.append(n**2)
print(squeres)

# Cara yang sederhana pada phyton menggunakan list
squeres = [n**2 for n in numbers]
print(squeres)

# Cara ketiga menemukan bilangan yang ada di kedua list
list_a = [1,2,3,4,5]
list_b = [2,3,45,5,4]
cari_num = []
for a in list_a:
    for b in list_b:
        if  a == b:
            cari_num.append(a)
print(cari_num)
print("\n")
# Contoh keempat Implementasi dengan list Comphersion
list_c = [1,2,3,4,5,621,6]
lisd_d = [1,2,34,4,5,3,6]
common_candra = [a for a in list_c for d in lisd_d if a==d]
print(common_candra)

# contoh ke lima kecilkan semua huruf
candra = ["bangsat","bidadari","jatuh","dari","kayangan"]
_candra = [_ .upper() for _ in candra]
print(_candra)

list_k = range(1,10,2)
x = [[a**2, a**3] for a in list_k]
print(x)