import random


class Student
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("time to chill")
        self.progress -= 0.1
        self.gladness -= 5

    def is_alive(self):
         if self.progress < -0.5:
             print("Cast out")
             self.alive = false
         elif self.gladness <= 0:
             print("Depresion")
             self.alive = false
         elif self.progress > 5:
             print("Passed externally...")
             self.alive = false

    def end_of_day(self):
        print("f"Gladness = {"self.gladness}"}
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day ="day" + str(day) + "of" + self.name + "lefe"
        print(f"{day:=^50}")