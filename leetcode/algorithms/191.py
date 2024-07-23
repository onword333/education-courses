"""
191. Number of 1 Bits
"""


def count_set_bits(n):
    # Convert the integer to a binary string
    binary_representation = bin(n)    
    return binary_representation.count('1')


num = 11
print(count_set_bits(num))