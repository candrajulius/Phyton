# Mekanisme Pewarisan (Inheritance)

# Paradigma Pemrograman Berorientasi Objek memiliki konsep pewarisan atau dalam
# bahasa Inggris disebut inheritance, tentunya di Python mendukung fitur ini.
class Candra:
    """Contoh kelas sederhana. anggap kelas ini tidak boleh diubah"""

    def __init__(self,nilai=0):
        self.nilai = nilai

    def tambah_angka(self,angka1,angka2):
        self.nilai = angka1 + angka2
        if  self.nilai > 9:
            print("Kalkulator sederhanan melebihi batas angka: {}".format(self.nilai))
        return self.nilai

class Kalkulatorkali(Candra):
    """Contoh mewarisi kelas kalkulator sederhana"""
    def kali_saya(self,angka1,angka2):
        self.nilai = angka1 * angka2
        return self.nilai

# Pemanggilan kelas kalkulator
kk = Kalkulatorkali()
a = kk.kali_saya(20,30) # Sesuai dengan definisi kelas memiliki fitur kali_angka
print(a)

b = kk.tambah_angka(20,10) # Sesuai dengan fitur tambah_angka karena mewarisi dari kalkulator
print(b)

print("\n")


#  Menimpa(Override) Metode dengan nama yang sama dengan kelas dasar
class CandraSehat(Candra):
    def kali_satu(self,angka1,angka2):
        self.nilai = angka1 * angka2
        return self.nilai

    def tambah_terjemahan(self,angka1,angka2):
        self.nilai = angka1 + angka2
        return self.nilai

kartu = CandraSehat()
julius = kartu.kali_satu(20,10)
print(julius)
saya = kartu.tambah_terjemahan(20,9)
print(saya)

# Pemanggilan Metode Kelas Dasar dari Kelas Turunan dengan Sintaksis Super
# Contoh Kelas turunan super
class KalkualtroTambah(Candra):
    def tambah_satu(self,angka1,angka2):
        if  angka1 + angka2 <= 9: # fitur ini sudah oke dikelas dasar, gunakan yang ada saja
            super().tambah_angka(angka1,angka2) # panggil fungsi dari Kalkulator lalu isi nilai
        else: # Ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            self.nilai = angka1 + angka2
        return self.nilai

sinaga = KalkualtroTambah()
sinaga1 = sinaga.tambah_satu(20,10)
print(sinaga1)