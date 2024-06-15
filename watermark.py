from turtle import Turtle


class Watermark(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.color("gray")
        self.write("Made by Adarsha", move=True, align="center", font=("arial", 15, "italic"))
