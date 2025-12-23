# DAY 3

# TOPIC 1 - OR/AND/NOT 

# AND - how does it work?
bus_pass = True
school_hours = True
                                            # remember == represents CHECKING , checking if bus_pass is available
if bus_pass == True and school_hours == True :  # just like in english, both conditions must be met for AND
    print("It's only 2 rupees")
else :
    print("Pay the full fare")



# OR - what does it mean?
physical_money = False
google_pay = True

if physical_money == True or google_pay == True : # like english- only one condition HAS to be satisfied both not necessary
    print("You can pay and not go to jail")
else :
    print("Im calling the police")



# NOT 
lays = True  # not True = False, not False = True
if not lays :     # since lays is True, not lays is False. But we already know that lays is available since lays=True
    print("Get out of the shop") # IF condition NOT met so move to else  
else :
    print("Buy some lays for neha") 


# EXAMPLE 1
# Determine which bus student should take based on BUS TIMINGS and AMT OF MONEY

money = int(input("How much money do you have?"))
bus_wait_time = input("How long are you willing to wait?")

if money >= 100 and bus_wait_time >= 10: # if money is more than or equal to 100 and you are willing to wait 10 mins
    print("Take an auto. You'll get home early")

elif money >= 40 and bus_wait_time >= 30: # if money more than or equal to 40 and willing to wait 30 mins
    print("Take a KSRTC bus. Cheaper but you'll have to wait longer.")

elif money >= 15 and bus_wait_time >= 60: # same idea applied here as well
    print("Take a private bus. Long wait times but cheap ticket pricing.")

else:
    print("Get someone to pick you up")

# EXAMPLE 2
# internet speed and streaming 

internet_speed = 15  # Mbps - mega bytes per second
subscription_tier = "Standard"

if internet_speed >= 25 and subscription_tier == "Premium":
    print("Streaming in 4K Ultra HD.")
elif internet_speed >= 5 and subscription_tier == "Standard":
    print("Standard .")
else:
    print("Low quality. Might face lag")


# EXAMPLE 3
# simple video logic ie, yt

# () means it will be considered first, program will identify if person has subscription or watching free content.
# AFTERWARDS, check if yt kids or normal yt

subscription = False
free_content = True
yt_kids = True

if (subscription or free_content) and not yt_kids :                         
    print("Downloadable video available (Not age restricted)")
elif (subscription or free_content) and yt_kids :
    print("Age restricted content is downloadable") 
else :
    print("Purchase a subscription or watch free content")



# TASK
# GRADE FINDER

score = int(input("Enter student score (0-100): "))
is_topper = False  

if score >= 90 or is_topper:
    print("Result: A")

elif score >= 80:
    print("Result: B")

elif score >= 70:
    print("Result: C")

elif not score >= 40:
    print("Result: D")

else:
    print("Result: F")
