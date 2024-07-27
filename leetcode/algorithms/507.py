"""507. Perfect Number"""


class Solution:
    def check_perfect_number(self, num: int) -> bool:
        """
        Проверяет является ли число совершенным
        Совершенное число - это такое число, которое равно сумме своих 
        положительных делителей (исключая само число).
        """
        
        if num <= 1:
            return False
        
        sum_divisions = 1

        sqrt_num = int(num ** 0.5)

        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                sum_divisions += i

                if i != num // i:
                    sum_divisions += num // i
            
        
        return sum_divisions == num
    
    def check_perfect_number_2(self, num: int) -> bool:
       """
       Проверяет является ли число совершенным.
       Ищет среди известных совершенных чисел.
       Такой подход ограничен диапазоном известных совершенных 
       чисел и не будет работать для чисел, выходящих за этот диапазон
       """
       return num in [6,28,496,8128,33550336]

n = 28
print(Solution().check_perfect_number(n))
print(Solution().check_perfect_number_2(n))