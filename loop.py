

# user_input = input()
# test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


# sum_extra = 0 # Initialize 0 before your loop


# for grade in test_grades:
#     if grade >= 100:
#         extra = 100 - grade 
#         sum_extra = sum_extra + extra


# print(f'Sum extra: {sum_extra}')


# -------------------------------------------------

num_guesses = int(input())
user_guesses = []

num_guesses = (str(num_guesses)).split()
guesses = int(num_guesses[0])

num_guess = []
num_guess = num_guess.append(num_guesses)

count = 0
while count < guesses:
    for guess in num_guess:
        user_guesses.append(guess)
        print(guess)
        count += 1



# while (user_input.lower() != 'exit'):
#     books.append(user_input)
#     user_input = input(prompt).strip()


print(count)
print(guesses)

print(f'user_guesses: {user_guesses}')