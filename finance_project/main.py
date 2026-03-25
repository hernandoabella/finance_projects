from loan import monthly_payment, total_payment, total_interest

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Loan Calculator ===")

    principal = get_float_input("Loan amount: ")
    annual_rate = get_float_input("Annual interest rate (e.g. 0.05 for 5%): ")
    years = get_float_input("Loan term (years): ")

    try:
        payment = monthly_payment(principal, annual_rate, years)
        total_paid = total_payment(payment, years)
        interest_paid = total_interest(total_paid, principal)

        print("\n--- Results ---")
        print(f"Monthly payment: {payment:.2f}")
        print(f"Total paid: {total_paid:.2f}")
        print(f"Total interest: {interest_paid:.2f}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
