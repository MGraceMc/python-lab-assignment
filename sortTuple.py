#Function to return the first element for sorting
def takeFirst(elem):
    return elem[0]

#List of tuples
list_of_tuples = [(2,5), (1, 2), (4, 4), (2, 3), (2, 1)]

#Sort the list using the first value in each tuple
list_of_tuples.sort(key=takeFirst)
print('Sorted list:', list_of_tuples)