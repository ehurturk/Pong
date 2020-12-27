from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, winning_point, point):
        super().__init__()
        self.score = 0
        self.winning_point = winning_point
        self.color("white")
        self.penup()
        self.hideturtle()
        self.xcor = point[0]
        self.ycor = point[1]
        self.goto(self.xcor, self.ycor)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
