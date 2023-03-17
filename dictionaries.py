


# my_dict = {'Ahmad': "value to remove", 'Jane': 42}
# val = my_dict.pop('Ahmad')

# print(my_dict)
# print(val)

#________________________


# user_input = 'China:1365830000,India:1247220000,United States:318463000,Indonesia:252164800'
# entries = user_input.split(',')
# country_pop = {}  

# for pair in entries:
#     split_pair = pair.split(':')
#     country_pop[split_pair[0]] = split_pair[1]
#     # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }


# for country, pop in country_pop.items():

#     print(f'{country} has {pop} people.')


#________________________

grades = {
    'John Ponting': 
    {
        'Homeworks': [79, 80, 74],
        'Midterm': 85,
        'Final': 92
    },
    'Jacques Kallis': 
    {
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': 
    {
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

user_input = 'Ricky Bobby'

while user_input != 'exit':
    if user_input in grades:
        # Get values from nested dict
        homeworks = grades[user_input]['Homeworks']
        midterm = grades[user_input]['Midterm']
        final = grades[user_input]['Final']

        # print info 
        for hw, score in enumerate(homeworks):
            
            print(f'Homework {hw}: {score}')

        
        print(f'Midterm: {midterm}')
        
        print(f'Final: {final}')

        # Compute student total score
        total_points = sum([i for i in homeworks]) + midterm + final
        
        print(f'Final percentage: {100*(total_points / 500.0):.1f}%')

    user_input = input('Enter student name: ')
