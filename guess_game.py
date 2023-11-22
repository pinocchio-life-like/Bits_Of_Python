from random import choice

print("This is a guess game, pick a number between [1, 10]")
num = choice([1,2,3,4,5,6,7,8,9,10])
trial = 0
while True:
    if trial > 0:
        guess = input("Pick again: ")
        if num == int(guess, base=10):
            print("You are a genius")
            break
        else:
            print("You are wrong guess again")
    else:
        guess = input("Welcome, pick from [1,10]: ")
        if num == int(guess, base=10):
            print("You are a genius")
            break
        else:
            print("You are wrong guess again")
    trial = 1
    
    