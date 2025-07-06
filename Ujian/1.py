def rumus(b, a, y):
    return b - 10 / 2 * (1 - a / 2 * y ** 2)

try:
    b = int(input("b: "))
    a = int(input("a: "))
    y = int(input("y: "))
except:
    print("Error")
    
print(rumus(b, a, y))
