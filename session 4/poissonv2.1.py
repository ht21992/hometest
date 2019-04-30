import numpy as np
import pandas as pd
from scipy.stats import poisson
import matplotlib.pyplot as plt

def get_Host_stats(Team):
    list_to_drop = ['WWin', 'DDraw', 'LLoss', 'GDGoal Difference (GD).Goals Scored - Goals Conceded', 'Pts', 'Last 5',
                    'PPG',
                    'CSClean Sheets (CS).Table of teams with the highest number of matches where they conceded 0 goals. Stats are taken from League runs only.* Team must have played a minimum of 7 matches before they qualify for this CS table.',
                    "BTTSBoth Teams To Score (BTTS).List of teams with the highest number of matches where both teams scored. Stats from team's Domestic League runs only.* Team must have played a minimum of 7 matches before they qualify for this BTTS table.",
                    'FTSFailed to Score (FTS).Matches where this team failed to score.',
                    'Yellow Card / Red Card', 'Corners / match',
                    '1.5+Over 1.5 (1.5+).The number or percent of matches where the total goals ended above 1.5 (ie: 2, 3, or 4 goals)',
                    '2.5+Over 2.5 (2.5+).The number or percent of matches where the total goals ended above 2.5 (ie: 3, 4, or 5 goals)',
                    'AVGAverage Goals Per Match (AVG).The average number of total goals per match.Calculated across this season.']
    Team=Team.drop(list_to_drop,axis=1)
    print (Team.values)
    name=Team.values[0,2]
    Host_Total_matches=Team.values[0,3]
    #Host_win=Team.values[0,2]
    #Host_draw=Team.values[0,3]
    #Host_loss=Team.values[0,4]
    Host_goals_for=Team.values[0,4]
    Host_goals_against=Team.values[0,5]
    return name,Host_Total_matches, Host_goals_for, Host_goals_against


def get_Away_stats(Team):
    list_to_drop = ['WWin', 'DDraw', 'LLoss', 'GDGoal Difference (GD).Goals Scored - Goals Conceded', 'Pts', 'Last 5',
                    'PPG',
                    'CSClean Sheets (CS).Table of teams with the highest number of matches where they conceded 0 goals. Stats are taken from League runs only.* Team must have played a minimum of 7 matches before they qualify for this CS table.',
                    "BTTSBoth Teams To Score (BTTS).List of teams with the highest number of matches where both teams scored. Stats from team's Domestic League runs only.* Team must have played a minimum of 7 matches before they qualify for this BTTS table.",
                    'FTSFailed to Score (FTS).Matches where this team failed to score.',
                    'Yellow Card / Red Card', 'Corners / match',
                    '1.5+Over 1.5 (1.5+).The number or percent of matches where the total goals ended above 1.5 (ie: 2, 3, or 4 goals)',
                    '2.5+Over 2.5 (2.5+).The number or percent of matches where the total goals ended above 2.5 (ie: 3, 4, or 5 goals)',
                    'AVGAverage Goals Per Match (AVG).The average number of total goals per match.Calculated across this season.']
    Team = Team.drop(list_to_drop, axis=1)
    print (Team.values)
    name = Team.values[0, 2]
    Away_Total_matches = Team.values[0, 3]
    #Away_win = Team.values[0, 2]
    #Away_draw = Team.values[0, 3]
    #Away_loss = Team.values[0, 4]
    Away_goals_for = Team.values[0, 4]
    Away_goals_against = Team.values[0, 5]
    return name,Away_Total_matches , Away_goals_for, Away_goals_against


