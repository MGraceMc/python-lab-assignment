#Creating two lists
list1 = ['physics', 'chemistry', 1997, 200]
list2 = [1, 2, 3, 4, 5]

#Accessing different values
print("list1[0]: ", list1[0])   #Prints first element of list1
print("list2[1:5]: ", list2[1:5]) #Prints elements from index 1 to 4

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

#Updating values
print(f"Value before update: {list2}")
list2[2] = 10  #Changes the third element (index 2)
print(f"Value after update: {list2}")

#Appending new elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati') #Adds to the end of the list 
print(motorcycles)

#Inserting new elements at specific locations
motorcycles.insert(0, 'kawasaki') #The 0 adds this to the beginning
print(motorcycles)
