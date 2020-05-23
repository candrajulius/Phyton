# Class
# Contoh kelas

# class NamaKelas:
#     pass # gantikan dengan pertanyaan pertanyaan , misal: atribut atau metode
# Contohnya
class Kalkulator:
    """Contoh kelas kalkulator sederhana"""
    i = 2345
    def __init__(self,j = 1234):
        self.j = j
    def candra(self):
        return "Candra ganteng"

julius = Kalkulator.i = 2000
print(julius)

# Pembahasan selanjutnya merupakan dari Objek (object: an instance of a class)
# Contoh membuat instance dari class Kalkulator menghasilkans sebuah objek
l = Kalkulator() # Membuat instance dari kelas jadi objek, kemudian disimpan pada variabel l

# Untuk memanggil metode f dari objek k, hasil instance dari class Kalkulator di atas sebagai berikut.
d = l.candra()
print(d)

# Class dan Construktor
u = Kalkulator(j= 2030)
print(u.j)

# Method
# Pembahasan lebih detail mengenai metode, selain yang dibahas sebelumnya, kita akan membahas 3 jenis metode:
#
# Metode dari objek (object method)
#
# Metode dari class (class method)
#
# Metode secara static (static method

# Classmethod adalah sebuah fungsi yang mengubah metode menjadi metode dari kelas

# Contoh kelas method
class Manusia:
    """Contoh kelas dalam manusia yang sederhana"""
    def g(self):
        return 'Candra Julius Sinaga'
    @staticmethod
    def kali_angka(angka1,angka2):
        return '{} x {} = {}'.format(angka1,angka2,angka2 * angka1)

# Cara sederhana untuk memanggil method static denga kelas
manusia1 = Manusia.kali_angka(20,10)
print(manusia1)

b = Manusia()
d = b.kali_angka(20,90)
print(d)