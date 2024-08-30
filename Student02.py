#using class student to create object function.


class Student:
    def __init__(self, name, major, gpa, position):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.position = position

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
    def on_position_roll(self):
        if self.position >= 10:
            return True
        else:
            return False