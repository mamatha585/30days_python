import math


age = int(input("Enter age: "))
height = float(input("Enter height: "))
print(1 + 1j)

# Area of triangle

base = int(input("Enter base: "))
height = int(input("Enter height: "))
print("Area of triangle:", 0.5*base*height)

# Perimeter of triangle
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
print("Perimeter of triangle: ",a + b + c)

# Area of rectangle and perimeter of rectangle
l = int(input("Enter length: "))
w = int(input("Enter width: "))
print("Area of rectangle: ",l*w)
print("Perimeter of rectangle: ",2*(l+w))

# Area of circle and circumference of circle
rad = int(input("Enter radius of circle: "))
print("Area of circle: ",3.14*rad**2)
print("Circumference of circle: ",2*3.14*rad)

# slope
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
slope = (y2-y1)/(x2-x1)
print("Slope of Line: ",slope)


# slope and euclidean distance between two points
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
slope1 = (y2-y1)/(x2-x1)
print("Slope of Line: ",slope1)
print("Euclidean distance between points: ",(x1 - y1)**2 + (x2 - y2)**2 )


# compare slopes
print( slope > slope1)
print( slope < slope1)
print( slope == slope1)

# calculate
x = int(input("Enter x: "))
y = (x**2 + 6*x + 9)
if y == 0:
    print(x)
else:
    print(y)
# lengths comparison

python = 'python'
dragon = 'dragon'

print("length of python is: ",len(python))
print("Length of dragon is: ",len(dragon))
print(len(python) < len(dragon) )
print(len(python) > len(dragon) )
print(len(python) == len(dragon) )


# and 
if python.endswith('on') and dragon.endswith('on'):
    print("True")
else:
    print("False")

# in

sen = 'I hope this course not full of jargon.'
print('jargon' in sen)



#

length = len(python)
print(length)
py = float(length)
print(py)
py = str(py)
print(py)


# even or odd
x = int(input("Enter a number: "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")


#
flo = 7//3 
print(flo == int(2.7))


#
n = '10'
m = 10
print(n == m)

#
n12 = float('9.8')
num = int(n12)
if num == 10:
    print("True")
else:
    print("False")


#
hours = int(input("Enter hours:"))
rate = int(input("Enter rate per hour: "))
print("Your weekly earning is: ",hours*rate)


#
years = int(input("Enter number of years you have lived: "))
print("You have lived for ",years*365*60*60*24 ,"seconds.")

#
for i in range(1,6):
    print(i,1,i,i**2,i**3,sep ='\t',end = '\n')

