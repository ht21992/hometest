class Person:
    def __init__(self,job,wage):
        self.job=job
        self.wage=wage
def financial_status(persons):
    """we have classes bad , average, good and rich and this function
    will check each person belongs to which one depending on each person's wage"""
    for person in persons:
        if person.wage<200:
            print("bad")
        elif person.wage>200 and person.wage<1000:
            print("avarage")
        elif person.wage>1000 and person.wage<2000:
            print("good")
        elif person.wage>2000:
            print("rich")


persons=[Person("enginner",1500),Person("housewife",0),Person("worker",220),Person("developer",2500)]
financial_status(persons)