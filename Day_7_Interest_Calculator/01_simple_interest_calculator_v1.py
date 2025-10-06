# Day 7 Mini Project - Simple Interest Calculator
# Author: Faiz Ur Rehman Ashrafi
# Purpose: To calculate Simple Interest and Total Amount from user input values.

print("=== Simple Interest Calculator ===")

try:
    # Taking user inputs and converting them to float for decimal support
    principal = float(input("Enter Principal Amount (P): "))
    rate = float(input("Enter Annual Interest Rate (%) (R): "))
    time = float(input("Enter Time (in years) (T): "))

    # Validating that values must be positive
    if principal <= 0 or rate <= 0 or time <= 0:
        raise ValueError("All values must be greater than zero.")

    # Formula for Simple Interest
    # SI = (P × R × T) / 100
    simple_interest = (principal * rate * time) / 100

except ValueError as e:
    # Handles invalid or negative input
    print(f"Error: {e}")
else:
    # Display the calculated results
    print("\n--- Result ---")
    print(f"Principal (P): Rs. {principal:,.2f}")
    print(f"Rate of Interest (R): {rate}%")
    print(f"Time Period (T): {time} years")
    print(f"Simple Interest (SI): Rs. {simple_interest:,.2f}")
    print(f"Total Amount (A = P + SI): Rs. {principal + simple_interest:,.2f}")
finally:
    # This block runs no matter what (for cleanup / closing message)
    print("\nProgram Finished Successfully!")
