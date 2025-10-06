# Day 7 Mini Project - Simple + Compound Interest Calculator
# Author: Faiz Ur Rehman Ashrafi
# Purpose: To calculate both Simple and Compound Interest using user input.

import locale


# Helper function to display compounding period text
def compound_period(period):
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


# Setting locale for PKR currency formatting
try:
    locale.setlocale(locale.LC_ALL, "en_PK.UTF-8")
except locale.Error:
    print("Warning: 'en_PK.UTF-8' locale not found. Falling back to default.")
    locale.setlocale(locale.LC_ALL, "")  # Fallback to default locale


# ---------------- SIMPLE INTEREST CALCULATOR ----------------
def simple_calculator():
    print("=== Simple Interest Calculator ===")

    try:
        # Taking user inputs
        principal = float(input("Enter Principal Amount (P): "))
        rate = float(input("Enter Annual Interest Rate (%) (R): "))
        time = float(input("Enter Time (in years) (T): "))

        # Input validation for positive values
        if principal <= 0 or rate <= 0 or time <= 0:
            raise ValueError("All values must be greater than zero.")

        # Formula for Simple Interest: SI = (P × R × T) / 100
        simple_interest = (principal * rate * time) / 100

    except ValueError as e:
        print(f"Error: {e}")
    else:
        # Display formatted results
        print("\n--- Result ---")
        print(f"Principal (P): Rs. {principal:,.2f}")
        print(f"Rate of Interest (R): {rate}%")
        print(f"Time Period (T): {time} years")
        print(
            f"Simple Interest (SI) PKR: {locale.currency(round(simple_interest, 2), symbol=True, grouping=True)}"
        )
        print(
            f"Total Amount (A = P + SI) PKR: {locale.currency(round(principal + simple_interest, 2), symbol=True, grouping=True)}"
        )
    finally:
        print("\nProgram Finished Successfully!")

    # Ask user if they want to calculate again
    again = input("Do you want to calculate again? (y/n): ")
    if again.lower() == "y":
        simple_calculator()
    else:
        print("Thanks for using the Simple Interest Calculator!")
    return None


# ---------------- COMPOUND INTEREST CALCULATOR ----------------
def compound_calculator():
    print("=== Compound Interest Calculator ===")

    try:
        # Taking user inputs
        principal = float(input("Enter Principal Amount (P): "))
        rate = float(input("Enter Annual Interest Rate (%) (R): "))
        time = float(input("Enter Time (in years) (T): "))
        period = float(
            input(
                "Enter Number of Compounding periods\n"
                "Yearly = 1\nQuarterly = 4\nMonthly = 12\nDaily = 365\n:==: "
            )
        )

        # Input validation
        if principal <= 0 or rate <= 0 or time <= 0 or period <= 0:
            raise ValueError("All values must be greater than zero.")

        # Formula for Compound Interest
        amount = principal * ((1 + (rate / (100 * period))) ** (period * time))
        compound_interest = amount - principal

    except ValueError as e:
        print(f"Error: {e}")
    else:
        # Display formatted results
        print("\n--- Result ---")
        print(f"Principal (P): Rs. {principal:,.2f}")
        print(f"Rate of Interest (R): {rate}%")
        print(f"Time Period (T): {time} years")
        compound_period(period)
        print(
            f"Compound Interest (CI) PKR: {locale.currency(round(compound_interest, 2), symbol=True, grouping=True)}"
        )
        print(
            f"Total Amount (A = P + CI) PKR: {locale.currency(round(amount, 2), symbol=True, grouping=True)}"
        )
    finally:
        print("\nProgram Finished Successfully!")

    # Ask user if they want to calculate again
    again = input("Do you want to calculate again? (y/n): ")
    if again.lower() == "y":
        compound_calculator()
    else:
        print("Thanks for using the Compound Interest Calculator!")
    return None


# ---------------- MAIN MENU ----------------
print("=== Welcome to Simple + Compound Interest Calculator ===")

while True:
    try:
        choice = int(
            input("1. Simple Calculator\n2. Compound Calculator\n3. Exit\n:==: ")
        )
        if choice == 1:
            simple_calculator()
        elif choice == 2:
            compound_calculator()
        elif choice == 3:
            print("Thanks for using the Interest Calculator! Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Please enter a numeric value (1, 2, or 3).")
