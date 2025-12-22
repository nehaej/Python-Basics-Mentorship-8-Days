# DAY 2! 

# TOPIC 1 - COMPARISON/ARITHMETIC OPERATORS
# arithmetic 
SUBTRACTION = 3-2
ADDITION = 3+2
MULTIPLICATION = 3*2 = 6
POWER = 3**2  = 9 
DIVISION = 3/2=1.5

FLOOR_DIVISION = 3//2  # quotient only  3//2 =1 
MODULO_DIVISION = 3%2  # reminder only  3//2 =0.5

# comparison 
a = 2 
b = 2
a == b # checking if b are equal
                        # = --> assignment operator    == ---> equality operator 
c = 4
d = 3
c != d # checking if not equal

c > d 
d < c

c >= d 
d <= c

# assignment 
a = "cat"              # you can combine with other arithmetic operators like += ,-= etc.
b += 3

    
# MINI SUB TOPIC       a = 3  name = "ali"
# variable names :      
# in python variable names MUST not contain any other special character other than _ 
# spaces strictly not allowed
# cant use any of python's keywords 
# python treats small letters and capital letters differently 


# TOPIC 2 - IF/ELSE STATEMENTS 
# If and else work the same way in code exactly like they do in english 

# SIMPLE EXAMPLES

# EXAMPLE-1

name = input("Enter name:")
enemy = input("Enter your enemy's name")

if name == "Aleesha" :
    print(f"{enemy} is cooked")
else :
    print(f"{name} got defeated by {enemy}")


# EXAMPLE-2

temperature = int(input("What is the temperature in Celsius? "))

if temperature > 30:
    print("It is a hot day!")
    print("Remember to drink water.")

# this line always runs because it's not indented INDENTATION IS VERY IMPORTANT !!
print("Have a nice day!")    


# TOPIC 3 - ELIF --> MULTIPLE CONDITIONS

# EXAMPLE - 1

score = int(input("Enter your test score (0-100): ")) # 76

if score >= 90:
    print("Grade: A - Excellent work!")    # alen -65
elif score >= 80:
    print("Grade: B - Well done!")
elif score >= 70:                                 # 45
    print("Grade: C - Good effort.")  # stop 
elif score >= 60:
    print("Grade: D - You passed.")
else:
    print("Grade: F - Better luck next time!") 

# ERROR  - For Discussion

temp = 35

if temp > 0:
    print("It's above freezing.")
elif temp > 30:
    print("It's a very hot day!") #  will never print ; recall elif/if relationship
else :
    print("antarctic :(")


# VOTER ELIGIBILITY
age = int(input("Enter your age"))

if age >= 18:
    print("ELIGIBLE")
if age < 18 :
    print("NOT ELIGIBLE")

# EVEN - ODD 
num = int(input("Enter a number:"))

if num%2 == 0 :
    print(f"{num} is even")
else :
    print(f"{num} is odd")


# TRY IT YOURSELF --> TRY TO UNDERSTAND THIS CODE 
# DISCOUNT CALCULATOR 
amount = float(input("Enter the total purchase amount: ₹"))

if amount >= 1000:
    discount = 20  # 20% discount for ₹1000 or more
elif amount >= 500:
    discount = 10  # 10%  for ₹500 to ₹999
elif amount >= 100:
    discount = 5   # 5% for ₹100 to ₹499
else:
    discount = 0   # No for less than ₹100

# final price
savings = (discount / 100) * amount
final_price = amount - savings

print(f"Discount applied: {discount}%")
print(f"Amount saved: ₹{savings:.2f}")       # .2f basically tells how to format the value ie, 2 decimal places 
print(f"Final total to pay: ₹{final_price:.2f}")
