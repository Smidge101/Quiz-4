wanted_info = input("Choose your math operation: +, -, *, /: ")

if wanted_info == "+":
    add_num1 = int(input("Enter the first number: "))
    add_num2 = int(input("Enter the second number: "))

    print("The answer is: " + str(add_num1 + add_num2))
