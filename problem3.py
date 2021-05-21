#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
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
number1=int(input("enter first integer:"))
number2=int(input("enter second integer:"))
number3=int(input("enter third integer:"))
if number1>number2 and number2>number3 and number1>number3:
    max=number1
    mid=number2
    min=number3
elif number1>number2 and number2<number3 and number2>number3:
    max=number1
    mid=number3
    min=number2
elif number2>number1 and number2>number3 and number1>number3:
    max=number2
    mid=number1
    min=number3
elif number2>number1 and number2>number3 and number1<number3:
    max=number2
    mid=number3
    min=number1
elif number3>number1 and number3>number2 and number1>number2:
    max=number3
    mid=number1
    min=number2
elif number3>number1 and number3>number2 and number1<number2:
    max=number3
    mid=number2
    min=number1
if max**2==(mid**2+min**2):
    print(max,",",mid,",",min," form a Pythagorean Triple.")
else:
    print(max,",",mid,",",min," do not form a Pythagorean Triple.")
    