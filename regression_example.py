class House:
    def __init__(self,size,age,facilities):
        self.size =size
        self.age=age
        self.facilities=facilities
def pricing(houses):
    """it will calculate the price of the house according to house parameters"""
    for house in houses:
        if house.facilities=="Full":
            price=int((house.size*800)/house.age)
            print(price)
        elif house.facilities=="None" and house.age<5:
            price = int((house.size * 600) / house.age)
            print(price)
        else:
            price=int((house.size*400)/house.age)
            print(price)
houses=[House(120,3,"Full"),House(200,2,"None"),House(700,10,"Full"),House(600,12,"None")]
pricing(houses)

