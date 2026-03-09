import random



def guessing_game():
    r = random.random()
    r = (int(r*101))
    print("Guess a number between 1-100. \n Enter 'X' to exit the game")
    run = True
    while run:
       try:
            inp = input("Guess a number between 1-100: ")
            if(inp == "X" or inp =="x"):
                run = False
                break
            inp = int(inp)
       except ValueError:
            print("Please enter a number")
            continue
       if inp < r:
        print("Your guess is too low")
       elif inp > r:
        print("Your guess is too high")
       else:
        print("Your guess is correct")
        run = False

name = 'Ermal'
first = 'Mal'
last = 'Mill'

print(f' {last:#>0}')


