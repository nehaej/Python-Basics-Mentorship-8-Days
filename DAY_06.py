# DAY 6 

# WHILE LOOPS
# What is while loop
# how is it different from IF STATEMENT ?

# EXAMPLE 

print("Type 'exit' to stop the program.")

while True:
    user_input = input("Say something: ")
    
    if user_input == "exit":
        print("Goodbye!")
        break  # This immediately stops the loop
    
    print(f"You said: {user_input}")

# TASK

secret_word = "python"
guess = ""

# The loop continues as long as the guess is NOT equal to the secret_word
while guess != secret_word:
    guess = input("Enter the secret word to pass: ").lower()
    
    if guess == secret_word:
        print("Access Granted!")
    else:
        print("Wrong! Try again.")



# EXAMPLE

boss_health = 100
print("ALEESHAAA appears!")

while boss_health > 0:
    damage = int(input("How much power is in your attack? (1-40): "))
    

    boss_health -= damage  # rmb boss health = bosshealth - damage
    
    if boss_health > 0:
        print(f"Aleesha has been hit! Current health: {boss_health}")
    else:
        print("Aleesha has been defeated. VICTORY 🏆")


# TASK

grocery_list = []   # need to make a list first always 

print("--- GROCERY LIST---")
print("Type 'done' when you are finished adding items.")

while True:
    item = input("Enter an item or done if finished: ").lower().strip()
    
    if item == "done":
        break  
    
    grocery_list.append(item)
    print(f"Added {item}. Total items: {len(grocery_list)}")

print("\nFinal Grocery List:")
for i in grocery_list:
    print(f"- {i}")

