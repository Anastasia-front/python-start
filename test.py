print()
print()
print("-------------------------------------------------")
print("NEW OUTPUT")
print("-------------------------------------------------")
print()
print("task 1.1 - `Exception handling mechanism (ZeroDivisionError)`")
print()

# 1.1 Exception handling mechanism (ZeroDivisionError)
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print("Divide by zero completed!")


print()
print()
print("-------------------------------------------------")
print()
print("task 1.2 - `Exception handling mechanism (ValueError)`")
print()

# 1.2 Exception handling mechanism (ValueError)
letter = "a"
try:
    letter = int(letter)
except ValueError:
    print(f"letter {letter} is not a number")
else:
    print(letter > 0)
finally:
    print("This will be printed anyway")


print()
print()
print("-------------------------------------------------")
print()
print("task 2 - `Calculating of salary`")
print()

# 2 Calculating of salary
hours = input("Enter Hours:")
h = float(hours)
rate = input("Enter rate:")
r = float(rate)
print(h, r)
if h > 40:
    print(h * r)
else:
    org = (h - 40) * (r * 0.5)
    print(org)
    print(h * r + org)


print()
print()
print("-------------------------------------------------")
print()
print("task 3 - `Calculating of price with/without discount`")
print()


# 3 Calculating of price with/without discount
def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
        return price

    apply_discount()
    print(price)


discount_price(100, 0.1)


print()
print()
print("-------------------------------------------------")
print()
print("task 4 - `centering a string within a given length`")
print()


# 4 centering a string within a given length
def format_string(string, length):
    if len(string) < length:
        spaces = "_" * ((length - len(string)) // 2)
        print(len(spaces))
        string = spaces + string + spaces
        print(string)


format_string("abaa", 15)


print()
print()
print("-------------------------------------------------")
print()
print("task 5 - `VARIABLE NUMBER OF PARAMETERS`")
print()

# 5 VARIABLE NUMBER OF PARAMETERS


def first(size, *args):
    return size + len(args)


print(first(3, 8, 9, 0, 0, 0, 0, 9))


def second(size, **kwargs):
    return size + len(kwargs)


print(second(3, po=8, lp=9, hg=0))


print()
print()
print("-------------------------------------------------")
print()
print("task 6 - `RECURSION`")
print()


# 6 RECURSION
# We are holding a prize draw among the first 50 subscribers
# to the YouTube channel. We have 7 prizes to give away.
# The question may be, how many different lists of winners
# can we get during the draw? For this, we will use the formula
# of combinations without repetitions
# Cnk = n! / ((n - k)! · k!)
# where n is the total number of people (cases) and k is the
#  number of people who received prizes.
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))


print(number_of_groups(50, 7))


print()
print()
print("-------------------------------------------------")
print()
print("task 7.1 - `mathematical degree`")
print()

# 7.1 mathematical degree


def convert_to_superscript(number):
    # Convert the exponent to Unicode superscript characters
    superscript_trans = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    return str(number).translate(superscript_trans)


def create_superscript_string(base, exponent):
    superscript_str = convert_to_superscript(exponent)

    # Combine the base and superscript exponent
    result = f"{base}{superscript_str}"

    return result


# Example usage
degree_str = create_superscript_string("x", 2)
print(f"x²: {degree_str}")

degree_str = create_superscript_string("y", 3)
print(f"y³: {degree_str}")


print()
print()
print("-------------------------------------------------")
print()
print("task 7.2 - `representing of logarithm`")
print()


# 7.2 representing of logarithm
def convert_to_subscript(number):
    # Convert the subscript to Unicode subscript characters
    subscript_trans = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(number).translate(subscript_trans)


def create_subscript_string(base, subscript):
    subscript_str = convert_to_subscript(subscript)

    # Combine the base and subscript
    result = f"{base}{subscript_str}"

    return result


# Example usage
log_str = create_subscript_string("log", 2)
print(f"log₂: {log_str}")

log_str = create_subscript_string("log", 10)
print(f"log₁₀: {log_str}")


print()
print()
print("-------------------------------------------------")
print()
print('task 7.3 - `"C" in logarithmic notation (log n) and as a mathematical degree`')
print()


# 7.3 "C" in logarithmic notation (log n) and as a mathematical degree
def create_log_degree_string(base, subscript, superscript):
    subscript_str = convert_to_subscript(subscript)
    superscript_str = convert_to_superscript(superscript)

    # Combine the base, subscript, and superscript
    result = f"{base}{subscript_str}{superscript_str}"

    return result


# Example usage
log_degree_str = create_log_degree_string("C", 2, 3)
print(f"C₂³: {log_degree_str}")
print()
print()
print("-------------------------------------------------")
print()
