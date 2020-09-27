# def multiply(*numbers):
# total = 1
# for item in numbers:
#     total *= item
# return total

"""
numberss = ["ali", "amir"]
sum = 0

for item in "python":
    print(item)
"""


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("fiz-buz")

    elif number % 3 == 0:
        print("fiz")

    elif number % 5 == 0:
        print("buz")

    elif number % 3 != 0 or number % 5 != 0 or number % 15 != 0:
        print(number)


fizz_buzz(4)
