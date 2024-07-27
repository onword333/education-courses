"""504. Base 7"""


class Solution:

    def convert_to_base7(self, num: int) -> str:
        """
        Возвращает число в семеричной системе        
        """

        # Чтобы перевести целое число в его представление в семеричной системе счисления, 
        # нужно последовательно делить число на 7 и сохранять остатки. Также нужно учитывать 
        # отрицательные числа, если они есть. В конце, строку из остатков перевернуть.

        if num == 0:
            return '0'

        is_negative = num < 0
        num = abs(num)
        res = []

        while num > 0:
            res.append(str(num % 7))
            num //= 7

        if is_negative:
            res.append('-')

        return ''.join(res[::-1])

    def convert_to_base7_2(self, num: int) -> str:
        num, s = abs(num), ''
        while num:
            num, remain = divmod(num,7)
            s = str(remain) + s
        return "-" * (num < 0) + s or "0"


num = -7

print(Solution().convert_to_base7(num))
print(Solution().convert_to_base7_2(num))
