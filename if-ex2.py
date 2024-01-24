import random
drinks = ["beer", "wine", "whiskey", "campari", "rum", "gin tonic", "martini", "vodka", "sangria"]

try:
    age = int(input("How old are you?"))
    country = input("Where do you live?")

except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    #Do some sanity checks on age
    if age < 0 or age > 130:
        print("I am sorry, but you are age cannot be negative, or greater than 130")

    elif age < 18:
        print("I am sorry, too young to play this drinking game everywhere")

    elif age < 21 and country =="US":
        print("I am sorry, too young to play this drinking game in the US")
    else:
        drink = random.choice(drinks)
        print("Drink some", drink, ". Thank you for playing, you are", age, "years old")