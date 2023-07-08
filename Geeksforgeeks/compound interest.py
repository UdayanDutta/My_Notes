def calculate_compound_interest(principle, rate, time):
    amount = principle * (pow(1 + rate / 100, time))
    compound_interest = amount - principle
    print('Compound interest is', compound_interest)

# driver code
calculate_compound_interest(1000, 10.25, 5)
