# user_input = input('Enter numbers: ')

# tokens = user_input.split()

# # Convert strings to integers
# nums = []
# for token in tokens:
#     nums.append(int(token))

# # Print each position and number
# print()
# for pos, val in enumerate(nums):  
    
#     print(f'{pos}: {val}')

# # Change negative values to 0
# for pos in range(len(nums)):
#     if nums[pos] < 0:
#         nums[pos] = 0

# # Print new numbers
# print('New numbers: ')
# for num in nums:
#     print(num, end=' ')

# input = (input())

# #convert string to float 
# input_list = [float(i) for i in input.split()]

# #validate negative numbers 

    

# input = input()

# #use list comprehension to convert string to int 
# input_numbers = [int(i) for i in input.split()]

# negative_numbers = []

# for i in input_numbers:
#     if i < 0:
#         negative_numbers.append(i)
    
    
# sorted(negative_numbers)

# print(negative_numbers)

# # 10 -7 4 -39 -6 12 -2

input_list = input().split()
range_input = input().split()

output = []

for num in input_list:
    if num > input_list[0] and num <= input_list[1]:
        output.append(num)
        
print(output)


# 25 51 0 200 33
# 0 50