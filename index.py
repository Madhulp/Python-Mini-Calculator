# python mini calculator

first = int(input("Enter a Number: "))
operator = input("Enter Operator: ")
second = int(input("Enter a Number: "))

if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "/":
    print(first/second)
elif operator == "*":
    print(first*second)
