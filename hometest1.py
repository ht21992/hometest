from functools import reduce
class Averge_Calculation:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def calculation(self):
        sum=reduce((lambda x,y:x+y),self.marks)
        average=sum/len(self.marks)
        print("the average of "+self.name+" is "+str(average))

Marks=[70,50,80,90]
average1=Averge_Calculation("Ali",Marks)
average1.calculation()
