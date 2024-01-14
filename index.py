print()
print()
print('-------------------------------------------------')
print('NEW OUTPUT')
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



print()
print()
print('-------------------------------------------------')
print()
print('task 21 - `Pass, Else in a for Loop`')
print()

#21 Pass, Else in a for Loop
numbers = [17, 7, 8, 11, 8, 5]

for i in numbers:
  if i > 5:
    print(i, 'is greater than 5')
  else:
    pass

else:
    print('Done')



print()
print()
print('-------------------------------------------------')
print()
print('task 22 - `Enumerate() in a for Loop`')
print()

#22 Enumerate() in a for Loop
numbers = [2, 3, 8, 5, 6, 7, 8, 11, 8]
counter = 0

for i, v in enumerate(numbers):
  if v % 3 == 0:
    print('Numbers[', i, '] =', v, 'is multiple of three')
    counter +=1
  else:
    continue
    
print(counter)



print()
print()
print('-------------------------------------------------')
print()
print('task 23 - `If/Else in a while Loop`')
print()

#23 If/Else in a while Loop
numbers = [1, -12, 4, -6, -10, 5, -1, -5, 4]
i = 0
counter = 1

while i < len(numbers):
  if numbers[i] < 0:
    counter *= numbers[i]
    i += 1
  else:
    i += 1

print(counter)



print()
print()
print('-------------------------------------------------')
print()
print('task 24 - `Break/Continue in a while Loop`')
print()

#24 Break/Continue in a while Loop
numbers = [2, 3, 4, -11, 5]
i = -1

while i < len(numbers) -1 :
  i += 1
  if numbers[i] < 0:
    print('Negative number was found!: ', numbers[i])
    break
  else:
    continue



print()
print()
print('-------------------------------------------------')
print()
print('task 25 - `Pass, Else in a while Loop`')
print()

#25 Pass, Else in a while Loop
counter = 0

while counter < 10:
  counter += 1
  pass

else:
  print('Done!')



print()
print()
print('-------------------------------------------------')
print()
print('task 26 - `First Nested Loop Pattern`')
print()

#26 First Nested Loop Pattern
  # Set outer loop for the number of rows
for i in range(4, 0, -1):
  # Set inner loop for the number of elements in the row
  for j in range(1, i+1):
    print('*', end=' ')
  print('')




print()
print()
print('-------------------------------------------------')
print()
print('task 27 - `Nested for Loop`')
print()

#27 Nested for Loop
matrix = [ [1, 2, 4, 29],
           [3, 4, 6, 1] ]

counter = 0
# Set outer loop to work with the number of rows
for i in range(len(matrix)):
  # Inner loop to work with the number of element in the row
  for j in range(len(matrix[i])):
    # Implement sum with the help of counter
    counter += matrix[i][j]

print(counter)




print()
print()
print('-------------------------------------------------')
print()
print('task 28 - `Nested While Loop`')
print()

#28 Nested While Loop
matrix = [ [1, 2, 4, 29],
           [3, 4, 6, 1],
          [10, -5, 0]]

# Set outer while loop to work with the number of rows
i = 0
while i < len(matrix):
  # Set inner while loop to work with the number of elements in the row
  j = 0
  while j < len (matrix[i]):
    matrix[i][j] += 1
    print(matrix[i][j], end = ' ')
    j +=1
  i += 1
  print('')



print()
print()
print('-------------------------------------------------')
print()
print('task 29 - `While Loop inside a for Loop`')
print()

#29 While Loop inside a for Loop
matrix = [['R', 'i', 'd', 'e', 'r', 's', ' ', 'o', 'n '],
   ['t', 'h', 'e', ' ', 's', 't', 'o', 'r', 'm']]

# Set for loop to work with rows (i)
for i in range(len(matrix)):
  # Set j
  j = 0
  # Set while loop to work with elements inside the row
  while j < len(matrix[i]):
    print(matrix[i][j], end = ' ')
    j += 1
  print('')




print()
print()
print('-------------------------------------------------')
print()
print('task 30 - `If/Else in a Nested Loop`')
print()

#30 If/Else in a Nested Loop
text = 'ofsddsfadfjfojnanjinjudfninvjunjee'
vowels = 'aeiou'

# Set i
i = 0
# Set while loop to work with elements of the text
while i < len(text):
  # Set for loop to work with the elements of the vowels
  for j in range(len(vowels)):
    # If an element in the text is one of the elements in vowels
    if text[i] == vowels[j]:
      print(text[i])
  i += 1



print()
print()
print('-------------------------------------------------')
print()
print('task 31 - `Break/Continue in a Nested Loop`')
print()

#31 Break/Continue in a Nested Loop
matrix = [[' L', '#', 'o', 'o', '#', 's', 'i', 'n', 'g', ' ', '#', 'm', 'y '],
  ['r', 'e', '#', 'l', 'i','#', 'g', 'i', 'o', '#', 'n', '!', 'apspsasd']]

# Set for loop to work with the number of rows 
for i in range(len(matrix)):
  # Set for loop to work with the number of elements of the row
  for j in range(len(matrix[i])):
    if matrix[i][j] == '#':
      continue
    elif matrix[i][j] == '!':
      break
    else:
      print(matrix[i][j], end=' ')




print()
print()
print('-------------------------------------------------')
print()
print('task 32 - `Challenge`')
print()

#32 Challenge
text = 'aew$^&hg32yy8wer3$#^*@#7ds983hn'
vowels = 'aeiou'

text_vowels = ''
text_consonants = ''
text_symbols = ''

i = 0
# Set outer while loop to work with text
while i < len(text):
  u = 0
  # Set condition *if an element is a letter*
  if text[i].isalpha():
    # Set inner *while* loop to work with vowels
    while u < len(vowels):
      # Set condition *if a letter from the text is in the vowels* 
      if text[i] == vowels[u]:
        # Add the letter to the text_vowels
        text_vowels += text[i]
        break
      u += 1
    else:
      # Add the letter to the text_consonants
      text_consonants += text[i]
  else:
    # Add the letter to the text_symbols
    text_symbols += text[i]
  i += 1
  
print('Vowels from the text: ', text_vowels)
print('Consonants from the text: ', text_consonants)
print('Symbols from the text: ', text_symbols)
print()
print()
print('-------------------------------------------------')
print()