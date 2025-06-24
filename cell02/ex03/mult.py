num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
output = num1*num2
print(f"{num1} x {num2} = {output}")
if output < 0:
     print ( "The result is negative.")
elif output > 0:
     print ( "The result is positive")
else:
     print ( "The result is positive and negative.")
