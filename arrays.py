ages = [21, 28, 30, 12, 67, 54, 96, 87]

names = ["Jane", "Eddie", "Patience", "Eddie", "Judy", "Eddie", "Claire", "Eddie"]

ages.append(32)
# ages.clear()
# ages.sort()
# ages.reverse()
print(ages)

# names.sort()
# print(names)

# eddie_count = names.count("Eddie")
# print(eddie_count)
#
# print(len(names))
# print(len(ages))
# print(sum(ages))
#
# print(sum(ages)/len(ages))
# print(123/5)
#
# print(ages[0]) #index
#
# print(names [-1]) #python specific
# print(ages[3:5]) #slicing
# print(ages[:5])
# print(ages[::-1])
#
# set
scores = {87, 73, 67, 65, 73}  # removes duplicates
print(scores)
scores.add(90)
scores.remove(65)
print(scores)

# tuple immutable
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays[0])

# dictionary
person = {"name": "George", "age": 23, "height": 170}
print(person["name"])
print(person["age"])
print(person["height"])

people = [
    {"name": "Victor", "age":20,},
    {"name": "John", "age":21},
    {"name":"Ryan", "age":17}
]
print(people[2]["name"])
