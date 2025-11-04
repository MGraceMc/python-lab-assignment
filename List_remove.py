#Creating a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Using the del statement
del motorcycles[1] #Removes 'yamaha'
print(motorcycles)

#Using pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() #Removes the last element
print(motorcycles)
print(popped_motorcycle)

#Using remove()
motorcycles = ['honda', 'yamaha', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)