def calculation_team_stregnth(Home_Team,Away_Team,AHG,AAG,AHC,AAC):
    HT, HP,HF, HA = get_Host_stats(Home_Team)
    AT, AP, AF, AA = get_Away_stats(Away_Team)
    """HGR(Home_team Goal Rate):we take the number of goals scored at home this season by Home_team and divide it by number of the home games
    AGR(Away_team Goal Rate):we take the number of goals scored when they were away side this season and divide it by number of the away games
    HCR(Home_team Conceded Rate):we take the number of goals conceded by Home_team when they were home side and divide it by number of the home games
    ACR(Away_team Conceded Rate):we take the number of goals conceded by Away_team when they were away side and divide it by number of the away games"""
    HGR = HF / HP
    AGR = AF / AP
    HCR = HA / HP
    ACR = AA / AP
    """HTAS:(Home Team Attack Strength)
           HTDS:(Home Team Defance Strength)
           ATAS:(Away Team Attack Strength)
           ATDS:(Away Team Defance Strength)"""
    HTAS = HGR / AHG
    HTDS = HCR / AHC
    ATAS = AGR / AAG
    ATDS = ACR / AAC
    """excpected_goal_for_Home_team: multiplication between Home Team Attack Strength and Away Team Defance Strength and Avrage Home Goals
       excpected_goal_for_Away_team:multiplication between Away Team Attack Strength and Home Team Defance Strength and Avrage Away Goals
       and we use it in poisson calculator """
    excpected_goal_for_Home_team = HTAS * ATDS * AHG
    excpected_goal_for_Away_team = ATAS * HTDS * AAG
    i = np.arange(0, 6)
    Home_Team_goal_probability = poisson.pmf(i, excpected_goal_for_Home_team)
    Away_Team_Team_goal_probability = poisson.pmf(i, excpected_goal_for_Away_team)
    """HG:our prediction for Home_team Goals in this match
       AG:our prediction for Away_team Goals in this match"""
    results, max, HG, AG, max2, HG2, AG2, max3, HG3, AG3, both_team_to_score = result_percentage_and_prediction(
        Home_Team_goal_probability, Away_Team_Team_goal_probability)
    labels = [HT + " Win", "Draw", AT + " Win"]
    fig = plt.figure(figsize=(10, 6))
    fig.suptitle("Goal probability\n" + HT + " Vs " + AT)
    ax = fig.add_subplot(221)
    ax.set(title=HT, xlabel="Number of Goals", ylabel="Probability")
    ax1 = fig.add_subplot(222)
    ax1.set(title=AT, xlabel="Number of Goals", ylabel="Probability")
    ax2 = fig.add_subplot(223)
    ax.bar(i, Home_Team_goal_probability, color="Blue")
    ax1.bar(i, Away_Team_Team_goal_probability, color="Green")
    ax2.pie(results, labels=labels, shadow=True, autopct='%1.1f%%')
    plt.text(3.3, 0.001,
             "Highest possibilities:\n" + HT + " " + str(HG) + " " + AT + " " + str(AG) + "   possibility: " + str(
                 max) + "%\n" +
             HT + " " + str(HG2) + " " + AT + " " + str(AG2) + "   possibility: " + str(max2) + "%\n" +
             HT + " " + str(HG3) + " " + AT + " " + str(AG3) + "   possibility: " + str(max3) + "%\n" +
             "Both Teams to score: " + str(both_team_to_score) + "%\n")

    fig.legend()
    plt.show()


def result_percentage_and_prediction(Home_Team_goal_probability, Away_Team_Team_goal_probability):
    Home_Win = 0
    Draw = 0
    Away_win = 0
    both_team_to_score = 0
    results = []
    """we collect all the result probabilities on all_results list and home and away lists storing number of goals for specific probability"""
    all_results = []
    home = []
    away = []
    for i in range(1, len(Home_Team_goal_probability)):
        for j in range(1, len(Away_Team_Team_goal_probability)):
            temp = (Home_Team_goal_probability[i] * Away_Team_Team_goal_probability[j]) * 100
            both_team_to_score += temp
    for i in range(len(Home_Team_goal_probability)):
        for j in range(len(Away_Team_Team_goal_probability)):
            result = (Home_Team_goal_probability[i] * Away_Team_Team_goal_probability[j]) * 100
            all_results.append(result)
            home.append(i)
            away.append(j)
            if i > j:
                temp = (Home_Team_goal_probability[i] * Away_Team_Team_goal_probability[j]) * 100
                Home_Win += temp
            if i == j:
                temp = (Home_Team_goal_probability[i] * Away_Team_Team_goal_probability[j]) * 100
                Draw += temp
            if i < j:
                temp = (Home_Team_goal_probability[i] * Away_Team_Team_goal_probability[j]) * 100
                Away_win += temp
    """now we are trying to find three highest probabilities.

       HG: Home_team Goals in this match for specific probability
       AG: Away_team Goals in this match for specific probability
       max_prob:maximum probability"""
    mapped = zip(all_results, home, away)
    mapped = set(mapped)
    maximum_probaility_and_goals1 = max(mapped)
    mapped.remove(maximum_probaility_and_goals1)
    maximum_probaility_and_goals2 = max(mapped)
    mapped.remove(maximum_probaility_and_goals2)
    maximum_probaility_and_goals3 = max(mapped)
    mapped.remove(maximum_probaility_and_goals3)
    max_prob1 = maximum_probaility_and_goals1[0]
    HG = maximum_probaility_and_goals1[1]
    AG = maximum_probaility_and_goals1[2]
    max_prob2 = maximum_probaility_and_goals2[0]
    HG2 = maximum_probaility_and_goals2[1]
    AG2 = maximum_probaility_and_goals2[2]
    max_prob3 = maximum_probaility_and_goals3[0]
    HG3 = maximum_probaility_and_goals3[1]
    AG3 = maximum_probaility_and_goals3[2]

    results.append(Home_Win)
    results.append(Draw)
    results.append(Away_win)
    max_prob1 = round(max_prob1, 2)
    max_prob2 = round(max_prob2, 2)
    max_prob3 = round(max_prob3, 2)
    both_team_to_score = round(both_team_to_score, 2)
    return results, max_prob1, HG, AG, max_prob2, HG2, AG2, max_prob3, HG3, AG3, both_team_to_score


