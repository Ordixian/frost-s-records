#!/usr/bin/env python3
"""
Simple Interest Calculator

This program calculates Simple Interest for varying principal amounts
using the formula: Simple Interest = (P × T × R) / 100

Where:
- P is the Principal amount
- T is the Time period (in years)
- R is the Rate of interest per annum
"""

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

def main():
    """
    Main function to calculate Simple Interest for varying principal amounts
    """
    # Fixed values as per the problem
    time_period = 2  # years
    interest_rate = 5  # percent per annum
    
    print("Simple Interest Calculator")
    print("=" * 50)
    print(f"Time Period: {time_period} years")
    print(f"Interest Rate: {interest_rate}% per annum")
    print("=" * 50)
    print(f"{'Principal (P)':<15} {'Simple Interest':<20} {'Total Amount':<15}")
    print("-" * 50)
    
    # Calculate Simple Interest for principal amounts from 1 to 20
    for principal in range(1, 21):
        simple_interest = calculate_simple_interest(principal, time_period, interest_rate)
        total_amount = principal + simple_interest
        
        print(f"{principal:<15} {simple_interest:<20.2f} {total_amount:<15.2f}")
    
    print("\n" + "=" * 50)
    print("Formula used: Simple Interest = (P × T × R) / 100")

if __name__ == "__main__":
    main()