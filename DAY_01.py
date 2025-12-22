# Welcome to the first day !!


# TOPIC 1 INPUT() AND PRINT()
# we use input function to get ANSWER/RESPONSE from the user

name = input("Enter your name please: ")    # REMEMBER: input accepts a string by default ! use conversions for other types

print(f"Hi",name)  # f stands for FORMATTED --> FORMATTED STRING 


fav_colour = input("What is your favourite colour?")

print(f"{fav_colour} is a great colour!")



# TOPIC 2 VARIABLES
# variables are like labelled boxes which can store items

x = 20
y = 10
z = x + y

user_response = input("What is your gender?")# input function will ask user for a response. 
                                             # this response can be stored in variable 
                                             # here variable is user_response



# CONVERSIONS

age = input("Enter your age")

# error
new_age = age + 2   # type error --->  we cannot add a string and a integer

# correct 
new_age = int(age)+2

num = 7
print(float(7))    # 7 become 7.0 ---> float is for decimal numbers
# REMEMBER : str(3) ----> "3"   str is for string/sentence



# TOPIC 3 - STATES
#computers contain 2 states - T and F
True 
False 
is_ready = True 


# EXAMPLE PROGRAM 1 - LIGHTS

lights_on = True

print("Did you leave the lights on?",lights_on)

new_status = input("Do you wish to leave the lights on? True/False")

lights_on = new_status
print(lights_on) # note the output


# EXAMPLE PROGRAM 2 - EXAM REGISTRATION

registered_candidate = True

name = input("Enter student name")
age = int(input("Enter your age"))
language = input("Which language are writing in? ENG/MAL/HIN")

print("Is student a reigstered candidate?",registered_candidate)

print("----------HALL TICKET----------")
print(f"STUDENT NAME : {name}")
print(f"AGE : {age}")
print(f"MEDIUM OF EXAM : {language}")


# EXAMPLE PROGRAM 3 - 

# TRY IT YOURSELF --> TRY TO UNDERSTAND THIS CODE 

#collecting info from passenger
print("--- KSRTC DIGITAL TICKET ---")
passenger_name = input("Enter Passenger Name: ")
start_point = input("Starting from: ")
destination = input("Going to: ")
ticket_count_text = input("How many tickets do you need? ")

# We convert the string to an integer .....EXAMPLE --> "3" becomes 3
number_of_tickets = int(ticket_count_text)


# We set the price and the status of the bus using variables
price_per_ticket = 120
is_bus_on_time = True  # This is our Boolean State (recall computer only has 2 states True/False)

# calculation 
total_cost = number_of_tickets * price_per_ticket

# printing in order to display output 
print("\n--- BOOKING CONFIRMED ---")
print("Passenger:  ", passenger_name)
print("Route:      ", start_point, "to", destination)
print("Total Cost: ", total_cost, "Rupees")
print("-------------------------------")
print("Is the bus on time?", is_bus_on_time)
print("Have a safe journey!")
