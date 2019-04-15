import requests
import pandas as pd
import numpy as np
import  random
import socket
from scipy.stats import poisson
import matplotlib.pyplot as plt
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
        if x>=-10 and x<=10:
            return self.HT+" will draw with "+self.AT
        elif x>10:
            return self.HT+" will Win "+self.AT
        else:
            return self.HT+" will lose against "+self.AT
    def predict(self):
        inputs = np.array([self.HW,self.HD,self.HL,self.HF,self.HA,self.AW,self.AD,self.AL,self.AF,self.AA])
        WeightsInputToOutput=[2,1,-2,2,-2,-2,1,2,-2,2]
        output = np.dot(WeightsInputToOutput, inputs)
        #print("output: " + str(output))
        return self.activation_function(output)

def is_connected():
    try:
        socket.create_connection(("www.google.com",80))
        return True
    except OSError:
        return False
def get_team_form():
    dic = {}
    changed_name_teams = []
    dfs = pd.read_html('http://www.footstats.co.uk/index.cfm?task=form_basic')
    for df in dfs:
        dic["Pos"] = df["Pos"]
        dic["Team"] = df["Team"]
        dic["P"] = df["P"]
        dic["F"] = df["F"]
        dic["A"] = df["A"]
        dic["Pts"] = df["Pts"]
        dic["Sequence"] = df["Sequence"]
    for team_name in dic["Team"]:
        if team_name == "Man City":
            team_name = team_name.replace("Man City", "Manchester City")
        elif team_name == "Tottenham":
            team_name = team_name.replace("Tottenham", "Tottenham Hotspur")
        elif team_name == "Leicester":
            team_name = team_name.replace("Leicester", "Leicter City")
        elif team_name == "Man United":
            team_name = team_name.replace("Man United", "Manchester United")
        elif team_name == "Newcastle":
            team_name = team_name.replace("Newcastle", "Newcastle United")
        elif team_name == "West Ham":
            team_name = team_name.replace("West Ham", "West Ham United")
        elif team_name == "Wolves":
            team_name = team_name.replace("Wolves", "Wolverhampton Wanderers")
        elif team_name == "Brighton":
            team_name = team_name.replace("Brighton", "Brighton & Hove Albion")
        elif team_name == "Bournemouth":
            team_name = team_name.replace("Bournemouth", "AFC Bournemouth")
        elif team_name == "Huddersfield":
            team_name = team_name.replace("Huddersfield", "Huddersfield Town")
        elif team_name == "Cardiff":
            team_name = team_name.replace("Cardiff", "Cardiff City")
        changed_name_teams.append(team_name)
    dic["Team"] = changed_name_teams
    ad = pd.DataFrame(dic)
    ad.to_csv("team_form.csv")


def update_standings_and_calendar():
    print("Updating...")
    if is_connected():
        url = 'https://www.footballwebpages.co.uk/league-table.csv?comp=1&showHa=yes'
        url2= 'https://www.footballwebpages.co.uk/fixtures-results.csv?comp=1'
        url3='http://www.footstats.co.uk/index.cfm?task=form_basic'
        url_respond = requests.post(url)
        url2_respond=requests.post(url2)
        url3_respond=requests.post(url3)
        if url_respond.ok and url2_respond.ok and url3_respond.ok:
            df = pd.read_csv(url)
            df1=pd.read_csv(url2)
            df.to_csv("live_table.csv")
            df1.to_csv("calendar.csv")
            get_team_form()
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
    print("today is:" + now)
    print("for which date you want the prediction")
    user_date_day = int(input("please enter the day: "))
    user_date_month = int(input("please enter the month: "))
    if user_date_month > 12 or user_date_month < 1:
        print("month is not correct")
    elif user_date_day > 31 or user_date_day < 1:
        print("day is not correct")
    else:
        user_date = str(user_date_day) + "/" + str(user_date_month) + "/" + str(datetime.datetime.now().year)
        print(user_date)
        if user_date<now:
            print("please enter a date for upcoming matches")
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

            predicted_Home_goals,predicted_Away_goals=expected_goal(Home_Team,Away_Team)
            HT,HW,HD,HL,HF,HA=get_Host_stats(Home_Team)
            AT,AW,AD,AL,AF,AA=get_Away_stats(Away_Team)
            ma = Match_Result(HT, HW, HD, HL, HF, HA, AT, AW, AD, AL, AF, AA)
            print("first algorithm prediction: "+ma.predict())
            print("first algorithm prediction: "+HT+" "+str(predicted_Home_goals)+" "+AT+" "+str(predicted_Away_goals)+"\n")
    if not statues:
        search_again=input("no match found in your date\ndo you want to search again(y/n)")
        search_again=search_again.lower()
        if search_again=="y":
            match_making()
        else:
            exit()


