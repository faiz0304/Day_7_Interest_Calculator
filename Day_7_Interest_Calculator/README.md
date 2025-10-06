# Day 7 - Simple & Compound Interest Calculator (Python Mini Project)

## Overview
This project contains three Python programs:
1. **Simple Interest Calculator** – Calculates interest using the formula `SI = (P × R × T) / 100`.
2. **Compound Interest Calculator** – Calculates compound interest with different compounding periods (yearly, quarterly, monthly, daily).
3. **Combined Interest Calculator** – A menu-based program allowing users to choose between simple or compound interest calculations.

Each calculator is designed with:
- Error handling for invalid inputs.
- Locale-based currency formatting.
- Option to re-run calculations without restarting the program.

---

## Formulas Used

### Simple Interest
\[
SI = \frac{P × R × T}{100}
\]

### Compound Interest
\[
A = P \times \left(1 + \frac{R}{100 × n}\right)^{n × T}
\]
\[
CI = A - P
\]

Where:
- **P** = Principal Amount  
- **R** = Rate of Interest (Annual %)  
- **T** = Time Period (in years)  
- **n** = Number of Compounding Periods (Yearly=1, Quarterly=4, Monthly=12, Daily=365)

---

## Features
- Calculates both **Simple** and **Compound Interest** accurately.
- Supports **multiple compounding frequencies**.
- **Formatted currency output** (PKR).
- **Error handling** for invalid numeric input.
- **Loop-based re-run** for continuous usage.
- **Menu-driven combined version** for easy selection.

---

## Sample Execution

### Example 1 – Simple Interest

=== Simple Interest Calculator ===
Enter Principal Amount (P): 10000
Enter Annual Interest Rate (%) (R): 10
Enter Time (in years) (T): 2

--- Result ---
Principal (P): 10000.0
Rate of Interest (R): 10.0%
Time Period (T): 2.0 years
Simple Interest (SI) PKR: ₨2,000.00
Total Amount (A) PKR: ₨12,000.00

Program Finished Successfully!

---

### Example 2 – Compound Interest

=== Compound Interest Calculator ===
Enter Principal Amount (P): 10000
Enter Annual Interest Rate (%) (R): 10
Enter Time (in years) (T): 2
Enter Number of Compounding periods
Yearly = 1
Quarterly = 4
Monthly = 12
Daily = 365 :==: 4

--- Result ---
Principal (P): 10000.0
Rate of Interest (R): 10.0%
Time Period (T): 2.0 years
Compounding Periods (Q): 4 quarterly
Compound Interest (CI) PKR: ₨2,028.64
Total Amount (A) PKR: ₨12,028.64

Program Finished Successfully!

---

### Example 3 – Combined Calculator

Welcome to simple + compound calculator

Simple Calculator

Compound Calculator

Exit: 1

=== Simple Interest Calculator ===
Enter Principal Amount (P): 5000
Enter Annual Interest Rate (%) (R): 8
Enter Time (in years) (T): 3

--- Result ---
Simple Interest (SI) PKR: ₨1,200.00
Total Amount (A) PKR: ₨6,200.00

## File Structure

Day7_Interest_Calculator/
│
├── simple_interest.py
├── compound_interest.py
├── combined_interest.py
├── README.md
├── output.txt
└── project.yml

yaml
Copy code

---

## Author
**Faiz Ur Rehman Ashrafi**  
Student | Electronics Engineering Technology  
Indus University, Karachi  