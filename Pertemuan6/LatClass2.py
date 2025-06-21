class Student:
    
    def __init__(self, name="None", score="None"):
        self.name = name
        self.score = score
        
    def printStudent(self):
        print("Name:", self.name, "\nScore:", self.score)
        
    def setStudent(self, name, score):
        self.name = name
        self.score = score
    
student1 = Student()
        
while True:
    
    inputMenu = input("""
    1. Declare Object
    2. Display Object
    3. Change Object Value
    4. Delete Object
    5. Exit
    Enter Your Choice (1/2/3/4/5): """)
    if inputMenu == "1":
        try:
            name = str(input("Enter Name: "))
            score = int(input("Enter Score: "))
            student1 = Student(name, score)
            print("Data input succesful")
        except:
            print("Value error")
            continue
        
    elif inputMenu == "2":
        print(student1.printStudent())
        
    elif inputMenu == "3":
        inputChange = input("Choose what to change (Name/Score): ")
        if inputChange == "Name":
            name = str(input("Enter new name: "))
            student1 = Student(name, score)
            print("Name change succesful")
        elif inputChange == "Score":
            try:
                score = int(input("Enter new score: "))
                student1 = Student(name, score)
                print("Score change succesful")
            except:
                print("Value error")
                continue
        else:
            print("Invalid input")
            continue
        
    elif inputMenu == "4":
        student1 = Student()
        print("Data succesfully deleted")

    elif inputMenu == "5":
        print("Exiting program")
        break
    
    else:
        print("Invalid input")
        continue
