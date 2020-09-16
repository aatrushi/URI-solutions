import math

#Inputs. We use the function split() because each line of data contains multiple values
x1,y1 = input().split()
x2,y2 = input().split()

#Input value type = float
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

#Distance formula given in URI 1015
Distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

#The output is formatted to 4 decimals
print('{:.4f}'.format(Distance))