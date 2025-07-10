class Calculator:
    def addition(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
    def subtraction(self,a,b):
        self.a=a
        self.b=b
        return self.a-self.b
    def multiplication(self,a,b):
        self.a=a
        self.b=b
        return self.a*self.b
    def division(self,a,b):
        self.a=a
        self.b=b
        try:
            self.res=self.a/self.b
            print(f"division:",self.res)
        except ZeroDivisionError:
            print("division by zero is not allowed")
cal=Calculator()
print(cal.addition(10,5))
print(cal.subtraction(10,5))
print(cal.multiplication(10,5))
cal.division(10,0)