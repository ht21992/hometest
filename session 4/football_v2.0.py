import requests
import pandas as pd
import numpy as np
import  random
import socket
class Match_Result:
    def __init__(self,Host_Team,Host_win,Host_draw,Host_Loss,Host_goals,Host_goal_conceded,Away_Team,Away_win,Away_draw,Away_Loss,Away_goals,Away_goal_conceded):
        self.HT=Host_Team
        self.HW=Host_win
        self.HD=Host_draw
        self.HL=Host_Loss
        self.HF=Host_goals
        self.HA=Host_goal_conceded
        self.AT=Away_Team
        self.AW=Away_win
        self.AD=Away_draw
        self.AL=Away_Loss
        self.AF=Away_goals
        self.AA=Away_goal_conceded

    def activation_function(self, x):
        if x == 0:
            return self.HT+" will draw with "+self.AT
        elif x>0:
            return self.HT+" will Win "+self.AT
        else:
            return self.HT+" will lose against "+self.AT
    def predict(self):
        inputs = np.array([self.HW,self.HD,self.HL,self.HF,self.HA,self.AW,self.AD,self.AL,self.AF,self.AA])
        WeightsInputToOutput=[2,1,-2,2,-2,-2,1,2,-2,2]
        output = np.dot(WeightsInputToOutput, inputs)
        print("output: " + str(output))
        return self.activation_function(output)

def is_connected():
    try:
        socket.create_connection(("www.google.com",80))
        return True
    except OSError:
        return False

def update_standings_and_calendar():
    print("Updating...")
    if is_connected():
        url = 'https://www.footballwebpages.co.uk/league-table.csv?comp=1&showHa=yes'
        url2= 'https://www.footballwebpages.co.uk/fixtures-results.csv?comp=1'
        url_respond = requests.post(url)
        url2_respond=requests.post(url2)
        if url_respond.ok and url2_respond.ok:
            df = pd.read_csv(url)
            df1=pd.read_csv(url2)
            df.to_csv("live_table.csv")
            df1.to_csv("calendar.csv")
        else:
            print("sth wrong with the server please Try again Later")
    else:
        print("Please check your network connection and try again")
        exit()



def get_Host_stats(Team):
    for name in Team["Team"]:
        for Host_win in Team["HW"]:
            for Host_draw in Team["HD"]:
                for Host_loss in Team["HL"]:
                    for Host_goal in Team["HF"]:
                        for Host_goal_conceded in Team["HA"]:
                            return name,Host_win,Host_draw,Host_loss,Host_goal,Host_goal_conceded
def get_Away_stats(Team):
    for name in Team["Team"]:
        for Away_win in Team["AW"]:
            for Away_draw in Team["AD"]:
                for Away_loss in Team["AL"]:
                    for Away_goal in Team["AF"]:
                        for Away_goal_conceded in Team["AA"]:
                            return name,Away_win,Away_draw,Away_loss,Away_goal,Away_goal_conceded
import datetime
def get_date():
    now = datetime.datetime.today().strftime('%d/%m/%Y')
    print("today is:" + now[1:])
    print("for which date you want the prediction")
    user_date_day = int(input("please enter the day: "))
    user_date_month = int(input("please enter the month: "))
    if user_date_month > 12 or user_date_month < 1:
        print("month is not correct")
    elif user_date_day > 31 or user_date_day < 1:
        print("day is not correct")
    else:
        user_date = str(user_date_day) + "/" + str(user_date_month) + "/" + str(datetime.datetime.now().year)
        if user_date<now[1:]:
            print("matches in your intended date has been held.please enter a valid date")
            get_date()
        return user_date
def match_making():
    update_standings_and_calendar()
    fixture = pd.read_csv('calendar.csv')
    standing=pd.read_csv('live_table.csv')
    user_date=get_date()
    statues=False
    for i in range(len(fixture["Date"])):
        if fixture.loc[i]["Date"]==user_date:
            statues=True
            team1 = fixture.loc[i]["Home Team"]
            team2 = fixture.loc[i]["Away Team"]
            print(team1+" vs "+team2)
            Home_Team = standing[standing['Team'] == team1]
            Away_Team = standing[standing['Team'] == team2]
            HT,HW,HD,HL,HF,HA=get_Host_stats(Home_Team)
            AT,AW,AD,AL,AF,AA=get_Away_stats(Away_Team)
            ma = Match_Result(HT, HW, HD, HL, HF, HA, AT, AW, AD, AL, AF, AA)
            print(ma.predict()+"\n")
    if not statues:
        search_again=input("no match found in your date\ndo you want to search again(y/n)")
        search_again=search_again.lower()
        if search_again=="y":
            match_making()
        else:
            exit()


match_making()


