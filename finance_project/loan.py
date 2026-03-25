import math

def monthly_payment(principal, annual_rate, years):
    if principal <= 0:
        raise ValueError("Principal must be positive")
    
    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative")
    
    if years <= 0:
        raise ValueError("Years must be positive")

    monthly_rate = annual_rate / 12
    total_payments = years * 12

    if monthly_rate == 0:
        return principal / total_payments

    numerator = principal * (monthly_rate * (1 + monthly_rate) ** total_payments)
    denominator = ((1 + monthly_rate) ** total_payments) - 1

    return numerator / denominator

def total_payment(monthly_payment, years):
    return monthly_payment * years * 12

def total_interest(total_paid, principal):
    return total_paid - principal
