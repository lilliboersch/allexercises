try:
    age= int(input("How old are you?"))
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    #Do some sanity checks on age
    if age < 0:
        print("I am sorry, but you are age cannot be negative")
    elif age > 130:
        print("I am sorry, but you age cannot be greater than 130")
    elif 130 > age > 0:
        print("Thank you for playing, you are", age, "years old")