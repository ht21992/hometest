import random
class ChatBot:
    def __init__(self,standardanswer,questionanswer):
        self.standardanswer=standardanswer
        self.questionanswer=questionanswer
    def reply(self,text):
        if "?" in text:
            random_ans=random.randint(0,len(self.questionanswer)-1)
            print(self.questionanswer[random_ans])
        else:
            random_ans=random.randint(0,len(self.standardanswer)-1)
            print(self.standardanswer[random_ans])
    def learn(self,text):
        if "?" in text:
            self.questionanswer.append(text)
        else:
            self.standardanswer.append(text)




Question_ans=["it's rainy","it's sunny"]
standard_ans=["hello","hi"]
chat1=ChatBot(standard_ans,Question_ans)
chat1.learn("i do not know")
#while True:
    #ans = input()
    #chat1.reply(ans)


#chat1.learn()
