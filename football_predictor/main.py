import prediction
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import socket


LabelBase.register(name="ChunkFive",fn_regular="Chunkfive.otf")
class Screenmanagement(ScreenManager):
    pass
class Popup_Window(Popup):
    pass
class Network_Popup(Popup):
    pass
class Home_Screen(Screen):
    def conection(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            NP = Network_Popup()
            NP.open()
            return False

class About_Screen(Screen):
    pass
class Start_Screen(Screen):
    values=["select your league"]
    w_graph=''
    g_graph=''
    predictions=''
    statue=''
    def set_initial_form(self):
        self.ids.home_spinner.text = "Home Team"
        self.ids.away_spinner.text = "Away Team"
        self.ids.home_spinner.values = Start_Screen.values
        self.ids.away_spinner.values = Start_Screen.values
        self.ids.Bundes_Liga_T_button.state='normal'
        self.ids.Laliga_T_button.state = 'normal'
        self.ids.Serie_A_T_button.state = 'normal'
        self.ids.PL_T_button.state = 'normal'
        self.ids.bg_pic.source = "start_bg.png"

    def PL_button(self):
        PL=FootballPredictionApp.PL
        self.ids.bg_pic.source = "PL_bg.png"
        self.ids.home_spinner.text = "Home Team"
        self.ids.away_spinner.text = "Away Team"
        self.ids.home_spinner.values=PL
        self.ids.away_spinner.values = PL
        Start_Screen.statue="PL"


    def Serie_A_button(self):
        serie_a=FootballPredictionApp.serie_a
        self.ids.bg_pic.source = "seria_A.jpg"
        self.ids.home_spinner.text = "Home Team"
        self.ids.away_spinner.text = "Away Team"
        self.ids.home_spinner.values=serie_a
        self.ids.away_spinner.values = serie_a
        Start_Screen.statue="Serie_A"


    def Bundes_Liga_button(self):
        bundes_liga=FootballPredictionApp.bundes_liga
        self.ids.bg_pic.source = "bundesliga_bg.jpg"
        Start_Screen.statue = "BundesLiga"
        self.ids.home_spinner.text = "Home Team"
        self.ids.away_spinner.text = "Away Team"
        self.ids.home_spinner.values = bundes_liga
        self.ids.away_spinner.values = bundes_liga


    def Laliga_Button(self):
        la_liga=FootballPredictionApp.la_liga
        self.ids.bg_pic.source = "laliga_bg.png"
        self.ids.home_spinner.text = "Home Team"
        self.ids.away_spinner.text = "Away Team"
        self.ids.home_spinner.values = la_liga
        self.ids.away_spinner.values = la_liga
        Start_Screen.statue = "LaLiga"



    def check_teams(self):
        if self.ids.home_spinner.text == "Home Team" or self.ids.away_spinner.text == "Away Team" or self.ids.home_spinner.text == "select your league" or self.ids.away_spinner.text == "select your league" :
            PW = Popup_Window()
            PW.open()
        else:
            return True

    def calculate_result(self):
        hs = Home_Screen()
        if hs.conection():
            if self.check_teams():
                if Start_Screen.statue=="PL":
                    fig, fig1, prediction_result = prediction.PremierLeague(self.ids.home_spinner.text, self.ids.away_spinner.text)
                    Start_Screen.w_graph = fig1
                    Start_Screen.g_graph = fig
                    Start_Screen.predictions = prediction_result
                elif Start_Screen.statue=="Serie_A":
                    fig, fig1, prediction_result = prediction.Serie_A_Italy(self.ids.home_spinner.text, self.ids.away_spinner.text)
                    Start_Screen.w_graph = fig1
                    Start_Screen.g_graph = fig
                    Start_Screen.predictions = prediction_result
                elif Start_Screen.statue == "BundesLiga":
                    fig, fig1, prediction_result = prediction.Bundesliga(self.ids.home_spinner.text, self.ids.away_spinner.text)
                    Start_Screen.w_graph = fig1
                    Start_Screen.g_graph = fig
                    Start_Screen.predictions = prediction_result
                elif Start_Screen.statue == "LaLiga":
                    fig, fig1, prediction_result = prediction.La_liga(self.ids.home_spinner.text, self.ids.away_spinner.text)
                    Start_Screen.w_graph = fig1
                    Start_Screen.g_graph = fig
                    Start_Screen.predictions = prediction_result
                else:
                    PW = Popup_Window(text="Something is wrong.Please Try again later")
                    PW.open()

class Result_Screen(Screen):
    def on_pre_leave(self, *args):
        lbl=self.ids.test_lbl
        lbl.text = "Please select from the task bar above"
        draw = self.ids.draw_layout
        draw.clear_widgets()
        draw.add_widget(lbl)

    def show_goal_graph(self):
        draw = self.ids.draw_layout
        draw.clear_widgets()
        draw.add_widget(FigureCanvasKivyAgg(Start_Screen.g_graph))
    def show_win_graph(self):
        draw=self.ids.draw_layout
        draw.clear_widgets()
        draw.add_widget(FigureCanvasKivyAgg(Start_Screen.w_graph))
    def show_predictions(self):
        draw = self.ids.draw_layout
        draw.clear_widgets()
        draw.add_widget(Label(text=Start_Screen.predictions,font_size="20dp",font_name='ChunkFive'))


class FootballPredictionApp(App):
    PL=[]
    bundes_liga=[]
    serie_a=[]
    la_liga=[]
    def on_start(self):
        hs=Home_Screen()
        if hs.conection():
            FootballPredictionApp.PL = prediction.get_premier_league()
            FootballPredictionApp.bundes_liga=prediction.get_bundesliga()
            FootballPredictionApp.la_liga=prediction.get_laliga()
            FootballPredictionApp.serie_a=prediction.get_serie_A()



if __name__=="__main__":
   FootballPredictionApp().run()



