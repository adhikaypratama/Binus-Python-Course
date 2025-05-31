while True:
    userInput = int(input("Masukkan nilai: "))
    tesGanjil = userInput % 2
    
    if(tesGanjil == 1):
        print("Ini angka ganjil")
    else: 
        print ("ini angka genap")
    
    stopInput = input("Lanjut? (y/n)")
    if(stopInput == "y"):
        continue
    elif(stopInput == "n"):
        break
