from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Courier', 24,'bold'))



    def show_score(self):
        self.score +=1
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Courier', 24,'bold'))



    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align='center',
                   font=('Courier', 24, 'bold'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER", align='center', font=('Courier', 24,'bold'))


