#Input, multiple values
numbers = input().split()

#Defining the variable as three integers
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

#Sorting the variable "numbers" and defining the variable as integers
numbers.sort(key=int)

#Printing the sorted numbers on each line
for ascending in numbers:
    print(ascending)

#Print blank linme
print()

#Unsorting the three integers again
unsorted = [a, b, c] 

#Printing the integers unsorted
for u in unsorted:
    print(u)