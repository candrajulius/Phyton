var1 =  100

if var1 == 100:
    print("var1 adalah nilai 100 ")
else:
    print("var1 bukan nilai 100 ")

var2 = 200
if  var2 == 100:
    print("Nilai dari var2 adalah 200")
else:
    print("Nilai dari var2 bukan 200")

# mengambil inputan dari user
candra = int(input("Masukkan angka yang anda inginkan = "))
if  candra <= 1000:
    discount = candra * 0.5
    print("Discount = ",discount)
else:
    discount = candra * 0.10
    print("Discount = ",discount)
print("Pembayaran: ", candra - discount)

a = 8
if  a % 2 == 0:
    print("bilangan  {} adalah genap" .format(a))
else:
    print("Bilangan  {} adalah ganjil".format(a))

uang = int(input("Masukkan angka yang anda inginkan = "))
if  uang > 100 :
    potongan = (20 / 100) * uang
    print("Potongan anda adalah {}".format(potongan))
else:
    potongan = (10 / 100) * uang
    print("potongan anda adalah {}".format(potongan))
print("Pembayaran dari belanja anda adalah = ",uang - potongan )

uang1 = int(input("Masukkan pembayaran anda = "))
if  uang1 < 10000:
    discount1 = uang1 * 0.5
    print("Discount ",discount1)
elif uang1 < 5000:
    discount1 = uang1 * 0.10
    print("Discount ",discount1)
else:
    discount1 = uang1 * 0.15
    print("Discount ",discount1)
print("Pembayaran  = " , uang1 - discount1)

# Ternary Operator
# condition_if_true if condition else condition_if_false
#  # Contoh
# is_nice = True
# state = "nice" if is_nice else "not nice"
# Ternary Tuples
# (kondisi_if_false,kondisi_if_true)[kondisi] # Rumusnya
# Contoh
nice = True
print(("Cantik","Jelek")[nice]) # pada nice dimanfaat nilai element ke 0 itu dinyatakan false, sedangkan
# element ke 1 adalah true

# Short Tenary Operator
nama = "Candra"
bandal  = str.lower(input("masukkan nama anda : "))
if  bandal == nama:
    print("Ini memang benar nama saya")
else:
    print("Ini bukan nama saya")
print("Anda menginput {}".format(bandal))
