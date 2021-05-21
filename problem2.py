#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
number1=int(input("enter first integer:"))
number2=int(input("enter second integer:"))
if number1>number2:
    f1=number1
    f2=number2
else:
    f1=number2
    f2=number1
rem=f1%f2
if rem==0:
    print(f2," is a factor of ",f1)
else:
    print(f2," is not a factor of ",f1)
    