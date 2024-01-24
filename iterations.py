import random
lives = 3

while lives > 0:
    print("You have", lives, "lives left")
    dice_roll = random.randint(1,6)
    if dice_roll == 6:
        print("You rolled a 6, you win!")
        break #no need for else after a break

    print("You rolled a", dice_roll, "try again")
    lives -= 1

else:
    print("You lost all your lives, game over")