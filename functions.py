# function methods
import greet

with open("temp.txt", "w") as file:
    file.write("99.34\n")
    file.write("120\n")
    file.write("57.36\n")

with open("temp.txt", "r") as file:
    content = file.read()
    print(content)

greet()