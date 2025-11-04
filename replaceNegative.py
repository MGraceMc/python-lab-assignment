#List with positive and negative numbers
numbers = [10, -20, 30, -40, 50]

#Loop through each element
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = abs(numbers[i]) #Replace with absolute value

print(numbers)