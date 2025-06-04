print('=' * 20)
print("Kalkulator Sederhana 🐍")
print("  1. Penjumlahan [+]") 
print("  2. Pengurangan [-]") 
print("  3. Perkalian   [*]") 
print("  4. Pembagian   [/]") 

print('=' * 20)
operasi = input("Pilih operasi (1/2/3/4) : ")
bilangan_1 = int(input("Masukkan bilangan pertama : "))
bilangan_2 = int(input("Masukkan bilangan kedua : "))

print('=' * 20)
if operasi == "1":
    hasil = bilangan_1 + bilangan_2
    print(f"Hasil penjumlahan dari {bilangan_1} + {bilangan_2} adalah : {hasil}")
elif operasi == "2":
    hasil = bilangan_1 - bilangan_2
    print(f"Hasil pengurangan dari {bilangan_1} - {bilangan_2} adalah : {hasil}")
elif operasi == "3":
    hasil = bilangan_1 * bilangan_2
    print(f"Hasil perkalian dari {bilangan_1} x {bilangan_2} adalah : {hasil}")
elif operasi == "4":
    hasil = bilangan_1 / bilangan_2
    print(f"Hasil pembagian dari {bilangan_1} / {bilangan_2} adalah : {hasil}")
else:
    print("Invalid WOI! Pilih operasi dari (1/2/3/4)")
print('=' * 20)
