from functools import reduce
class Averge_Calculation:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def calculation(self):
        sum=reduce((lambda x,y:x+y),self.marks)
        average=sum/len(self.marks)
        print("the average of "+self.name+" is "+str(average))

Marks=[40,50,60,70]
average1=Averge_Calculation("Ali",Marks)
average1.calculation()
