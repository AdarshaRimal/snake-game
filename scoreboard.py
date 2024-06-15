from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.current_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update()

 

    def update(self):
        self.clear()
        self.write(f"Score  :{self.current_score} High Score : {self.high_score}", move=False, align="center", font=("arial", 15, "normal"))

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")

        self.current_score = 0
        self.update()


    def increase_score(self):
        self.current_score += 1
        self.update()
