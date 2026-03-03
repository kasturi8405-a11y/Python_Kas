
def bmi_calculator():
    """Calculate BMI and categorize based on weight status."""
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
        return
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Categorize BMI
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal Weight"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    
    # Display results
    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    bmi_calculator()



weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

# Categorize BMI
if bmi < 18.5:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal weight"
elif bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

print("Category:", category)