# Imports (sympy, random)
from sympy import *
import random

# Define prime number generator using sympy to check if number is prime.
def generate_prime():
    while True:
        num = random.randint(10, 1000)
        if isprime(num):
            return num

# Define primitive root finder for prime number, using sympy.
def find_primitive_root(n):
    if not isprime(n):
        return None  # Primitive root only exists for prime moduli
    return primitive_root(n)


# Example usage:
p = generate_prime()
g = find_primitive_root(p)  # Example prime modulus

# A is Alice public key, a is private, same for Bob, B is public, b is private
# p is prime number, g is shared secret.
# Eve gets the secrets with g^ab mod p.
# S = B^a mod p
# Now we generate Alice's private key
a = random.randint(1, p - 1)
# Alice's public key
A = (g ** a) % p
# Bob's private key
b = random.randint(1, p - 1)
# Bob's public key
B = (g ** b) % p
# Alice calculates the shared secret key
shared_secret_key_A = (B ** a) % p
# Bob calculates the shared secret key
shared_secret_key_B = (A ** b) % p
# Check if the shared secret keys are equal

print("DH Key Exchange Protocol:")
if shared_secret_key_A == shared_secret_key_B:
    print("Shared secret keys match!")

else:
    print("Shared secret keys do not match!")


# This function prints a table with three columns: Alice, Bob and Eve. The table shows a, b, A, B, and S for Alice, Bob and Eve.
# Eve is an eavesdropper who intercepts the public keys A and B exchanged between Alice and Bob.

def finalTable(a, b, A, B, Sa, Sb):
    # Print the table header
    print("Alice\tBob\t\tEve")

    # Print the values of a, b, A, B, and S for Alice, Bob and Eve
    print(str(a) + "\t\t" + str(b) + "\t\t" + "Nothing")
    print(str(A) + "\t\t" + str(B) + "\t\t" + "Alice and Bob's public keys")
    print(str(Sa) + "\t\t" + str(Sb) + "\t\t" + str((A ** B) % p))


finalTable(a, b, A, B, shared_secret_key_A, shared_secret_key_B)

