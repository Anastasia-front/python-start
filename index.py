#1 - statement of type
length = "2.75"
width = "1.75"
area =float(length)*float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"

print(show)

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

print(result)

#3 - lists
my_list = [2024, 3.12]
some_data = ['Python']
my_list.extend(some_data)
my_list.insert(1,"Python")
my_list.reverse()

print(my_list)


#4 - dictionary
data ={}
data['year']=2024
data['lang']="Python"
data['version']=3.12

print(data)

#5 - dictionary and lists
cat = {}
info = {"status": "vaccinated", "breed": True}
cat['nick']="Simon"
cat['age']=4
cat['characteristics']=['white','soft']
age = cat.get('age')
cat.update(info)

print(cat)

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

#7 function and if/elif/else
        
def is_positive(n):
  if n>0:
    return('positive')
  elif n < 0:
    return('negative')
  else:
    return('zero')

# Test your function on -5, 0 and 5
print('Number -5 is', is_positive(-5))
print('Number 0 is', is_positive(0))
print('Number 5 is', is_positive(5))

#8 using of function parameters
# People dictionary
people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175), 'John': (41, 185), 'Michelle': (35, 165)}

# Define the function
def people_information(d, name):
  print("Name:", name)
  print("Age:", d[name][0], "y.o.")
  print("Height:", d[name][1], "cm")

# Testing the function
people_information(people_d, "Alex")
people_information(people_d, "Michelle")

#9 lambda
# Define lambda function
sq = lambda x, y: (x + y)**2
# Test it
print('Sum of 2 and 3 squared is', sq(2, 3))

#10 modifying functions
# Data
countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
                  'Germany': (357114, 83783942), 'Brazil': (8515767, 212559417), 
                  'India': (3166391, 1380004385)}

# Defining a function
def country_information(d, name):
  if name not in d.keys():
    print("There is no information about", name)
  else:
   print('Country:', name)
   print('Area:', d[name][0], 'sq km')
   print('Population:', round(d[name][1]/1000000, 2), 'MM')

# Testing the function
country_information(countries_dict, 'USA')
country_information(countries_dict, 'Ukraine')