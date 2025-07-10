class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def setstudent(self,name,marks):
        self.__name=name
        self.__marks=marks
    def getstudent(self):
        return self.__name
    def getmarks(self):
        return self.__marks
    def display(self):
       if self.__marks<0 or self.__marks>100:
           print("Error:Marks should be between 0 and 100")
       else:
           print("Student Marks (after invalid input):",self.__marks)
s1=Student("Alice",190)
print("Student Name:",s1.getstudent())
s1.display()
#print("Student Marks:",s1.getmarks())
