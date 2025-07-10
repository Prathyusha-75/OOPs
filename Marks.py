class Marks:
    def math_marks(self,marks):
        self.__marks=marks
    def setmarks(self,marks):
        self.__marks=marks
    def getmarks(self):
        return self.__marks
m=Marks()
m.math_marks(80)
print(m.getmarks())