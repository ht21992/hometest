import numpy as np
import pandas as pd
from scipy.stats import poisson
import matplotlib.pyplot as plt
def drandom():
    pmass=[0.2,0.4,0.1,0.3]
    var,pp,u=0,pmass[0],np.random.uniform(0,1)
    while(u>pp):
        var=var+1
        pp=pp+pmass[var]
    return  var

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

def expected_goal():
    standing = pd.read_csv('live_table.csv')
    Home_Team = standing[standing['Team'] == "Watford" ]
    Away_Team = standing[standing['Team']== "Arsenal" ]
    HT,HW,HD,HL,HF,HA=get_Host_stats(Home_Team)
    AT, AW, AD, AL, AF, AA = get_Away_stats(Away_Team)
    """HP:refers to number of all matches which the specific team played as host
       AP: refers to number of all matches which the specific team played as guest"""
    HP=HW+HD+HL
    AP=AW+AD+AL
    """HGR(Home_team Goal Rate):we take the number of goals scored at home this season by Home_team and divide it by number of the home games
       AGR(Away_team Goal Rate):we take the number of goals scored when they were away side this season and divide it by number of the away games
       HCR(Home_team Conceded Rate):we take the number of goals conceded by Home_team when they were home side and divide it by number of the home games
       ACR(Away_team Conceded Rate):we take the number of goals conceded by Away_team when they were away side and divide it by number of the away games"""
    HGR=HF/HP
    AGR=AF/AP
    HCR=HA/HP
    ACR=AA/AP
    """AHG(Avrage Home Goals):we divide the the home goals scored per game during the season by number of all home games 
       AAG(Average Away Goals):we divide the the Away goals scored per game during the season by number of all away games 
       AHC(Average Home Conceded):  we divide the conceded goals scored per game during the season by number of all Home games
       AAC(Avrage Away Conceded):we divide the conceded goals scored per game during the season by number of all away games"""
    AHG=sum(standing["HF"])/(sum(standing["HW"])+sum(standing["HD"])+sum(standing["HL"]))
    AAG=sum(standing["AF"])/(sum(standing["AW"])+sum(standing["AD"])+sum(standing["AL"]))
    AHC=sum(standing["HA"])/(sum(standing["HW"])+sum(standing["HD"])+sum(standing["HL"]))
    AAC=sum(standing["AA"])/(sum(standing["AW"])+sum(standing["AD"])+sum(standing["AL"]))
    """HTAS:(Home Team Attack Strength)
       HTDS:(Home Team Defance Strength)
       ATAS:(Away Team Attack Strength)
       ATDS:(Away Team Defance Strength)"""
    HTAS=HGR/AHG
    HTDS=HCR/AHC
    ATAS=AGR/AAG
    ATDS=ACR/AAC
    """excpected_goal_for_Home_team: multiplication between Home Team Attack Strength and Away Team Defance Strength and Avrage Home Goals
       excpected_goal_for_Away_team:multiplication between Away Team Attack Strength and Home Team Defance Strength and Avrage Away Goals
       and we use it in poisson calculator """
    excpected_goal_for_Home_team=HTAS*ATDS*AHG
    excpected_goal_for_Away_team=ATAS*HTDS*AAG
    i=np.arange(0,6)
    Home_Team_goal_probability= poisson.pmf(i, excpected_goal_for_Home_team)
    Away_Team_Team_goal_probability = poisson.pmf(i, excpected_goal_for_Away_team)
    fig=plt.figure(figsize=(10,6))
    fig.suptitle("Goal probability\n"+HT+" Vs "+AT)
    ax = fig.add_subplot(221)
    ax.set(title=HT,xlabel="Number of Goals",ylabel="Probability")
    ax1 = fig.add_subplot(222)
    ax1.set(title=AT, xlabel="Number of Goals", ylabel="Probability")
    ax.bar(i,Home_Team_goal_probability,label=HT,color="blue")
    ax1.bar(i,Away_Team_Team_goal_probability,label=AT,color="red")
    fig.legend()
    data={'Goals':[0,1,2,3,4,5],HT:Home_Team_goal_probability,AT:Away_Team_Team_goal_probability}
    df=pd.DataFrame(data)
    df.to_csv("pro.csv")
    plt.show()

    #print(pridected_goal_for_Home_team,pridected_goal_for_Away_team)
    #return pridected_goal_for_Home_team,pridected_goal_for_Away_team

expected_goal()