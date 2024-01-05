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