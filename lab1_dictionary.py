

contact_input = 'Joe',123-5432 'Linda',983-4123 'Frank',867-5309
name_search = 'Frank'


# Initialize dictionary 
contact_dict = {}

for pair in contact_input:
    #Joe,123-5432 (Separate value and key)
    pair_contact = contact_input.split(',') 
    #create the pairs dict{key = value} --> contact_dict{'Joe' = '123-5432'}
    contact_dict[pair_contact[0]] = pair_contact[1]
    print(contact_dict)
    
for name_search in contact_dict:     
    if name_search in contact_dict: 
        search = contact_dict.get(name_search, 'Name no found')
        print(search)



        
