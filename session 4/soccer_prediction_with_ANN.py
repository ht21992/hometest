import numpy as np
class Match_Result:
    def __init__(self,Team_A,Team_B,Team_A_rating,Team_B_rating,TeamA_GA,TeamB_GA):
        self.Team_A=Team_A
        self.Team_B=Team_B
        self.Team_A_rating=Team_A_rating
        self.Team_B_rating=Team_B_rating
        self.TeamA_GA=TeamA_GA
        self.TeamB_GA=TeamB_GA

    def activation_function(self, x):
        if x == 1:
            return self.Team_A+" will draw with "+self.Team_B
        elif x>1:
            return self.Team_A+" will Win "+self.Team_B
        else:
            return self.Team_A+" will lose against "+self.Team_B

    def predict(self):
        inputs = np.array([self.Team_A_rating, self.Team_B_rating, self.TeamA_GA,self.TeamB_GA])
        WeightsInputToOutput=[2,-2,1,-1]
        output = np.dot(WeightsInputToOutput, inputs)
        print("output: " + str(output))
        return self.activation_function(output)
def get_statistic(Team):
    for name in Team["Team"]:
        for goal_avrage in Team["GA"]:
            for rating in Team["rating"]:
                return name,rating,goal_avrage

import pandas as pd
import random

xg_data = pd.read_csv('epl_xg.csv')
Team_1=xg_data[xg_data['Team']==random.choice(xg_data['Team'])]
Team_2=xg_data[xg_data['Team']==random.choice(xg_data['Team'])]
name1,r1,g1=get_statistic(Team_1)
name2,r2,g2=get_statistic(Team_2)
print("club: "+name1+" Rating: "+str(r1)+" Goal Avrage: "+str(g1))
print("club: "+name2+" Rating: "+str(r2)+" Goal Avrage: "+str(g2))
ma=Match_Result(name1,name2,r1,r2,g1,g2)
print(ma.predict())