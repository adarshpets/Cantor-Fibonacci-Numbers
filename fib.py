"""Fibonacci Number Generator"""
def main():
    """Take user input, returns Fibonacci numbers"""
    num_terms = input("Enter the number of Fibonacci terms: ")
    # Validates input - checks that the input is a non-negative number
    valid = num_terms.isnumeric()
    if valid:
        num_terms = int(num_terms)
        a, b = 1, 1
        # Loop iterates for the requested number of temrs
        for i in range(0, num_terms):
            print(a)
            a, b = b, a + b
            i += 1
    else:
        print("Invalid input. Input must be a numeric value.")


main()