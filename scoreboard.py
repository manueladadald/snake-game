"""Creating scoreboard and adding scoring"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    """Class for the scoreboard"""
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def keep_score(self):
        """Function to keep score"""
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increasing score"""
        self.score += 1

    def game_over(self):
        """Ending the game"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
