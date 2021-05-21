#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
number=float(input("enter a number:"))
rem=number%2
if number<0:
    print(number," is not a positive integer")
elif rem==1 or rem==0 and number!=0:
    print(number," is a positive integer")
elif number==0:
    print(" the number is zero")
else:
     print(number," is not a positive integer")