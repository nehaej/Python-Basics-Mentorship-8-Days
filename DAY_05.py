# LISTS - What are lists?
# a list is an ordered sequence of elements enclosed in square brackets
# EXAMPLES
list1 = ["cat","a","cdef"]   
list2 = [2,3,4,5,6]  
[2,4.5,"bob",34]

# SOME LIST FUNCTIONS 
# recall the functions we learnt yesterday for TUPLE - ALL can be used in LIST as well

L1 = [7,5,8,3,5,5]
L2 = ["apple","banana","cat","abc"]
L1.append(22) # add 34 to the end of L1
print(L1)

ind = L1.index(8) # will return index value of 8

L1.insert(2,75)# add 75 in 2nd position
print(L1)

L1.sort() # explained in TUPLE
print(L1)

L1.remove(5) # 5 will be removed from L1, FIRST OCCURENCE 
print(L1)

L1.count(5) # 3 5s are there
print(L1)

L1.reverse() 
print(L1)

L1.extend(L2)
print(L1) # add L2 to end of L1

# LIST SLICING
# values are "numbered" in a list starting from 0 : similar to TUPLE
L1[2:4]   # index 2 = 8, index 3 = 3, index 4 = 5 : LAST NUMBER EXCLUDED --> 2:4 only 2,3 positions displayed

L2 = ["apple","banana","cat","abc"]
chosen = L2[0:3]
print(chosen)

# EXAMPLES to explain list functions 

# EXAMPLE 1 - SHOPPING CART

cart = ["Apple", "Milk"]
item = input("What do you want to buy? ")
cart.append(item) # remember will be added to end of list

unwanted = "Milk"

if unwanted in cart:
    cart.remove(unwanted) 
    print(f"Removed {unwanted}. Updated cart: {cart}")
else:
    print("Item not found!")

# EXAMPLE 2 - NUMBERS

numbers = [450, 780, 120, 900, 560]
numbers.sort() # will arrange numbers in descending order
print(f"low to high: {numbers}")

numbers.reverse() # reverse list ---> descending becomes ascending 
print(f"Reversed order: {numbers}")

lowest = numbers.pop() # pop() deletes the last elemnt  # pop(2) deletes elem w/ index == 2
print(f"Removed number: {lowest}")


# TASK - CINEMA TICKETING SYSTEM
# List of movies given; might hv age restrictions and diff pricing depending on movie 

movies = ["Jurassic World","Avatar","Dies Irae","Drishyum","Marco"]
prices_inr = [250,200,150,175,125]
min_age = [13,13,18,13,18]

print(f"Movie name: {movies[0]} Ticket price: {prices_inr[0]}")
print(f"Movie name: {movies[1]} Ticket price: {prices_inr[1]}")
print(f"Movie name: {movies[2]} Ticket price: {prices_inr[2]}")
print(f"Movie name: {movies[3]} Ticket price: {prices_inr[3]}")
print(f"Movie name: {movies[4]} Ticket price: {prices_inr[4]}")
movie_name = input("Which of the following movies would you like to watch? ")

age = int(input("Enter your age: "))
money = int(input("Enter how much money you have (inr): "))

index_val = movies.index(movie_name)   # to figure out which movie customer chose

if movie_name not in movies :
    print("Please choose a movie from the given options")

if age >= min_age[index_val] and money >= prices_inr[index_val] : # eg: min_age[0] = 13 , age = 7, if 7 >= 13...
    print("Enjoy the show! ")
    remaining_amt = money - prices_inr[index_val]
    print(f"Balance:{remaining_amt}")

elif age <= min_age[index_val] :
    print("This movie is R rated. You are not old enough")

else :
    print("You do not have enough money to purchase a ticket for this movie")
