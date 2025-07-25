#!/usr/bin/env python3
"""
Enhanced Simple Interest Calculator

This program calculates Simple Interest with flexible input options
using the formula: Simple Interest = (P × T × R) / 100
"""

import sys

def calculate_simple_interest(principal, time, rate):
    """
    Calculate Simple Interest using the formula: (P × T × R) / 100
    
    Args:
        principal (float): Principal amount
        time (float): Time period in years
        rate (float): Rate of interest per annum
    
    Returns:
        float: Simple Interest
    """
    return (principal * time * rate) / 100

def calculate_range(start_p, end_p, time, rate):
    """
    Calculate Simple Interest for a range of principal values
    
    Args:
        start_p (int): Starting principal amount
        end_p (int): Ending principal amount
        time (float): Time period in years
        rate (float): Rate of interest per annum
    """
    print(f"\nSimple Interest Calculator - Range Analysis")
    print("=" * 60)
    print(f"Principal Range: {start_p} to {end_p}")
    print(f"Time Period: {time} years")
    print(f"Interest Rate: {rate}% per annum")
    print("=" * 60)
    print(f"{'Principal':<12} {'Simple Interest':<18} {'Total Amount':<15} {'Interest %':<12}")
    print("-" * 60)
    
    for principal in range(start_p, end_p + 1):
        simple_interest = calculate_simple_interest(principal, time, rate)
        total_amount = principal + simple_interest
        interest_percentage = (simple_interest / principal) * 100 if principal > 0 else 0
        
        print(f"{principal:<12} {simple_interest:<18.2f} {total_amount:<15.2f} {interest_percentage:<12.1f}%")

def calculate_single(principal, time, rate):
    """
    Calculate Simple Interest for a single set of values
    """
    simple_interest = calculate_simple_interest(principal, time, rate)
    total_amount = principal + simple_interest
    
    print(f"\nSimple Interest Calculation")
    print("=" * 40)
    print(f"Principal Amount: ${principal:.2f}")
    print(f"Time Period: {time} years")
    print(f"Interest Rate: {rate}% per annum")
    print("-" * 40)
    print(f"Simple Interest: ${simple_interest:.2f}")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Interest Percentage: {(simple_interest/principal)*100:.1f}%")

def main():
    """
    Main function with menu-driven interface
    """
    print("Simple Interest Calculator")
    print("=" * 50)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--default":
        # Run the default scenario from the problem
        calculate_range(1, 20, 2, 5)
        return
    
    print("Choose an option:")
    print("1. Calculate for the given problem (P: 1-20, T: 2 years, R: 5%)")
    print("2. Calculate for a custom range of principal amounts")
    print("3. Calculate for a single set of values")
    print("4. Exit")
    
    try:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            calculate_range(1, 20, 2, 5)
            
        elif choice == "2":
            start_p = int(input("Enter starting principal amount: "))
            end_p = int(input("Enter ending principal amount: "))
            time = float(input("Enter time period (years): "))
            rate = float(input("Enter interest rate (% per annum): "))
            calculate_range(start_p, end_p, time, rate)
            
        elif choice == "3":
            principal = float(input("Enter principal amount: "))
            time = float(input("Enter time period (years): "))
            rate = float(input("Enter interest rate (% per annum): "))
            calculate_single(principal, time, rate)
            
        elif choice == "4":
            print("Thank you for using the Simple Interest Calculator!")
            return
            
        else:
            print("Invalid choice. Please run the program again.")
            
    except ValueError:
        print("Error: Please enter valid numeric values.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    
    print("\n" + "=" * 50)
    print("Formula used: Simple Interest = (P × T × R) / 100")
    print("Where P = Principal, T = Time (years), R = Rate (% per annum)")

if __name__ == "__main__":
    main()