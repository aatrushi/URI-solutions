#Input (integer value)
n = int(input())

#Assignments
Years = n // 365
Months = (n % 365) // 30
Days = (n % 365) % 30

#Output
print(str(Years) + ' ano(s)')
print(str(Months) + ' mes(es)')
print(str(Days) + ' dia(s)')