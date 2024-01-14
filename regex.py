import re

print()
print()
print('-------------------------------------------------')
print('NEW OUTPUT')
print('-------------------------------------------------')
print()
print('task 1 - `Search Function`')
print()

# Search Function
text = "The cat in the hat"
x = re.search(".at", text)
print(x) # Output: <re.Match object; span=(4, 7), match='cat'>


print()
print()
print('-------------------------------------------------')
print()
print('task 2 - `Matching a phone number`')
print()


# Matching a phone number
phone_number = "223-456-7890"
phone_regex = r'^\d{3}-\d{3}-\d{4}$'
x = re.search(phone_regex, phone_number)
print(x.group()) # Output: 123-456-7890

print()
print()
print('-------------------------------------------------')
print()
print('task 3 - `SPLIT Method`')
print()


# SPLIT Method
text = "The cat is cute. The dog is also cute."
x = re.split("\.", text)
print(x) # Output: ['The cat is cute', ' The dog is also cute', '']
print()
print()
print('-------------------------------------------------')
print()
print('task 4 - `Findall Method`')
print()


# Findall Method
text = "The cat is cute. The dog is also cute."
x = re.findall("cute", text)
print(x) # Output: ['cute', 'cute']

print()
print()
print('-------------------------------------------------')
print()
print('task 5 - `Finditer Method`')
print()

# Finditer
text = "The cat is cute. The dog is faithful."

x = re.finditer("(cat|dog) is (cute|faithful)", text)
for match in x:
  print(match.group(), end=' ')  # Output: cat is cute dog is faithful

print()
print()
print('-------------------------------------------------')
print()