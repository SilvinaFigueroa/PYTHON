

input_list = input()
range_input = input()#.split()

output = []

for num in input_list:
    if num > input_list[0] and num <= input_list[1]:
        output.append(num)
        
print(output)

# 25 51 0 200 33
# 0 50