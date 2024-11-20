class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


    def Honor_Roll(self):
        if self.gpa > 4.0:
            return True
        else:
            return False

