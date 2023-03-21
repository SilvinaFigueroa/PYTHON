
#Check exercise

# def get_numbers():
#     user_input = input()
#     values = [5,7,2,17,11,16]
#     for token in user_input.split():
#         values.append(int(token))
#     return values

# def print_selected_numbers():
#     numbers = get_numbers()
#     for number in numbers:
#         if number >= 9:
#             print(number)

# print_selected_numbers()

# The statement print_cat = print_pig reassigns the print_pig function object with the variable print_cat. 
#The call print_cat() thus calls the referenced object, which is equivalent to print_pig().

# def print_cat():
#     print('meow')

# def print_pig():
#     print('oink')

# print_cat = print_pig
# print_cat()


# print('Initial global namespace: ')
# print(globals())

# my_var = "This is a variable"
# print('\nCreated new variable')
# print(globals())

# def  my_func():
#     pass

# print('\nCreated new function')
# print(globals())



def int_to_reverse_binary(integer_value):
    str_binary = integer_value
    binary = ""

    if (integer_value > 0):

        while (str_binary !=0 ): 

            remainder_div = str(str_binary % 2)
            str_binary   = str_binary //2

            binary += remainder_div

        return binary   
    
    else: 
    #if integer input by user is = 0  
        return "0"


def string_reverse(input_string):
    reverse_string = ""
    index = len(input_string)

    while index > 0: 
        reverse_string += input_string [index - 1]
        index -= 1

    return reverse_string

if __name__ == '__main__':
    
    integer_value = int(input())
    input_string = int_to_reverse_binary(integer_value)
    
    print(string_reverse(input_string))


