# program to print sum of two numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=a+b
print("The sum of", a, "and", b, "is:", sum)

#program to print the difference of two numbers
diff = a - b
print("The difference of", a, "and", b, "is:", diff)

# program to print the product of two numbers
product = a * b
print("The product of", a, "and", b, "is:", product)

#program to print the division of two numbers
if b != 0:
    division = a / b
    print("The division of", a, "and", b, "is:", division)
else:
    print("Division by zero is not allowed.")