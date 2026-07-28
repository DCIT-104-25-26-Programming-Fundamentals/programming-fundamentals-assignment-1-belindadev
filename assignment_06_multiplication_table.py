# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_single_table(num):
    """Prints the multiplication table for a given number from 1 to 12."""
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")


def generate_all_tables(n):
    """Prints multiplication tables for numbers from 1 to N with separators."""
    for i in range(1, n + 1):
        print_single_table(i)
        if i < n:
            print("---")


def main():
    # PART A: Single Table
    user_input = input("Enter a number for Part A: ")
    
    # Input Validation (Must be a positive integer)
    if not user_input.isdigit() or int(user_input) <= 0:
        print("Error: Input must be a positive integer.")
        return

    num = int(user_input)
    print_single_table(num)

    # PART B: Bonus - Tables from 1 to N
    print("\n-----------------------------------")
    bonus_input = input("Enter a number N for Part B: ")

    if not bonus_input.isdigit() or int(bonus_input) <= 0:
        print("Error: Input must be a positive integer.")
        return

    n = int(bonus_input)
    generate_all_tables(n)


if __name__ == "__main__":
    main()