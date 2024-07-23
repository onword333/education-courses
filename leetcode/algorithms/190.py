"""
190. Reverse Bits
"""


def reverse_bits(n: int) -> int:
    result = 0
    for i in range(32):
        # Сдвигаем result влево на 1 бит
        result = (result << 1)
        # Добавляем младший бит n к result
        result = result | (n & 1)
        # Сдвигаем n вправо на 1 бит
        n = n >> 1
    return result


num = 8
print(reverse_bits(num))