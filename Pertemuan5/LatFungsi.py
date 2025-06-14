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
        print(tambah(x, y))
        
    elif inputMenu == '-':
        print(kurang(x, y))
        
    elif inputMenu == '/':
        print(bagi(x, y))
        
    elif inputMenu == '*':
        print(kali(x, y))
        
    elif inputMenu == '%':
        print(modulus(x, y))
        
    elif inputMenu == 'stop':
        print("Stopping Program")
        break
    
    else:
        print("Invalid Input")
