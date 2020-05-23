# Contoh kesalahan
# z = 0
# 1/z
try:
    z = 0
    x = 1/z
    print(x)
except ZeroDivisionError:
    print("tidak bisa membagi dengan angka nol",ZeroDivisionError)

# ketika membuka file tetapi file tidak ada dibuat
try:
    with open('conoth.py') as file:
        print(file.read())
except (FileNotFoundError):
    print("file tidak ditemukan",FileNotFoundError)

d = {'ratarata': '10.0'}
try:
    print('rata-rata: {}'.format(d['rata_rata']))
except KeyError:
    print("Kunci tidak ditemukan pada dictionary",KeyError)
except ValueError:
    print("Nilai tdiak sesuai",ValueError)

try:
    print('rata-rata : {}'.format(d['ratarata']/3))
except KeyError:
    print("Terjadi kesalahan saat membuat key ",KeyError)
except (ValueError,TypeError):
    print("Value dan Tipe error",(ValueError,TypeError))

try:
    print('Pembulatan rata-rata: {}'.format(int(d['ratarata'])))
except(ValueError,TypeError) as e:
    print("penanganan masalah: {}".format(e))