import random
def guess_the_number():
    print("welcome to guess the number")
    print("think of a number between 1 and 20")
    
    secret_number = random.randint(1,20)
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        try:
            guess = int(input("enter your guess:"))
            attempts +=1
            
            if guess< secret_number:
                print("too low! try again.")
            elif guess> secret_number:
                print("too high! try again")
            else:
                print("congratulations you guessed the number in (attempts) attempts")
                
                guessed_correctly = True
        except ValueError:
            print("invalid input please enter a number")
            
            
guess_the_number()