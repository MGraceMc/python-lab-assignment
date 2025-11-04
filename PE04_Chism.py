guests = ["Madison", "Amy", "Hannah"]
print("Original guest list:", guests)

#Replacing a guest
guests[1] = "David"
print("Updated guest list:", guests)

#Adding guests
guests.insert(0, "Courtney")
guests.insert(2, "Bernie")
guests.append("Lily")
print("New guest list:", guests)

#Removing until only two remain
while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed}, you can't come to dinner.")

print("Final guest list:", guests)

#Task 2: Animal List and Slices
animals = ["cat", "dog", "fish", "horse", "pig", "bird", "ferret"]
for animal in animals:
    print(animal)

print("\nThe first three items are:", animals[:3])
print("Three items from the middle are:", animals[2:5])
print("The last three items are:", animals[-3:])

#Task 3: Finding duplicates
nums= [10, 20, 30, 40, 40, 50, -20, 60, -20, -20, 20]
output_list = []
for n in nums:
    if nums.count(n) > 1 and n not in output_list:
        output_list.append(n)
print("Duplicate elements:", output_list)

#Buffet Menu Tuple

foods = ("Tacos", "Pasta", "Hamburgers", "Cake")
print("\nUpdated menu:")
for food in foods:
    print(food)

#I do not understand why this code is developing an invalid syntax?

#Task 5: Sort List of Tuples
data = [('452', 10), ('256', 5), ('123', 4), ('135', 15)]
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted tuples:", sorted_data)

# Please help me understand where I am messing up my cade for the last two tasks. I keep receiving the SyntaxError: invalid syntax
