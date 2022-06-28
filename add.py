def add_numbers(x, y):
    """
    Adds two numbers together and returns the result.
    Parameters:
        x - The first number
        y - The second number
    Returns:
        The sum of the two numbers
    """
    sum = x + y
    return sum

def main():
    num1 = int(input("What is your favorite number? "))
    num2 = int(input("What is your second number? "))
    result = add_numbers(num1, num2)
    print(f"The sum is {result}")

if __name__ == "__main__":
    main()

# result = add_numbers(12, 27)
# if result != 39:
#     print("Error! Bad result")

# result = add_numbers(-12, 27)
# if result != 15:
#     print("Error! Bad result (-12, 27) != 15")

# result = add_numbers(-12, -27)
# if result != -39:
#     print("Error! Bad result")

# result = add_numbers(0, 0)
# if result != 0:
#     print("Error! Bad result")


# print(add_numbers(12, 27))
# print(add_numbers(-12, 27))
# print(add_numbers(-12, -27))
# print(add_numbers(0, 0))
