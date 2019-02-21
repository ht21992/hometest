import random
import time
class Bot1:
    say_hi=False
    lines=0
    def __init__(self,askquestion,greet):
        self.askquestion=askquestion
        self.greet=greet
    def ask(self):
        if Bot1.lines==10:
            print("BOT1: bye")
            return "bye"
        if Bot1.say_hi==True:
            Bot1.lines+=2
            random_ask=random.randint(0,len(self.askquestion)-1)
            print("BOT1: "+self.askquestion[random_ask])
            return self.askquestion[random_ask]
        else:
            Bot1.say_hi=True
            random_greet=random.randint(0,len(self.greet)-1)
            print("BOT1: "+self.greet[random_greet])
            return self.greet[random_greet]



class Bot2:
    def __init__(self, standardanswer, questionanswer, greetinganswer, farewellanswer):
        self.standardanswer = standardanswer
        self.questionanswer = questionanswer
        self.greetinganswer = greetinganswer
        self.farewellanswer = farewellanswer

    def check_greeting(self, text):
        text = text.lower()
        for greeting in self.greetinganswer:
            if text.__contains__(greeting):
                return True

    def check_farewell(self, text):
        text = text.lower()
        for farewell in self.farewellanswer:
            if text.__contains__(farewell):
                return True
    def reply(self,text):
        if self.check_farewell(text):
            random_ans = random.randint(0, len(self.farewellanswer) - 1)
            print("BOT2: "+self.farewellanswer[random_ans])
            exit()
        elif self.check_greeting(text):
            random_ans = random.randint(0, len(self.greetinganswer) - 1)
            print("BOT2: "+self.greetinganswer[random_ans])
        elif "?" in text:
            random_ans=random.randint(0,len(self.questionanswer)-1)
            print("BOT2: "+self.questionanswer[random_ans])
        else:
            random_ans=random.randint(0,len(self.standardanswer)-1)
            print("BOT2: "+self.standardanswer[random_ans])
askquestion=["how is the weather?","how old are you?","where are you ?","are you like me?"]
Greetings=["hello there","hi","greetings","sup","what's up"]
Farewells=["bye","see you later","goodbye"]
Question_ans=["i can not answer that","who knows","i do know"]
standard_ans=["that's good","so sad","intersting"]
chat1=Bot1(askquestion,Greetings)
chat2=Bot2(standard_ans,Question_ans,Greetings,Farewells)
while(True):
    ask=chat1.ask()
    time.sleep(3)
    chat2.reply(ask)
    time.sleep(2)

