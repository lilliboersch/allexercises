try:
    age=int(input("What is your age? "))
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    print("Your age is", age)