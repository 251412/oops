class Student:
    def __init__(self):
        self.__marks = 0
    def set_marks(self,value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks.")
    def get_marks(self):
        return self.__marks
s=Student()
s.set_marks(95)
print(s.get_marks())
    