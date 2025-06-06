from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.teleport(0, 270)
        self.write(arg=f"Score: {self.score}",
                    move=False,
                   align=ALIGNMENT,
                   font=FONT)
        self.teleport(0, 250)
        self.write(arg="-" * 60,
                   move=False,
                   align="center",
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.teleport(0,0)
        self.write(arg=f"GAME OVER",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)
        self.teleport(0, -20)
        self.write(arg=f"Final core: {self.score}",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)