def PremierLeague():
    #premierleague_table=pd.read_html("https://footballdatabase.com/league-scores-tables/england-premier-league-2018-19")
    premierleague_table=pd.read_html("https://footystats.org/england/premier-league/home-away-league-table")
    #Total_premierleague_table=premierleague_table[0]
    Home_premierleague_table=premierleague_table[0]
    Away_premierleague_table=premierleague_table[1]
    Home_Team = Home_premierleague_table[Home_premierleague_table["Team"] == "Manchester United FC"]
    Away_Team = Away_premierleague_table[Away_premierleague_table['Team'] == "Chelsea FC"]
    """AHG(Avrage Home Goals):we divide the total home goals scored per game during the season by number of all home games 
       AAG(Average Away Goals):we divide the total Away goals scored per game during the season by number of all away games 
       AHC(Average Home Conceded):  we divide the conceded goals scored per game during the season by number of all Home games
       AAC(Avrage Away Conceded):we divide the conceded goals scored per game during the season by number of all away games"""
    AHG = sum(Home_premierleague_table['GFGoals For (GF).The number of goals thisteam have scored.']) / (sum(Home_premierleague_table['MPMatches Played this season']))
    AAG = sum(Away_premierleague_table['GFGoals For (GF).The number of goals thisteam have scored.']) / (sum(Away_premierleague_table['MPMatches Played this season']))
    AHC = sum(Home_premierleague_table['GAGoals Against (GA).The number of goals thisteam have conceded.']) / (sum(Home_premierleague_table['MPMatches Played this season']))
    AAC = sum(Away_premierleague_table['GAGoals Against (GA).The number of goals thisteam have conceded.']) / ((sum(Away_premierleague_table['MPMatches Played this season'])))
    calculation_team_stregnth(Home_Team,Away_Team,AHG,AAG,AHC,AAC)
def Serie_A_Italy():
    serie_a_italy_table = pd.read_html("https://footystats.org/italy/serie-a/home-away-league-table")
    Home_serie_a_italy_table = serie_a_italy_table[0]
    Away_serie_a_italy_table = serie_a_italy_table[1]
    Home_Team = Home_serie_a_italy_table[Home_serie_a_italy_table["Team"] == "Torino FC"]
    Away_Team = Away_serie_a_italy_table[Away_serie_a_italy_table['Team'] == "AC Milan"]
    AHG = sum(Home_serie_a_italy_table['GFGoals For (GF).The number of goals thisteam have scored.']) / (sum(Home_serie_a_italy_table['MPMatches Played this season']))
    AAG = sum(Away_serie_a_italy_table['GFGoals For (GF).The number of goals thisteam have scored.']) / (sum(Away_serie_a_italy_table['MPMatches Played this season']))
    AHC = sum(Home_serie_a_italy_table['GAGoals Against (GA).The number of goals thisteam have conceded.']) / (sum(Home_serie_a_italy_table['MPMatches Played this season']))
    AAC = sum(Away_serie_a_italy_table['GAGoals Against (GA).The number of goals thisteam have conceded.']) / ((sum(Away_serie_a_italy_table['MPMatches Played this season'])))
    calculation_team_stregnth(Home_Team, Away_Team, AHG, AAG, AHC, AAC)
