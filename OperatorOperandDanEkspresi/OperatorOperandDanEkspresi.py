from operator import *

# Jenis-jenis operator
# Matematika dan string
# + (tambah)
# Menambahkan dua objek.
# 3 + 5 menghasilkan 8
# 'a' + 'b' menghasilkan 'ab'.
# - (kurang)
# Mengurangkan operand kedua dari operand pertama. Jika hanya satu operand, diasumsikan nilai operand pertama adalah 0.
# -5.2 adalah expression yang sama dengan 0 - 5.2 menghasilkan -5.2.
# 50 - 24 menghasilkan 26.
# Tidak berlaku untuk string, akan menghasilkan error unsupported operand.
# * (perkalian)
# Mengembalikan hasil perkalian angka atau mengembalikan string yang diulang sejumlah tertentu.
# 2 * 3 menghasilkan 6.
# 'la' * 3 menghasilkan 'lalala'.
# ** (pangkat)
# Mengembalikan operand pertama pangkat operand kedua.
# 3 ** 4 menghasilkan 81 (sama dengan 3 * 3 * 3 * 3).
# | Tips: untuk akar dua, gunakan pangkat 0.5.
# / (pembagian)
# Mengembalikan hasil pembagian operand pertama dengan operand kedua (float).
# 13 / 3 menghasilkan 4.333333333333333.
# // (pembagian habis dibagi / div)
# Mengembalikan hasil pembagian operand pertama dengan operand kedua (bilangan bulat), kecuali jika salah satu operand adalah float, akan menghasilkan float.
# 13 // 3 menghasilkan 4.
# -13 // 3 menghasilkan -5.
# 9//1.81 menghasilkan 4.0.
# % (modulo)
# Mengembalikan sisa bagi.
# 13 % 3 menghasilkan 1.
# -25.5 % 2.25 menghasilkan 1.5.
#
#
# Operasi Bit
# << (left shift)
# Menggeser representasi bit/binary dari operand pertama sebanyak operand kedua ke kiri.
# 2 << 2 menghasilkan 8.
# 2 direpresentasikan sebagai 10 dalam binary.
# Geser ke kiri sebanyak 2x, menjadi 1000 (tambahkan 0 di belakangnya).
# 1000 dalam binary bernilai 8 dalam desimal.
# >> (right shift)
# Menggeser representasi bit/binary dari operand pertama sebanyak operand kedua ke kanan.
# 11 >> 1 menghasilkan 5.
# 11 direpresentasikan sebagai 1011 dalam binary.
# Geser ke kanan sebanyak 1x, menjadi 101.
# 101 dalam binary bernilai 5 dalam desimal.
# & (bit-wise AND)
# Menjalankan operasi binary AND pada representasi operand pertama dan kedua.
# 5 & 3 menghasilkan 1.
# Representasi binary 5 adalah 101 dan representasi binary 3 adalah 011.
# 101 and 011 bernilai 001.
# 001 dalam desimal adalah 1.
# | (bit-wise OR)
# Menjalankan operasi binary OR pada representasi operand pertama dan kedua.
# 5 | 3 menghasilkan 7.
# Representasi binary 5 adalah 101 dan representasi binary 3 adalah 011.
# 101 or 011 bernilai 111.
# 111 dalam desimal adalah 7.
# ^ (bit-wise XOR)
# Menjalankan operasi binary XOR pada representasi operand pertama dan kedua.
# 5 ^ 3 menghasilkan 6.
# Representasi binary 5 adalah 101 dan representasi binary 3 adalah 011.
# 101 xor 011 bernilai 110.
# 110 dalam desimal adalah 6.
# ~ (bit-wise invert)
# Menjalankan operasi binary invert pada representasi operand.
# Nilai invert dari x adalah -(x+1), menggunakan metode Two’s Complement
# ~5 menghasilkan -6.
# Lebih lanjut mengenai Two’s Complement dapat dibaca pada https://en.wikipedia.org/wiki/Two%27s_complement
#
#
# Perbandingan
# < atau operator.lt (less than)
# Menjalankan perbandingan apakah operand pertama lebih kecil dari operand kedua.
# 5 < 3 menghasilkan False and 3 < 5 menghasilkan True.
# Perbandingan dapat berisi lebih dari dua operand, misalnya 3 < 5 < 7 menghasilkan True.
# > atau operator.gt (greater than)
# Menjalankan perbandingan apakah operand pertama lebih besar dari operand kedua.
# 5 > 3 menghasilkan True.
# <= atau operator.le (less than or equal to)
# Menjalankan perbandingan apakah operand pertama lebih kecil atau sama dengan operand kedua.
# x = 3; y = 6;
# x <= y menghasilkan True.
# >= atau operator.ge (greater than or equal to)
# Menjalankan perbandingan apakah operand pertama lebih besar atau sama dengan operand kedua.
# x = 4; y = 3;
# x >= y menghasilkan True.
# == atau operator.eq (equal to)
# Menjalankan perbandingan apakah operand pertama sama dengan operand kedua.
# x = 2; y = 2;
# x == y menghasilkan True.
# x = 'str'; y = 'stR';
# x == y menghasilkan False.
# x = 'str'; y = 'str';
# x == y menghasilkan True.
# != atau operator.ne (not equal to)
# Menjalankan perbandingan apakah operand pertama tidak sama dengan operand kedua.
# x = 2; y = 3;
# x != y returns True.
 # Contohnya
 # Penambahan
candra = 1 + 2
print(candra)
candra1 = 'A' + 'b'
print(candra1)
# Perkalian
print('\nIni perkalian angka')
sama = 1 * 4
print(sama)
print('\nIni perkalian string')
print('A' * 9)
print('\n Perpangkatan')
candra2 = 4 ** 10
print(candra2)
print(3 ** 0.5)
# pembagian
print('\n pembagian')
candra3 = 4 / 3
print(candra3)
# pembagian habis dibagi / dv
print(13 // 3)
print(-13 // 3)
print(9 // 1.81)
# modula == Mengembalikan sisa bagi
print(13 % 3)
print(-25.5 % 2.25)
# Pengguanan left shif
print(2 << 2)
# Penggunaan right shif
print(11 >> 1)

# Perbandingan
print(5 < 3) # perbandingan menggunakan les than atau <(Lebih kecil dari)
print(5 > 3) # perbandingan mengguankan greater than atau > (Lebih besar dari)
print(5 >= 3) # perbandingan menggunakan less than or equal to (Lebih besar sama dengan dari)
print(5 <= 3) # perbandingan menggunakan greater than or equal to(Lebih kecil sama dengan dari)
print(5 == 5) # perbandingan menggunakan sama dengan
print( 5 != 3) # perbandingan menggunakan tidak sama dengan

# Penggunaan le, lt, gt, ge, eq, ne
a = 1
b = 5.0
print('a = {}'.format(a))
print('b = {}'.format(b))
for func in (lt ,le , eq , ne , ge , gt):
    print('{} (a,b): {}'.format(func.__name__,func(a,b)))

# penggunaan dari AND
x = False
y = True
print(x and y)
u = True
z = True
print(u and z)
d = False
e = False
print(e and d)
g = True
h = False
print(g and h)

# Penggunaan dari boolean not
x = False
print(not x )

# Penggunaan dari boolean OR
x = False
y = True
print(x or y)
p = True
k = True
print(p or k)
u = False
h = False
print(u or h)
