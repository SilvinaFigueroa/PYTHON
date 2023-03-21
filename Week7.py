


# user_string = input()
# compare_to = "1234567890"
# count = 0


# for user_char in user_string:
#     if user_char in compare_to:
#         count += 1


# if ((count) == len(user_string)): 
#     print ("Yes")
# else:
#     print ("No")

# print(count)



# __________________




# name = input()
# separate_name = name.split()

# firstName = ""
# middleName= ""
# lastName = ""
# fullName = ""

# first_initial = firstName.split()
# middle_initial = middleName.split()

# if len(separate_name) == 3:
#     firstName = separate_name[0] 
#     middleName = separate_name [1] 
#     lastName = separate_name [2] + ", " 
 
#     fullName = "".join([lastName,firstName[0]+".",middleName[0]+"."])

# elif  len(separate_name) == 2:  
#       firstName = separate_name[0]
#       lastName = separate_name [1] + ", "

#       fullName = "".join([lastName,firstName[0]+"."])



# print(fullName)


     
# ----------------------------------------


# str_input = input()
# word_input = str_input[2:]
# char_input = str_input[0]
# count_char = 0
# output = ""

# count_char = word_input.count(char_input)

# if count_char > 1:
#      output = (f'{count_char} {char_input}\'s')

# else:
#      output = (f'{count_char} {char_input}')

# print(output)

# ----------------------------------------------

# word_input = ""

# while word_input != "quit":
#     word_int = input()
#     split_input = word_int.split()
#     word_input = split_input[0] 
#     int_input = split_input[1]
    
#     if word_input != "quit":
#         print(f'Eating {int_input} {word_input} a day keeps you happy and healthy.')
    
# ----------------------------------------------

# user_input = input()
# clean_str = user_input.strip
# reverse_input = clean_str[::-1]

# if user_input == reverse_input: 
#     print(f'palindrome: {reverse_input}')

# else: 
#     print(f'not a palindrome: {user_input}')

# ----------------------------------------------


user_input = input()
clean_string = ""


for char in user_input: 
    if char >= "a" and char <= "z" or char >= "A" and char <= "Z": 
        clean_string += char

print(clean_string)


