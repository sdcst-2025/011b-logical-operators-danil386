#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

x = input("enter an integer")
y = input("enter an integer")
z = input("enter an integer")
x = float(x)
y = float(y)
z = float(z)
c = max(x,y,z)
b = min(x,y,z)

if x != c or b:
    a = x
if z != c or b:
    a = z
if y != c or b:
    a = y

if (a**2 + b**2) == c**2:
    print(f"{x}, {y}, {z} form a Pythagorean triple")
else:
    print(f"{x}, {y}, {z} do not form a Pythagorean triple")