# the following are some of the final projects submitted by the students 
# slcted 1
print("📚 Study Tracker Program")
print("Enter your study hours for each day")
print("Type 0 when you are done")

total_hours = 0
days = 0

while True:
    hours = float(input("Enter hours studied today: "))

    if hours == 0:
        break

    if hours < 0:
        print("Hours cannot be negative. Try again.")
        continue

    total_hours = total_hours + hours
    days = days + 1

if days > 0:
    average = total_hours / days
    print("\n✅ Study Summary")
    print("Days studied:", days)
    print("Total hours:", total_hours)
    print("Average per day:", average)
else:
    print("❌ No study data entered")


# slcted 2
# Calculate budget of user

print("--- Welcome to Budget Bot 1.0 ---")

starting_budget = float(input("Enter your total budget for the month: $"))
remaining_balance = starting_budget
total_spent = 0.0


# We use a while loop so the user can enter as many items as they want
spend = True

while spend:
    print(f"Remaining Balance: ${remaining_balance}")
    item = input("Enter expense name (or type 'done' to finish): ").lower()

    if item == 'done':
        spend = False # Make it false so loop wont run again
    else:
        cost = float(input(f"How much did '{item}' cost? $"))
        
        # Check if the user has enough money using comparison operators
        if cost > remaining_balance:
            print("⚠️ WARNING: This exceeds your remaining budget!")
            confirm = input("Add it anyway? (yes/no): ").lower()
            if confirm != 'yes':
                continue # start from beginning again and ask for a new item
        
        remaining_balance -= cost
        total_spent += cost
        print(f"✅ Added {item}. Total spent so far: ${total_spent}")

# SUMMARY
print("--- MONTHLY SUMMARY ---")
print(f"Total Spent: ${total_spent}")
print(f"Remaining: ${remaining_balance}")


# Logic: Calculate what percentage of budget is left
percent_left = (remaining_balance / starting_budget) * 100

if percent_left >= 50:
    print("Status: Excellent! You are a super saver. 🌟")
elif percent_left > 0 and percent_left < 50:
    print("Status: Good. But be careful with your spending. ⚖️")
else:
    print("Status: BROKE 🚨") 

# slcted 3
total_earnings = 0
earn = "yes" 

print("Welcome to the Kerala Farmer's Calculator!")

while earn == "yes":
    # 1. Get user input
    crop = input("What are you selling? (Rubber, Coconut, Pepper): ").lower()
    weight = float(input(f"How many kg of {crop} do you have? "))

    # MRP/kg
    if crop == "rubber":
        price = 180
    elif crop == "coconut":
        price = 30
    elif crop == "pepper":
        price = 600
    else:
        price = 0
        print("Sorry, we don't have the price for that crop yet.")

    sale = weight * price
    total_earnings = total_earnings + sale
    
    print(f"You made ₹{sale} from this sale.")

    # Ask to continue
    earn = input("Do you have more crops to add? (yes/no): ").lower()

# Displayed 
print(f"TOTAL REVENUE: ₹{total_earnings}")
print("Thank you for using the Agri-Counter!")     

# slcted 4
checking = "yes"

while checking == "yes": # Loop will run as long as checking == "yes"
 
    day = input("What day is it? ").lower().strip()
    is_public_holiday = input("Is it a Public Holiday? (yes/no): ").lower()
    is_rainy_day = input("Did the Collector declare a rain holiday? (yes/no): ").lower()

   
    # True ==> school is CLOSED
    if day == "saturday" or day == "sunday":
        print("RESULT: No School.")
        
    elif is_public_holiday == "yes":
        print("RESULT: No School.")
        
    elif is_rainy_day == "yes":
        print("RESULT: No School. Collector has declared holiday 🌧️")
        
    else:
        print("RESULT: School is OPEN today ;(")

    # 3. Ask to check another day
    checking = input("Do you want to check again? (yes/no): ").lower()

print("Have a great day!")
