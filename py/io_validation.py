"EXERCISE 1"

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Display result
print("Result:", result)


"EXERCISE 2"
score = 0

print("Welcome to the LUCKYDRAW Quiz!")

# Question 1
answer1 = input("1. What is 5 + 3? ")
if answer1 == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
answer2 = input("2. What is my name? ")
if answer2.lower() == "Kasturi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
answer3 = input("3. What data type is used for decimal numbers? ")
if answer3.lower() == "float":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Final Score
print("\nQuiz Finished!")
print("Your final score is:", score, "/ 3")


def simple_calculator():
    """read two numbers and an operator from the user and print the result."""
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
    except ValueError:
        print("Please type valid numbers.")
        return

    op = input("Enter operation (+, -, *, /): ").strip()
    if op == "+":
        print("Result:", n1 + n2)
    elif op == "-":
        print("Result:", n1 - n2)
    elif op == "*":
        print("Result:", n1 * n2)
    elif op == "/":
        if n2 != 0:
            print("Result:", n1 / n2)
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation!")

if __name__ == "__main__":
    simple_calculator()

# ...existing code for the quiz follows...