import math
import yaml
from fractions import Fraction
from sympy import gcd

def continued_fractions(n):
    """
    Generate a sequence of continued fractions for the square root of n.

    Parameters:
    n (int): The integer for which to compute the continued fractions.

    Returns:
    list: A list of Fraction objects representing the continued fractions.
    """
    x0 = int(math.isqrt(n))  # Initial approximation
    a0 = x0
    m = 0
    d = 1
    a = a0

    fractions = []

    while True:
        fractions.append(Fraction(a, 1))

        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d

        if d == 0:
            break

    return fractions

def rsa_attack(e, n):
    """
    Perform an RSA attack using continued fractions to factor n.

    Parameters:
    e (int): The public exponent.
    n (int): The modulus to factor.

    Returns:
    tuple: A tuple containing the factors p and q, or None if failed.
    """
    cf = continued_fractions(n)

    for i in range(1, len(cf)):
        p = cf[i].numerator
        q = n // p

        if p * q == n and gcd(e, (p - 1) * (q - 1)) == 1:
            print(f"Found factors: p = {p}, q = {q}")
            return p, q

    print("Failed to factor n.")
    return None

def main(yaml_file):
    """
    Main function to execute the RSA attack with parameters from a YAML file.

    Parameters:
    yaml_file (str): Path to the YAML configuration file containing e and n.
    """
    with open(yaml_file, 'r') as file:
        config = yaml.safe_load(file)

    # Convert hexadecimal values to integers
    e = int(config['e'], 16)
    n = int(config['n'], 16)

    print(f"Starting RSA attack with e = {e} and n = {n}...")
    rsa_attack(e, n)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python rsa_attack.py <path_to_yaml>")
        sys.exit(1)

    yaml_file = sys.argv[1]
    main(yaml_file)
