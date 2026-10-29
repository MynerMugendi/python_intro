def add(a, b, c):
    res = a + b + c
    return res


def addition(x, *hop):
    total = sum(hop)
    return total
    """
Returns the sum of all the numbers passed as arguments
Parameters:
integers or floats or a mix of integers and floats
Returns:
Integers or floats
    """

def build_profile(**kwargs):  # dict key-word args
    for k, w in kwargs.items():
        print(f"{k} : {w}")


def fancy(name, *hop, **kwargs):
    print(name)
    print(hop)
    print(kwargs)


# anonymous = lambda

# def square(num):
#     return num ** 2
#
# result = square(3)
# print(result)

square = lambda num: num * num
print(square(5))

res = square(2.9)
print(res)

surface_area_cylinder = lambda r, h: 22 / 7 * r ** 2 * 2 + 22 / 7 * 2 * r * h

value = (surface_area_cylinder(2.789, 7.72))
print(value)


people = [
    {"name": "Mufasa", "age": 28},
    {"name": "Scar", "age": 30},
    {"name": "Simba", "age": 18},
]

sorted_by_age = sorted(people, key=lambda x: x["name"], reverse = True)
print(sorted_by_age)
# build_profile(experience=100, name="Jane", age='23', proffesion = "Programming", gender="male")

# call the function
# print(add(9, 7, 5))

# print(addition(6, 7, 3, 1, 7, 8, 9, 78))
