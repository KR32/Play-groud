# Create a Class with instance attributes

class Bird:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def sing(self):
        print(f"{self.name} is a bird")

    def fly(self):
        print(f"{self.name} can fly")


class Dove(Bird):
    def fly(self):
        print(f"{self.name} can fly")


class Eagle(Bird):
    def __init__(self, name, age, color, wingspan):
        super().__init__(name, age, color)
        self.wingspan = wingspan

    def fly(self):
        print("I can fly too high")

dove = Dove("Dove", 1, "white")
dove.fly()

eagle = Eagle("Eagle", 2, "black", 10)
eagle.fly()


