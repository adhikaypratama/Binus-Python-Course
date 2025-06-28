def createFile():
  file = open(fileName, "w")
  file.write(fileInput)
  file.close()

def readFile():  
  file = open(fileName, "r")
  text = file.read()
  print(text)
  file.close()

def appendFile():
  file = open(fileName, "a")
  file.write(inputAppend)
  file.close()

fileName = str(input("Create text file: "))
fileInput = input("Write: ")
createFile()

while True:
  inputMenu = input("""
  1. Read file
  2. Add to file
  3. Stop
  """)

  if inputMenu == "1":
    readFile()

  elif inputMenu == "2":
    inputAppend = input("Add text: ")
    appendFile()

  elif inputMenu == "3":
    print("Stopping program")
    file.close()
    break

  else:
    print("Invalid input")
