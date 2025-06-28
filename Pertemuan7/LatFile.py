def inputData():
  file = open("Biodata.txt", "w")
  file.write("Name: " + name + " Age: " + age + " Address: " + address + " Email: " + email)

def printData():
  file = open("Biodata.txt", "r")
  text = file.read()
  print(text)
  
name = (input("Name: "))
age = (input("Age: "))
address = (input("Address: "))
email = (input("Email: "))

inputData()

printData()

file.close()
