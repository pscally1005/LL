#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# x = 10 / 0

# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
# try:
#     x = 10 / 0
# except:
#     print("ERROR")

# TODO: You can also catch specific exceptions
try:
    answer = input("What should I divide 10 by? ")
    num = float(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("ERROR: Cannot divide by zero")
except ValueError as e:
    print("ERROR: Input is invalid")
    print(e)
finally:
    print("This will always run")