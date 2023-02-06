
#namedtuple 
from collections import namedtuple

Dog = namedtuple('Dog', ['name', 'breed', 'color'] )


#Create a new address object house where house.street is "221B Baker Street", house.city is "London", and house.country is "England".

Address = namedtuple('Address', ['street', 'city', 'country'])
direccion = namedtuple('Address', ['street', 'city', 'country'])


house = Address ("221B Baker Street","London","England")

print(house.street)

house = direccion ("Sherlock baby","London","England")

print(house.street)

# ____________________________________

# Create a set using the set() function.
nums1 = set([1, 2, 3])

# Create a set using a set literal.
nums2 = { 7, 8, 9 }

# Print the contents of the sets.
print(nums1)
print(nums2)

# ____________________________________

# Create sets
names1 = {'Corrin', 'Pedro', 'Khan', 'Dean'}
names2 = {'Emilia', 'Kara', 'Corrin', 'Tia'}
names3 = {'Karat', 'Kara', 'Karah', 'Khan'}
names4 = {'Khan', 'Dean', 'Pascale'}

# Union names1 and names2
result_set = names1.union(names2)

print(result_set)

# Intersection btwn result_set and names3
result_set = result_set.intersection(names3)
print(result_set)

# Difference btwn result_set and names4
result_set = result_set.difference(names4)


# ____________________________________

person1_cities = {'Edmonton', 'Vancouver', 'Paris', 'Bangkok', 'Bend', 'Boise', 'Memphis', 'Zurich', 'Accra', 'Cairo'}
person2_cities = {'Accra', 'Orlando', 'Tokyo', 'Paris', 'Anaheim', 'Buenos Aires', 'London', 'Lima', 'Seoul', 'Bangkok'}

# Use set methods to create sets all_cities, same_cities, and different_cities.

all_cities = person1_cities.union(person2_cities)
same_cities = person1_cities.intersection(person2_cities)
different_cities = person1_cities.symmetric_difference(person2_cities)

print(sorted(all_cities))
print(sorted(same_cities))
print(sorted(different_cities))

# ____________________________________
#Dictionary

prices = {}  # Create empty dictionary
prices['banana'] = 1.49  # Add new entry
print(prices)

prices['banana'] = 1.69  # Modify entry
print(prices)

del prices['banana']  # Remove entry
print(prices)

# ____________________________________

car_makers = {'Acura': 'Japan', 'Fiat': 'Egypt'}

# Add the key Tesla with value USA to car_makers
# Modify the car maker of Fiat to Italy

car_makers ['Tesla'] = 'USA'
car_makers ['Fiat'] = 'Italy'

print(f'Acura made in {car_makers["Acura"]}')
print(f'Fiat made in {car_makers["Fiat"]}')
print(f'Tesla made in {car_makers["Tesla"]}')