def subtract_numbers(num1, num2):
    return num1 - num2

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = subtract_numbers(num1, num2)
    print("The result is:", result)

if __name__ == "__main__":
    main()
