"""
283. Move Zeroes
Решим задачу с помощью алгоритма двух указателей или его еще называют
алгоритмом размещения ненулевых элементов. Если текущее значение не равно 0, 
то переместим его на место предыдущего не пустого значения

"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last_non_zero = 0 # отслеживает позицию последнего ненулевого элемента

        for i in range(len(nums)):
            if nums[i] != 0:
                # Меняем местами текущий элемент и элемент на позиции lastNonZeroFoundAt
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                # Перемещаем указатель lastNonZeroFoundAt вправо
                last_non_zero += 1


obj = Solution()
num = [0, 1, 1, 1]
obj.moveZeroes(num)
print(num)
