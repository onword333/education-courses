"""496. Next Greater Element I"""

class Solution:

    def next_greater_element(self, nums1, nums2):
        res = []
        len_nums2 = len(nums2)

        for n1 in nums1:
            find_idx = nums2.index(n1)

            next_greater_el = -1
            for g in range(find_idx, len_nums2):
                if nums2[g] > n1:
                    next_greater_el = nums2[g]
                    break    
                
            res.append(next_greater_el)
            
        return res


    def next_greater_element_2(self, nums1, nums2):
        # Словарь для хранения следующего большего элемента
        next_greater = {}
        # Стек для отслеживания элементов, для которых еще не найден следующий больший элемент
        stack = []

        # Проходим по массиву nums2 справа налево
        for num in reversed(nums2):
            # Удаляем элементы из стека, которые меньше или равны текущему элементу
            while stack and stack[-1] <= num:
                stack.pop()
            # Если стек не пуст, следующий больший элемент будет на вершине стека
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            # Добавляем текущий элемент в стек
            stack.append(num)

        # Формируем ответ для nums1
        return [next_greater[num] for num in nums1]


    def next_greater_element_3(self, nums1, nums2):
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [next_greater.get(num, -1) for num in nums1]


nums1, nums2 = [4,1,2], [1,3,4,2]

print(Solution().next_greater_element(nums1, nums2))
print(Solution().next_greater_element_2(nums1, nums2))
print(Solution().next_greater_element_3(nums1, nums2))
