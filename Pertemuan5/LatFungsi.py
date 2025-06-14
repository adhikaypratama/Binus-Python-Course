def tambah(x, y):
    return x + y
    
def kurang(x, y):
    return x - y
    
def bagi(x, y):
    return x / y
    
def kali(x, y):
    return x * y
    
def modulus(x, y):
    return x % y
    
while True:
    
    inputMenu = input("Enter Menu (+|-|/|*|%|stop): ")
    if inputMenu in ('+', '-', '/', '*', '%'):
        try:
            x = int(input("Enter Value 1: "))
            y = int(input("Enter Value 2: "))
        except:
            print("Value error")
            continue
        
    if inputMenu == '+':
        print("Hasil dari", x, "+", y, "sama dengan", tambah(x, y))
        
    elif inputMenu == '-':
        print("Hasil dari", x, "-", y, "sama dengan", kurang(x, y))
        
    elif inputMenu == '/':
        print("Hasil dari", x, "/", y, "sama dengan", bagi(x, y))
        
    elif inputMenu == '*':
        print("Hasil dari", x, "*", y, "sama dengan", kali(x, y))
        
    elif inputMenu == '%':
        print("Hasil dari", x, "%", y, "sama dengan", modulus(x, y))
        
    elif inputMenu == 'stop':
        print("Stopping Program")
        break
    
    else:
        print("Invalid Input")
