# adding comments in your file

x = 100
y = 0.05
z = x * y
w = x + z
print(w)     # without comments is it easy to understand??

# HEADER COMMENTS: explain aim of the program

# cal total bill w/ 0.05% tip added

total_bill = 100 
tip_percentage = 0.05  #  IN-LINE COMMENTS:  explain variables that may seem confusing to others
                        # percentage for tip is 0.05 and money owed is 100

# LOGIC COMMENTS: explain how the step works, like how i added comments in prev days' classes
# Calculate the tip amount and add it to the original bill
tip_amount = total_bill * tip_percentage
final_total = total_bill + tip_amount

print(f"Your total with tip is: ${final_total}")

# why add comments? - easier for ur teammates
# easier for u to debug ltr 


# EXAMPLE 2 --> rmb the grocery prog from 2 days ago??

# HEADER : # program that accepts items from user and creates a grocery list

grocery_list = []   #  INLINE :  initialize a list 

print("--- GROCERY LIST---")
print("Type 'done' when you are finished adding items.")

while True:
    item = input("Enter an item or done if finished: ").lower().strip() # INLINE : groceries entered by user 
    
    if item == "done": # LOGIC : if user enters done for item input then break out of the while loop and end program 
        break  
    
    grocery_list.append(item)
    print(f"Added {item}. Total items: {len(grocery_list)}")

print("\nFinal Grocery List:")
for i in grocery_list:
    print(f"- {i}")