def expected_goal(Home_Team,Away_Team):
    standing = pd.read_csv('live_table.csv')
    #Home_Team = standing[standing['Team'] == home_team ]
    #Away_Team = standing[standing['Team']== away_team ]
    HT,HW,HD,HL,HF,HA=get_Host_stats(Home_Team)
    AT, AW, AD, AL, AF, AA = get_Away_stats(Away_Team)
    """HP:refers to number of all matches which the specific team played as host
       AP: refers to number of all matches which the specific team played as guest"""
    HP=HW+HD+HL
    AP=AW+AD+AL
    """HGR(Home_team Goal Rate):we take the number of goals scored at home this season by Home_team and divide it by number of the home games
       AGR(Away_team Goal Rate):we take the number of goals scored when they were away side this season and divide it by number of the away games
       HCR(Home_team Conceded Rate):we take the number of goals conceded by Home_team when they were home side and divide it by number of the home games
       ACR(Away_team Conceded Rate):we take the number of goals conceded by Away_team when they were away side and divide it by number of the away games
       """
    HGR=HF/HP
    AGR=AF/AP
    HCR=HL/HP
    ACR=AL/AP
    """AHG(Avrage Home Goals):we divide the the home goals scored per game during the season by number of all home games 
       AAG(Average Away Goals):we divide the the Away goals scored per game during the season by number of all away games 
       AHC(Average Home Conceded):  we divide the conceded goals scored per game during the season by number of all Home games
       AAC(Avrage Away Conceded):we divide the conceded goals scored per game during the season by number of all away games"""
    AHG=sum(standing["HF"])/(sum(standing["HW"])+sum(standing["HD"])+sum(standing["HL"]))
    AAG=sum(standing["AF"])/(sum(standing["AW"])+sum(standing["AD"])+sum(standing["AL"]))
    AHC=sum(standing["HL"])/(sum(standing["HW"])+sum(standing["HD"])+sum(standing["HL"]))
    AAC=sum(standing["AL"])/(sum(standing["AW"])+sum(standing["AD"])+sum(standing["AL"]))
    """HTAS:(Home Team Attack Strength)
       HTDS:(Home Team Defance Strength)
       ATAS:(Away Team Attack Strength)
       ATDS:(Away Team Defance Strength)"""
    HTAS=HGR/AHG
    HTDS=AGR/AHC
    ATAS=HCR/AAG
    ATDS=ACR/AAC
    """pridected_goal_for_Home_team: multiplication between Home Team Attack Strength and Away Team Defance Strength and Avrage Home Goals
       pridected_goal_for_Away_team:multiplication between Away Team Attack Strength and Home Team Defance Strength and Avrage Away Goals
       and we use it in poisson calculator """
    pridected_goal_for_Home_team=poisson.rvs(mu=HTAS*ATDS*AHG,random_state=1)
    pridected_goal_for_Away_team=poisson.rvs(mu=ATAS*HTDS*AAG,random_state=1)
    return pridected_goal_for_Home_team,pridected_goal_for_Away_team

match_making()
