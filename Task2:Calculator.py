a = float(input("Enter the first number: "))

print(" ")

b = float(input("Enter the second number: "))

print(" ")

print("addition = '+'")

print("subtraction = '-'")

print("multiplication = '*'")

print("division = '/'")

o = str(input("Enter the operator: "))

print(" ")

if o == '+':

    addition = a + b

    print("Sum = " + str(addition))

elif o == '-':

    difference = a - b

    print("difference = " + str(difference))

elif o == '*':

    product = a * b

    print("product = " + str(product))

elif o == '/':

    quotient = a + b

    print("quotient = " + str(quotient))

else :

    print("Invalid input")

print(" ")

print(" ")

print("************************Thanks for using our calculator*****************")

