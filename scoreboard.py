from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(x=0, y=280)
        self.write(arg=f"Score: {self.score}", align='center', font=('Arial', 12,'bold'))



    def show_score(self):
        self.score +=1
        self.clear()
        self.write(arg=f"Score {self.score}", align='center', font=('Arial', 12,'bold'))

