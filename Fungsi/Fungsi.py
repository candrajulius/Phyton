# Fungsi adalah blok kode yang terorganisasi dengan baik sehingga dapat digunakan kembali (reusable).
# Mendeklarasikan sebuah fungsi pada phyton dengan membuat awalan def
 # Contoh
 # def fungsiNama( paramater ):
 # "Function doing"
 # function_suite
 # return [expression]

 # Contoh penggunaan fungsi pada phyton
def FungsiNama(str,int):
    candra = ("Nama saya adalah {}".format(str))
    age = ("Umur saya adalah {}".format(int))
    print(candra,age)
    return

def PemanggilanAngka(arg1,arg2):
    total = arg1 + arg2
    print("Inside the function {}".format(total))
    return total

FungsiNama("Candra Julius Sinaga",20)
bangsat = PemanggilanAngka(10,20)
print("Out of the function {}".format(bangsat))

# Nilai kembalian dari sebuah fungsi dapat disimpan dalam sebuah variabel. Ini yang akan membedakan s
# ebuah fungsi yang mengembalikan nilai dengan sebuah fungsi yang tidak mengembalikan nilai (sering disebut sebagai prosedur).

def kuadrat(x):
    return x*x
a = 10
k = kuadrat(a)
print("Nilai kuadrat dari {}".format(a,k))

# Pass by reference vs value
# Seluruh parameter (argumen) pada bahasa Python bersifat “passed by reference”. Artinya saat Anda mengubah sebuah variabel,
# maka data yang mereferensi padanya juga akan berubah, baik di dalam fungsi, maupun di luar fungsi pemanggil.
# Kecuali jika anda melakukan operasi assignment yang akan mengubah reference parameter.
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print('Nilai di dalam fungsi: {}'.format(mylist))

cabdra = [12,3,4,521]
changeme(cabdra)
print("Nilai dari fungsi luar {}".format(cabdra))

def penambahan(mylist):
    mylist = [1,3,4,51,2]
    print("My angka dalam list {}".format(mylist))

myAngka = [1,34,123,45]
penambahan(myAngka)
print("Niali dari perubahan adalah {}".format(myAngka))
    
# Contoh pemanggilan Variabel-length arguments
# # Contohnya
# def functionName([formal_args]*var_args_tuple):
#     "function docstring"
#     funtionSuite
#     return [expression]

def printInfo(fixedrag, *args):
    "This prints a variable passed arguments"
    print('Output: fixedarg {}'.format(fixedrag))
    for a in args:
        print('argument posisi {}'.format(a))

printInfo(10)
printInfo(10,20,30)
print("\n")

def carinfo(*args,**kwargs):
    for a in args:
        print('argument posisi {}'.format(a))
    for key,value in kwargs.items():
        print('argument kata kuci {} {}'.format(key,value))

carinfo(i=7, j=8, k=9)
carinfo(1, 2, j=8, k=9)
carinfo(*(2, 3), **{'i':7, 'j':8})

# lambda [arg1[,arg2,...argn]]:expression # Saintaks dari lambada
# contoh pengguanaan dari lambada
sum1 = lambda arg1,arg2: arg1 + arg2
print("Value total adalah {}".format(sum1(10,20)))
print("Value total kedua adalah {}".format(sum1(20,20)))

# Cakupan variabel
total = 0 # Ini variabel global
def sama(arg1,arg2):
    total = arg1 + arg2
    print("Inside the function = {}".format(total))
    return total

# Memanggil sum
sama(20,30)
print("Outside the function {}".format(total))