
print('-------------------------------------------------')
print()
print('task 1 - `statement of type`')
print()
print()

#1 - statement of type
length = "2.75"
width = "1.75"
area =float(length)*float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"

print(show)

print()
print()
print('-------------------------------------------------')
print()
print('task 2 - `input`')
print()

#2 - input
name = str(input("Your name? "))
email =str(input("Your email? "))
age =int(input("Your age? "))
height =float(input("Your height? "))
is_active =bool(input("Your status? "))
result = f'''\
   Your name is - {name} \
   Your email is - {email} \
   Your age is - {age} \
   Your height is - {height} \
   Your status is - {is_active} 
   '''

# print(result)

print()
print()
print('-------------------------------------------------')
print()
print('task 3 - `lists`')
print()

#3 - lists
my_list = [2024, 3.12]
some_data = ['Python']
my_list.extend(some_data)
my_list.insert(1,"Python")
my_list.reverse()

print(my_list)

print()
print()
print('-------------------------------------------------')
print()
print('task 4 - `dictionary`')
print()

#4 - dictionary
data ={}
data['year']=2024
data['lang']="Python"
data['version']=3.12

print(data)

print()
print()
print('-------------------------------------------------')
print()
print('task 5 - `dictionary and lists`')
print()

#5 - dictionary and lists
cat = {}
info = {"status": "vaccinated", "breed": True}
cat['nick']="Simon"
cat['age']=4
cat['characteristics']=['white','soft']
age = cat.get('age')
cat.update(info)

print(cat)


print()
print()
print('-------------------------------------------------')
print()
print('task 6 - `nested lists and loop for`')
print()

#6 nested lists and loop for
countries = [["USA", 9629091, 331002651], ["Canada", 9984670, 37742154],
            ["Germany", 357114, 83783942], ["Brazil", 8515767, 212559417],
            ["India", 3166391, 1380004385]]

# Iterating over external list
for i in range(len(countries)):
    if type(countries[i]) is list:
        # Computing population density for a country
        pop_dens = round(countries[i][2]/countries[i][1], 2)
        print(countries[i][0], pop_dens, 'people per km²')



print()
print()
print('-------------------------------------------------')
print()
print('task 7 - `function and if/elif/else`')
print()

#7 function and if/elif/else
def is_positive(n):
  if n>0:
    return('positive')
  elif n < 0:
    return('negative')
  else:
    return('zero')

print('Number -5 is', is_positive(-5))
print('Number 0 is', is_positive(0))
print('Number 5 is', is_positive(5))



print()
print()
print('-------------------------------------------------')
print()
print('task 8 - `using of function parameters`')
print()


#8 using of function parameters
people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175), 'John': (41, 185), 'Michelle': (35, 165)}

def people_information(d, name):
  print("Name:", name)
  print("Age:", d[name][0], "y.o.")
  print("Height:", d[name][1], "cm")

people_information(people_d, "Alex")
people_information(people_d, "Michelle")



print()
print()
print('-------------------------------------------------')
print()
print('task 9 - `lambda`')
print()

#9 lambda
sq = lambda x, y: (x + y)**2
print('Sum of 2 and 3 squared is', sq(2, 3))



print()
print()
print('-------------------------------------------------')
print()
print('task 10 - `modifying functions`')
print()

#10 modifying functions
countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
                  'Germany': (357114, 83783942), 'Brazil': (8515767, 212559417), 
                  'India': (3166391, 1380004385)}

def country_information(d, name):
  if name not in d.keys():
    print("There is no information about", name)
  else:
   print('Country:', name)
   print('Area:', d[name][0], 'sq km')
   print('Population:', round(d[name][1]/1000000, 2), 'MM')

country_information(countries_dict, 'USA')
country_information(countries_dict, 'Ukraine')



print()
print()
print('-------------------------------------------------')
print()
print('task 11 - `find the word index and get the word`')
print()

#11 find the word index and get the word
string = "It can be painful to learn from mistakes"

