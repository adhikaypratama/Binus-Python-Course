# a. Variabel adalah tempat penyimpanan nilai atau data dalam program
# b. Variabel dalam program ini adalah "y2h", "_t", dan "x"
# c. Variabel "y2h" harus didefinisikan, variabel "x" harus dikasih range, for x dikasih ":",
#   if x % 2 dikasih "==", dan di elif _t > x, ";" diganti menjadi ":" 
    
y2h = 0
_t = 18
for x in range(1, 5):
    if x % 2 == 1:
        y2h = _t - x
    elif _t > x:
        _t = _t // x
    else:
        y2h = y2h + 1

print(x, y2h)
