from shlex import join

this = {"apple", "banana", "cherry", True, 1, 2}
print(len(this))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(type(this))

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print("banana" not in thisset)

jet1 = {"benz", "bmw", "audi"}
jet2 = {"toyota", "subaru", "mazda"}
jet3 = jet1.union(jet2)
jet4 = {"simba", "ndovu", "paka"}
jet5 = jet1 | jet2 | jet3 | jet4
print(jet5)
