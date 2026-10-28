import math


def greet():
    print("hello")


def greeting(name):
    print(f"Hello {name}")


def volume_cylinder(radius, height):
    v = math.pi * radius ** 2 * height
    print(round(v, 4))


def volume_cylinder_better(radius, height):
    v = math.pi * radius ** 2 * height
    return v


def volume_surface(radius, height):
    v = math.pi * radius ** 2 * height
    a = math.pi * radius ** 2 + math.pi * radius * 2 * height
    return v, a


volume, area = volume_surface(13, 7.7)
print(f"volume is {volume} and area is {area}")

# result = volume_cylinder_better(12, 13)
# print(round(result))
#
# with open("volumes.txt", "w") as file:
#     file.write(str(result))
# volume_cylinder(10, 30)
# volume_cylinder(2.67, 3.74)

# greeting('Leslie')
# greeting('Sydney')

# greet() # calling the function no arguments/params

v, a = volume_surface(height=7.7, radius=13)
print(f"volume is {v} and area is {a}")


def divide(x, y, should_round=False):
    ans = x / y
    if should_round == True:
        return round(ans, 1)

    else:
        return ans


print(divide(7, 8, True))


