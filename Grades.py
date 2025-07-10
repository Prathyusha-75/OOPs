std=input("Enter student name: ")
marks=list(map(int,input("Enter marks seperated by space: ").split()))
avg=sum(marks)/len(marks)
def grades(avg):
    if avg>=90 and avg<=100:
        return "A+"
    elif avg>=80 and avg<=89:
        return "A"
    elif avg>=70 and avg<=79:
        return "B"
    elif avg>=60 and avg<=69:
        return "C"
    elif avg>=50 and avg<=59:
        return "D"
    elif avg<50:
        return "F"
print("Student:",std)
print("Marks:",marks)
print("Average:",avg)
print("Grade:",grades(avg))
