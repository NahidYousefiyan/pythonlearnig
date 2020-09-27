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
        return("fiz-buz")

    if number % 3 == 0:
        return("fiz")

    if number % 5 == 0:
        return("buz")

    return(number)


print(fizz_buzz(4))
