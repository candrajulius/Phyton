# Example for pertama pada phyton
for letter in 'phyton':
    print("Current letter {}".format(letter))
# Cara kedua menggunakan list
fruits = ["Apel","jeruk","Pisang"]
for j in fruits:
    print("Current in {}".format(j))
# Mengitung berdasarkan len atau panjang pada variabel list
print("\n")
for k in range(len(fruits)):
     print("Current fruits {}".format(fruits[k]))

# Menggunakan While
# Nilai true pada phyton adalah nilai yang non zero
# Contohnya

var = 1
while var > 0:
    print("nilai {} sangat besar dari 0".format(var))
    break # kalau tidak ditambah statement break maka akan muncul infinitive loop
    
while var < 10:
    print("Nilai dari {}".format(var))
    var = var + 1
print("\n")

# Perulangan bertingkat
for b in range(0,5):
    for u in range(0,5 - b):
        print('*',end='')
        print()