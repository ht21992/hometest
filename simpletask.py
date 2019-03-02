from functools import reduce
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __str__(self):
        return self.name
    __repr__=__str__
def calculation(students):
    red_diploma=[]
    yellow_diploma=[]
    for student in students:
        sum=reduce((lambda x,y:x+y),student.marks)
        average=sum/len(student.marks)
        if average>80:
            red_diploma.append(student)
        else:
            yellow_diploma.append(student)
    print(red_diploma)
    print(yellow_diploma)

students=[Student("Ali",[40,50,60,70]),Student("Daniel",[90,80,90,100]),Student("Marry",[80,70,90,70])]
calculation(students)

#testing pull command
