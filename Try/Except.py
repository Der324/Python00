# Try except!

try:
        answer = 10/20
        number = int(input("Enter a number: "))
        print(number)
except ZeroDivisionError as err:
        print(err)
except ValueError:
        print("invalid input")