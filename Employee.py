class Employee:
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
    def setemployee_name(self):
        print(self.name)
    def setemployee_salary(self):
        print(self.salary)
    def setemployee_age(self):
        print(self.age)
    def getemployee_name(self):
        return self.name
    def getemployee_salary(self):
        return self.salary
    def getemployee_age(self):
        return self.age
    def display(self):
        print("Employee Name:",self.getemployee_name())
        if self.salary<0 or self.salary==0:
            print("salary must be greater than 0")
        else:
            print("Employee Salary:",self.getemployee_salary())
        if self.age<18 or self.age>100:
            print("age must be between 18 and 100")
        else:
            print("Employee age:",self.getemployee_age())
e1=Employee("Alice",0,20)
e1.display()


