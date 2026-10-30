# object projected programming
# classes

class Person:
    # constructor
    def __init__(self, name, dob, color, weight, height):
        self.name = name
        self.dob = dob
        self.color = color
        self.weight = weight
        self.height = height

    def display(self):
        print(f"Name is {self.name} and DOB is {self.dob}")

    def get_bmi(self):
        result = self.weight / self.height ** 2
        return round(result, 2)


# blueprint for creating objects
# name class using uppercase

p1 = Person("Alfred Kinuthia", "17-08-2004", "Black", "72", "1.79")
p2 = Person("Leslie Mong'ina", "17-12-2007", "Black", "60", "1.65")

p1.display()
p2.display()

print(f"{p1.name} bmi is {p1.get_bmi()}")
print(f"{p2.name} bmi is {p2.get_bmi()}")
