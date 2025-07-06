def angkaTerbesar(n1, n2, n3):
    return max(n1, n2, n3)
    
try:
    n1 = int(input("Input angka pertama: "))
    n2 = int(input("Input angka kedua: "))
    n3 = int(input("Input angka ketiga: "))
except:
    print("Input salah")
    
print("Angka terbesar:", angkaTerbesar(n1, n2, n3))
