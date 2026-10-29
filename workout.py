# def add (a,b,c):
#     rs = a + b + c
#     return rs
# print(add(1,2,3))
#
# def build_profile(**kwargs):
#     for k, w in kwargs.items():
#         print(f"{k} : {w}")
#
# build_profile(
#     experience=100,
#     name="Jane",
#     age=23,
#     profession="Programming",
#     gender="male"
# )
#
# def square(num):
#     return num * num
# print(square(9))

# x
class MyClass:
    x = 5
p1 = MyClass()
p3 = MyClass()
p2 = MyClass()

print(p1.x)
print(p3.x)
print(p2.x)

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    # def greet(self):
    #     print("Hello, my name is" + self.name)

p1 = Person("John", 25 )
print(p1.age)

class Person:
    def __init__ (self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Emily")
p2 = Person("Tobias")

print(p1.name, p1.age)
print(p2.name, p2.age)