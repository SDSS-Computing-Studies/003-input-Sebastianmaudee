#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704
A = input("enter 1 short side of triangle")
B = input("second short side of a triangle")
A = float(A)
B = float(B)
C = A ** (2) + B ** (2)
C2 = C ** (1/2)
print(C2)