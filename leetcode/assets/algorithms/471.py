"""476. Number Complement"""


class Solution:
    def findComplement(self, num: int) -> int:
        
        num_bits = num.bit_length()

        mask = (1 << num_bits) - 1
        return num ^ mask

n = 5
print(Solution().findComplement(n))