painful = string[string.index('painful'):string.index('painful')+7]
mistakes = string[string.index('mistakes'):string.index('mistakes')+ 8]
learn = string[string.index('learn'):string.index('learn') + 5]

print(painful)
print(mistakes)
print(learn)



print()
print()
print('-------------------------------------------------')
print()
print('task 12 - `datetime`')
print()

#12 datetime
from datetime import datetime

# 2020-02-25
date_1 = datetime(2020, 2, 25).date()
# 2020-09-17
date_2 = datetime(2020, 9, 17).date()

delta = None
if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print("Difference is", delta.days, "days")



print()
print()
print('-------------------------------------------------')
print()
print('task 13 - `list comprehensions`')
print()

#13 list comprehensions
sentence = "List comprehension in Python is fun and powerful!"
vowels = 'aeiou'

# Using list comprehension with a conditional to extract and capitalize vowels
capitalized_vowels = [char.upper() for char in sentence if char.lower() in vowels]

# Output the list of capitalized vowels
print(capitalized_vowels)



print()
print()
print('-------------------------------------------------')
print()
print('task 14 - `dictionary comprehensions`')
print()

#14 dictionary comprehensions
city_population = {
    'New York': 8419600,
    'Los Angeles': 3980400,
    'Chicago': 2716000,
    'Houston': 2328000,
    'Phoenix': 1690000,
    'SmallTown': 15000
}
min_population = 5000000
filtered_cities = {
    city: population for city, population in 
  city_population.items() if min_population < population
}

print(filtered_cities)



print()
print()
print('-------------------------------------------------')
print()
print('task 15 - `delete an item from tuple`')
print()

#15 delete an item from tuple
fruits = ('apple', 'apricot', 'banana', 'grape', 'mango', 'peach', 'pineapple')

list_fruits = list(fruits) 
list_fruits.remove('banana')
list_fruits.remove('grape')
list_fruits.remove('peach')

fruits = tuple(list_fruits)

print(fruits)



print()
print()
print('-------------------------------------------------')
print()
print('task 16 - `methods of set`')
print()

#16 methods of set
set = {1, 5, 10, 15}
set.add(150)
set.update([20,25,100])
set.remove(10)
# will be KeyError
# set.remove(999)
set.discard(15)
#without throwing an error
set.discard(999)

print(1 in set)
print(set)
set.clear()
print(set)



print()
print()
print('-------------------------------------------------')
print()
print('task 17 - `logical operators`')
print()

#17 logical operators
def leap_year(year):
    if year % 4  == 0 and (year % 100 != 0 or year % 400 == 0):
        return 'Leap year'
    else:
        return 'Not a leap year'

print(leap_year(2024))
print(leap_year(2014))



print()
print()
print('-------------------------------------------------')
print()
print('task 18 - `Rock, Paper and Scissors`')
print()

#18 Rock, Paper and Scissors
player_1 = 'scissors'
player_2 = 'paper'

def game(player_1, player_2):
	if player_1 == player_2:
		return("It's a draw!")
	if (player_1 == 'rock' and player_2 == 'scissors') or (player_1 == 'scissors' and player_2 == 'paper') or (player_1 == 'paper' and player_2 == 'rock'):
		return("Player 1 wins!")
	else:
		return("Player 2 wins!")

print(game(player_1, player_2))



print()
print()
print('-------------------------------------------------')
print()
print('task 19 - `Car Brands`')
print()

#19 Car Brands
cars = ['mazda', 'lexus', 'bmw', 'tesla', 'kia']
new_list = []

for car in cars:
    if car == 'bmw':
        new_list.append(car.upper())
    elif car == 'kia':
        new_list.append(car.upper())
    else:
        new_list.append(car.title())
print(new_list)



print()
print()
print('-------------------------------------------------')
print()
print('task 20 - `Conditional Expression`')
print()

#20 Conditional Expression
amount = 95_000
bmw_x5 = 80_000
tesla_x = 120_000

car_to_buy = 'BMW x5' if amount < tesla_x else 'Tesla X'

print(car_to_buy)