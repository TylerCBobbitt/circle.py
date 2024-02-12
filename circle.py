import math

radius = int(input('Enter the radius of the circle: '))

circumference = (2*math.pi*radius)
area = (math.pi * radius ** 2)
print('The circumference of your circle is ' + str(round(circumference,2)) + ' and the area of the circle is  ' + str(round(area,2)) + '.')