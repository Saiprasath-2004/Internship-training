
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def study(self):
        print(f"{self.name} studied Well for exam and got {self.grade} Grade")

    
s1=Student("Sai",'A')
s2=Student("Varshini",'A+')

s1.study()
s2.study()
