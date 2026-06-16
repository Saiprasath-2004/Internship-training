class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary = salary
    def display(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)
    
emp1=Employee('Sai',90000)
emp2=Employee('Rahul',75000)

emp1.display()
emp2.display()
        