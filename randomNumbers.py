import random 

def number_guess(num):
    # Get a random number between 1-100
        random_number = (random.randint(1, 100))
        
        if num > random_number:
            print(f'{num} is too high. Random number was {random_number}.')
        elif num == random_number:
            print(f'{num} is correct!')
        else: 
            print(f'{num} is too low. Random number was {random_number}.')
    
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    # Convert the string tokens into integers
    user_input = input()
    tokens = user_input.split()
    for i in tokens:
        num = int(i)
        number_guess(num)

