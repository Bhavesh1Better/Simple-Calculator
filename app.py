x = input("Enter a number: ")
y = input("Enter another number: ")
z = input("What operation would you like to perform? (+, -, *, /): ")
if z == "+":
    print("The result is: ", int(x) + int(y))
elif z == "-":
    print("The result is: ", int(x) - int(y))
elif z == "*":
    print("The result is: ", int(x) * int(y))
elif z == "/":
    print("The result is: ", int(x) / int(y))
else:
    print("Please enter a valid input for the operation.")