def Bundesliga():
    bundesliga_table = pd.read_html("https://footystats.org/germany/bundesliga/home-away-league-table")
    Home_bundesliga_table = bundesliga_table[0]
    Away_bundesliga_table = bundesliga_table[1]
    Home_Team = Home_bundesliga_table[Home_bundesliga_table["Team"] == "1. FC Nürnberg"]
    Away_Team = Away_bundesliga_table[Away_bundesliga_table['Team'] == "FC Bayern München"]
    AHG = sum(Home_bundesliga_table['GFGoals For (GF).The number of goals thisteam have scored.']) / (sum(Home_bundesliga_table['MPMatches Played this season']))
    AAG = sum(Away_bundesliga_table['GFGoals For (GF).The number of goals thisteam have scored.']) / (sum(Away_bundesliga_table['MPMatches Played this season']))
    AHC = sum(Home_bundesliga_table['GAGoals Against (GA).The number of goals thisteam have conceded.']) / (sum(Home_bundesliga_table['MPMatches Played this season']))
    AAC = sum(Away_bundesliga_table['GAGoals Against (GA).The number of goals thisteam have conceded.']) / ((sum(Away_bundesliga_table['MPMatches Played this season'])))
    calculation_team_stregnth(Home_Team, Away_Team, AHG, AAG, AHC, AAC)
def La_liga():
    la_liga_table=pd.read_html("https://footystats.org/spain/la-liga/home-away-league-table")
    Home_la_liga_table = la_liga_table[0]
    Away_la_liga_table = la_liga_table[1]
    Home_Team = Home_la_liga_table[Home_la_liga_table["Team"] == "Rayo Vallecano"]
    Away_Team = Away_la_liga_table[Away_la_liga_table['Team'] == "Real Madrid CF"]
    AHG = sum(Home_la_liga_table['GFGoals For (GF).The number of goals thisteam have scored.']) / (sum(Home_la_liga_table['MPMatches Played this season']))
    AAG = sum(Away_la_liga_table['GFGoals For (GF).The number of goals thisteam have scored.']) / (sum(Away_la_liga_table['MPMatches Played this season']))
    AHC = sum(Home_la_liga_table['GAGoals Against (GA).The number of goals thisteam have conceded.']) / (sum(Home_la_liga_table['MPMatches Played this season']))
    AAC = sum(Away_la_liga_table['GAGoals Against (GA).The number of goals thisteam have conceded.']) / ((sum(Away_la_liga_table['MPMatches Played this season'])))
    calculation_team_stregnth(Home_Team, Away_Team, AHG, AAG, AHC, AAC)


def Iran_pro_league():
    iran_pro_table = pd.read_html("https://footystats.org/iran/persian-gulf-pro-league/home-away-league-table")
    Home_iran_pro_table = iran_pro_table[0]
    Away_iran_pro_table = iran_pro_table[1]
    Home_Team = Home_iran_pro_table[Home_iran_pro_table["Team"] == "Esteghlal FC"]
    Away_Team = Away_iran_pro_table[Away_iran_pro_table['Team'] == "Foolad Mobarakeh Sepahan SC"]
    AHG = sum(Home_iran_pro_table['GFGoals For (GF).The number of goals thisteam have scored.']) / (sum(Home_iran_pro_table['MPMatches Played this season']))
    AAG = sum(Away_iran_pro_table['GFGoals For (GF).The number of goals thisteam have scored.']) / (sum(Away_iran_pro_table['MPMatches Played this season']))
    AHC = sum(Home_iran_pro_table['GAGoals Against (GA).The number of goals thisteam have conceded.']) / (sum(Home_iran_pro_table['MPMatches Played this season']))
    AAC = sum(Away_iran_pro_table['GAGoals Against (GA).The number of goals thisteam have conceded.']) / ((sum(Away_iran_pro_table['MPMatches Played this season'])))
    calculation_team_stregnth(Home_Team, Away_Team, AHG, AAG, AHC, AAC)



#PremierLeague()
#Serie_A_Italy()
#Bundesliga()
#Iran_pro_league()
#La_liga()
fix = pd.read_html("https://footystats.org/england/premier-league/matches")
a=fix[70]
print(a["Home"])