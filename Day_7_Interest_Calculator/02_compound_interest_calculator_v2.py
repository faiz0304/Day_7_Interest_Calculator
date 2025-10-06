# Day 7 Mini Project - Compound Interest Calculator
# Author: Faiz Ur Rehman Ashrafi
# Purpose: Calculate compound interest and total amount for different compounding periods.

import locale

print("=== Compound Interest Calculator ===")

# Setting locale for currency formatting (PKR)
try:
    locale.setlocale(locale.LC_ALL, "en_PK.UTF-8")
except locale.Error:
    print("Warning: 'en_PK.UTF-8' locale not found. Falling back to system default.")
    locale.setlocale(locale.LC_ALL, "")  # Fallback to default locale


def compound_calculator():
    """Function to calculate compound interest with user input."""
    try:
        # Taking user inputs
        principal = float(input("Enter Principal Amount (P): "))
        rate = float(input("Enter Annual Interest Rate (%) (R): "))
        time = float(input("Enter Time (in years) (T): "))
        period = float(
            input(
                "Enter Number of Compounding periods:\n"
                "Yearly = 1\nQuarterly = 4\nMonthly = 12\nDaily = 365\n:==: "
            )
        )

        # Validating positive inputs
        if principal <= 0 or rate <= 0 or time <= 0 or period <= 0:
            raise ValueError("All values must be greater than zero.")

        # Formula for Compound Interest:
        # A = P * (1 + R / (100 * n))^(n * T)
        # CI = A - P
        amount = principal * ((1 + (rate / (100 * period))) ** (period * time))
        compound_interest = amount - principal

    except ValueError as e:
        # Handle invalid or negative input
        print(f"Error: {e}")
    else:
        # Display results
        print("\n--- Result ---")
        print(f"Principal (P): Rs. {principal:,.2f}")
        print(f"Rate of Interest (R): {rate}%")
        print(f"Time Period (T): {time} years")

        # Display compounding period in words
        if period == 1:
            print(f"Compounding Periods (Y): {period} Yearly")
        elif period == 4:
            print(f"Compounding Periods (Q): {period} Quarterly")
        elif period == 12:
            print(f"Compounding Periods (M): {period} Monthly")
        elif period == 365:
            print(f"Compounding Periods (D): {period} Daily")
        else:
            print(f"Compounding Periods: {period} times per year")

        # Display formatted currency output
        print(
            f"Compound Interest (CI) PKR: {locale.currency(round(compound_interest, 2), grouping=True)}"
        )
        print(
            f"Total Amount (A = P + CI) PKR: {locale.currency(round(amount, 2), grouping=True)}"
        )
    finally:
        print("\nProgram Finished Successfully!")


# Main loop to allow multiple calculations
compound_calculator()
while True:
    again = input("Do you want to calculate again? (y/n): ")
    if again.lower() == "y":
        compound_calculator()
    else:
        print("Thanks for using the Compound Interest Calculator!")
        break
