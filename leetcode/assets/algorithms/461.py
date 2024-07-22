"""
461. Hamming Distance
Cравниv побитовое представление чисел и подсчитаем количество 
позиций, в которых биты различаются.
"""

class Solution:

    def hamming_distance(self, x: int, y: int) -> int:        
        return bin(x ^ y).count('1')

    def hamming_distance_2(self, x: int, y: int) -> int:
        bxor = x ^ y # применим исключаещие ИЛИ
        set_bit = 0

        while bxor > 0:
            # провем старший бит, если он равен 1, то складываем
            set_bit += bxor & 1

            #  смещаем вправо на 1 бит
            bxor >>= 1
        return set_bit


x = 3
y = 1

print(Solution().hamming_distance(x, y))
print(Solution().hamming_distance_2(x, y))