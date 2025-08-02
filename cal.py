def calculate_bmi(weight_kg, height_m):
    """Calculate BMI given weight in kg and height in meters"""
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi):
    """Classify BMI into categories"""
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal weight"
    elif 25 <= bmi < 30:
        return "overweight"
    else:
        return "obese"

def main():
    print("BMI Calculator")
    print("-------------")
    
    try:
        # Get user input
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Validate input
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers.")
            return
        
        # Calculate and display results
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"\nYour BMI is: {bmi:.1f}")
        print(f"Classification: {category}")
        
        # Display BMI categories for reference
        print("\nBMI Categories:")
        print("Underweight: BMI < 18.5")
        print("Normal weight: 18.5 ≤ BMI < 25")
        print("Overweight: 25 ≤ BMI < 30")
        print("Obese: BMI ≥ 30")
        
    except ValueError:
        print("Error: Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()