from Decorators import timer, standard_format, tax_authority_format, securities_agency_format


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@timer
def find_primes():
    primes = []
    for num in range(2, 1001):
        if is_prime(num):
            primes.append(num)
    return primes


@timer
def find_primes2(start=2, end=1000):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


@standard_format
def generate_financial_statement():
    """Generate the core financial statement."""
    # Example based on Tesla/SpaceX hypothetical data
    return (
        "Revenue: $80,000,000,000\n"
        "Expenses: $65,000,000,000\n"
        "Net Profit: $15,000,000,000"
    )


@tax_authority_format
def generate_tax_statement():
    # Example based on hypothetical tax information
    return (
        "Revenue: $80,000,000,000\n"
        "Expenses: $65,000,000,000\n"
        "Tax Due: $3,000,000,000"
    )


@securities_agency_format
def generate_securities_statement():
    # Example based on publicly traded company metrics
    return (
        "Revenue: $80,000,000,000\n"
        "Expenses: $65,000,000,000\n"
        "Earnings Per Share: $8.50"
    )
