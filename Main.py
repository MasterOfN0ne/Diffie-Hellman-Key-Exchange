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

inputbinlist = []
keybinlist = []
result_list = []
result = []

EOD = int(input("Encrypt(1) or Decrypt(2)?: "))
if EOD == 1:
    user_input = input("Enter the text you would like to encrypt: ")
    key_input = input("Enter the key of the encrypted text: ")

    def iterate_to_match_length(short_str, long_str):
        short_len = len(short_str)
        long_len = len(long_str)
        iterations = long_len // short_len
        remainder = long_len % short_len

        repeated_str = short_str * iterations + short_str[:remainder]
        return repeated_str


    key_iterate1 = iterate_to_match_length(key_input, user_input)

    for c in user_input:
        input_binary = format(ord(c), '08b')  # Convert character to 8-bit binary string
        inputbinlist.append(input_binary)

    for c in key_iterate1:
        input_key = format(ord(c), '08b')  # Convert character to 8-bit binary string
        keybinlist.append(input_key)


    def xor_lists(list1, list2):

        for i in range(min(len(list1), len(list2))):
            result.append(''.join(str(int(x) ^ int(y)) for x, y in zip(list1[i], list2[i])))
        return result


    xor_result = xor_lists(inputbinlist, keybinlist)
    print("XOR result list:", xor_result)
elif EOD == 2:
    bin_key = []
    enc_txt_bin = []
    dec_key = input("Enter the key for decryption: ")
    enc_txt = input("Enter the encrypted text: ")


    def iterate_to_match_length(short_str, long_str):
        short_len = len(short_str)
        long_len = len(long_str)
        iterations = long_len // short_len
        remainder = long_len % short_len

        repeated_str = short_str * iterations + short_str[:remainder]
        return repeated_str

    key_iterate = iterate_to_match_length(dec_key, enc_txt)

    for c in key_iterate:
        key_binary = format(ord(c), '08b')  # Convert character to 8-bit binary string
        bin_key.append(key_binary)
    for a in enc_txt:
        txt_binary = format(ord(a), '08b')  # Convert character to 8-bit binary string
        enc_txt_bin.append(txt_binary)

    def xor_lists(list1, list2):
        result2 = []
        for i in range(min(len(list1), len(list2))):
            result2.append(''.join(str(int(x) ^ int(y)) for x, y in zip(list1[i], list2[i])))
        return result2


    xor_finalfinal = xor_lists(bin_key, enc_txt_bin)
    dec_chars = ''.join(chr(int(y, 2)) for y in xor_finalfinal)
    print(dec_chars)

else:
    print("Invalid option. Please enter 1 for encryption or 2 for decryption.")
