"""In this project, we get 3 arguments of user from cli.
 respectivelly command, number 1 and number 2. Then do command with to
 numbers and print full answer in cli. commands are:
 [add, minus, multiplication, division, power, remaining]"""


import sys

# get command and numbers from user(cli)
inputs = sys.argv
command = inputs[1].lower()
number_1 = float(inputs[2])
number_2 = float(inputs[3])


# use "if statment" to check which command is entred by user
if command in ["+", "add", "a", "-a"]:
    print(f"{number_1} + {number_2} = {number_1 + number_2}")

elif command in ["-", "minus", "mn", "-mn"]:
    print(f"{number_1} - {number_2} = {number_1 - number_2}")
    print(f"{number_2} - {number_1} = {number_2 - number_1}")

elif command in ["multiplicaation", "ml", "-ml"]:  # * operator is meaningfull in cli
    print(f"{number_1} * {number_2} = {number_1 * number_2}")

elif command in ["/", "dvision", "d", "-d"]:
    print(f"{number_1} / {number_2} = {number_1 / number_2}")
    print(f"{number_2} / {number_1} = {number_2 / number_1}")

elif command in ["%", "eamaining", "r", "-r"]:
    print(f"{number_1} % {number_2} = {number_1 % number_2}")
    print(f"{number_2} % {number_1} = {number_2 % number_1}")

elif command in ["power", "p", "-p"]:  # ** operator is meaningfull in cli
    print(f"{number_1} ** {number_2} = {number_1 ** number_2}")
    print(f"{number_2} ** {number_1} = {number_2 ** number_1}")

else:
    print(f"{command} {number_1} {number_2} => error")
