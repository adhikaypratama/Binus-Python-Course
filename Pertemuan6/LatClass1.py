class Student:
    
    def __init__(self, name="Student", age="0", kelas="0"):
        self.name = name
        self.age = age
        self.kelas = kelas
        
    def studentName(self):
        print("Name:", self.name)
        
    def studentAge(self):
        print("Age:", self.age)
        
    def studentKelas(self):
        print("Kelas:", self.kelas)
        
student1 = Student("Adhika", 20, 12)

while True:
    
    inputData = input("Check Name/Age/Kelas?: ")
    if inputData == "Name":
        print(student1.studentName())
    elif inputData == "Age":
        print(student1.studentAge())
    elif inputData == "Kelas":
        print(student1.studentKelas())
    elif inputData == "stop":
        print("Stopping program")
        break
    else:
        print("Data not found")
        continue
