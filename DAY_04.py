# DAY 4

# RECALL ARITHMETIC OPERATORS + IF STATEMENTS

"+,-,*,/,//,%"

# CREATE A CALCULATOR (GUIDED)

num1 = int(input('Enter first number: '))
num2 = int(input("Enter second number: "))

print("The following operators are available: +,-,*,/,**")      # we made use of if/elif/else statements, equality operator and arithmetic operators 
op = input("Enter operator: ")

if op == "+" :
    print("Sum: ",num1 + num2)
elif op == "-" :
    print("Difference: ",num1 - num2)
elif op == "*" :
    print("Product: ",num1*num2)
elif op == "/" :
    print("Division: ",num1/num2)
elif op == "**" :
    print("First number raised to second :",num1**num2)
else :
    print("Please choose an operator from the options given above")


# TASK: PROFITS- Find amount of money earned by a rubber farmer based on amt harvested
harvest = int(input("How many kilograms of rubber was harvested?"))
MRP_kg = int(input("Enter current MRP per kg of rubber:"))

total_money_earned = harvest*MRP_kg

production_costs = int(input("How much money was spent on farming this season?"))

profit = total_money_earned - production_costs

print(f"The farmer earned {profit} in total profits this farming season")


# TUPLES : WHAT ARE THEY? 
# a Tuple is an immutable ordered sequence of elements that can hold different data types, defined using parentheses ()
# immutable --> cant be changed aft you create it 
# values separated by commas

# EG: (1,2,3,4,5)
# ("cat","dog",2.0,32)  ---> different "types" : string/float/int

# SOME TUPLE FUNCTIONS 

tup1 = (1,2,3,4,5)
print(len(tup1)) # number of elements in tup1
print(max(tup1)) # max value = 5
print(min(tup1)) # min value = 1
print(sum(tup1)) # sum = 15
print(sorted(tup1))  # returns a LIST (DAY 5) []
 


string = "Don't mess with Aleesha"
print(tuple(string))        # tuple() ---> change into tuple
