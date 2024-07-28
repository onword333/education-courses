[back](../README.md)

# Алгоритмы

## 9. Palindrome Number
```python
class Solution:
  def isPalindrome(self, x: int) -> bool:
    num_str = str(x)

    if num_str == num_str[::-1]:
      return True
    else:
      return False
```

## 14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
```python
class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
      return ""

    # по умолчанию прфекс будет = первому элементу
    prefix = strs[0]

    for string in strs[1:]:
      while string.find(prefix) != 0:   # выполняем пока не найдем общий префикс
        prefix = prefix[:-1]            # убираем один символ с конца до тек пор пока не найдем общий префикс,
        if not prefix:                  # если не найден, то
          return ""                     # возвращаем пустую строку

    return prefix
```

## 20. Valid Parentheses
[promlem](https://leetcode.com/problems/valid-parentheses/description/)

Эту проблему можно решить, используя структуру данных стека. Основная идея состоит в том, чтобы перебирать строку, помещая открывающие скобки в стек и извлекая их из стека всякий раз, когда встречается закрывающая скобка. Если в какой-либо момент закрывающая скобка не соответствует соответствующей открывающей скобке наверху стека или стек пуст при обнаружении закрывающей скобки, то строка недействительна.

```python
class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    brackets = {
      ')': '(', 
      '}': '{', 
      ']': '['
    }

    for char in s:
      if char in brackets.values():
        stack.append(char)
      elif char in brackets.keys():
        if not stack or brackets[char] != stack.pop():
          return False
      else:
        return False

    return not stack
```

## 1929. Concatenation of Array
[source](https://leetcode.com/problems/concatenation-of-array/)

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

```python
class Solution:
  def getConcatenation(self, nums: List[int]) -> List[int]:
    ans = []
    
    for n in range(0, 2):
      for num in nums:
        ans.append(num)
    
    return ans
```

вариант 2
```python
class Solution:
  def getConcatenation(self, nums: List[int]) -> List[int]:
    return nums + nums
```

## 1920. Build Array from Permutation
[source](https://leetcode.com/problems/build-array-from-permutation/description/)

Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

```python
class Solution:
  def buildArray(self, nums: List[int]) -> List[int]:
    ans = [None] * len(nums)

    for i in range(0, len(nums)):
      ans[i] = nums[nums[i]]

    return ans
```

## 1108. Defanging an IP Address
[source](https://leetcode.com/problems/defanging-an-ip-address/description/)

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

```python
class Solution:
  def defangIPaddr(self, address: str) -> str:
    return address.replace('.', '[.]')
```

## 1512. Number of Good Pairs
[source](https://leetcode.com/problems/number-of-good-pairs/description/)

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Вариант 1 c двумяя циклами
```python
class Solution:
  def numIdenticalPairs(self, nums: List[int]) -> int:
    nums_range = range(len(nums))

    good_pairs = []

    for i in nums_range:  
      for j in nums_range:
        if (nums[i] == nums[j] and i < j):
          good_pairs.append([i, j])

    return len(good_pairs)
```

Вариант 2 без с одним циклом
```python
class Solution:
  def numIdenticalPairs(self, nums: List[int]) -> int:    
    count = {}
    good_pairs = 0

    for num in nums:
      if num in count:
        good_pairs += count[num]
        count[num] += 1
      else:
        count[num] = 1

    return good_pairs
```

## 1. Two Sum
[source](https://leetcode.com/problems/number-of-good-pairs/description/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Можно решить эту проблему, используя dict для хранения индексов чисел при переборе массива. При переборе массива для каждого числа можно проверить, существует ли дополнение этого числа (цель - текущее число) в хеш-карте. Если это так, то мы нашли пару чисел, которые в сумме соответствуют цели.

```python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_indices = {}

    for i, num in enumerate(nums):
      complement = target - num
      if complement in num_indices:
        return [num_indices[complement], i]
      
      num_indices[num] = i
```

## 13. Roman To Integer
[source](https://leetcode.com/problems/roman-to-integer/description/)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Эту проблему можно решить, перебирая строку римских цифр и суммируя соответствующие целочисленные значения на основе предоставленных правил. Когда мы встречаем римскую цифру, обозначающую вычитание (например, IV, IX, XL, XC, CD, CM), нам нужно поступить с ней по-другому и примерить формулу (тек. значение - 2 * пред. значение)

```python
class Solution:
  def romanToInt(self, s: str) -> int:
    roman_values = {
      'I': 1, 
      'V': 5, 
      'X': 10, 
      'L': 50, 
      'C': 100, 
      'D': 500, 
      'M': 1000
    }

    total = 0
    prev_value = 0

    for roman in s:
      curr_value = roman_values[roman]
      
      if curr_value > prev_value:
        total += curr_value - 2 * prev_value
      else:
        total += curr_value
      
      prev_value = curr_value

    return total
```

## 21. Merge Two Sorted Lists
[source](https://leetcode.com/problems/merge-two-sorted-lists/description/)

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    # создадим фиктивный узел, который будет
    # служить первым узлом в одно связанном списке
    dummy = ListNode(0)

    # указатель для дальнейшего перемещения по списку
    cur = dummy

    ## обходим одновременно два списка
    while list1 and list2:    
      # сортировка должна быть по возвр.
      if list1.val < list2.val:
        cur.next = list1
        list1 = list1.next
      else:
        cur.next = list2
        list2 = list2.next    
      
      cur = cur.next

    # присоединяем оставшиеся ноды из list1 или list2
    cur.next = list1 if list1 else list2

    return dummy.next
```

## 26. Remove Duplicates from Sorted Array
[source](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.

Constraints:

- 1 <= nums.length <= 3 * 104
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.

```python
class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
      return 0
    
    # Инициализируем указатель для отслеживания позиции, 
    # в которой должен быть размещен следующий уникальный элемент
    unique_index = 1
    
    # перебираем элементы начиная со второго элемента
    for i in range(1, len(nums)):
      # если текущий элемент отличиается от предыдущего,
      # то поместим его в позицию, указнную в unique_index
      if nums[i] != nums[i - 1]:
        nums[unique_index] = nums[i]
        unique_index += 1
    
    return unique_index
```

## 27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]


Explanation: Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores).

### Solution

```python
class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
      if nums[i] != val:
        nums[k] = nums[i]
        k += 1
    
    return k
```

## 28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0

Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

```python
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    return haystack.find(needle)
```

## 35. Search Insert Position
[source](https://leetcode.com/problems/search-insert-position/description/)

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:

    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:

  Input: nums = [1,3,5,6], target = 7
  Output: 4

### Solution
We can use Binary Search

```python
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
      mid = left + (right - left) // 2

      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1      

    return left
```

## 58. Length of Last Word
[source](https://leetcode.com/problems/length-of-last-word/description/)

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

    Input: s = "Hello World"
    Output: 5

Explanation: The last word is "World" with length 5.

Example 2:

    Input: s = "   fly me   to   the moon  "
    Output: 4

Explanation: The last word is "moon" with length 4.

Example 3:

    Input: s = "luffy is still joyboy"
    Output: 6

Explanation: The last word is "joyboy" with length 6.

### Solution

```python
class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    words = s.strip().split(sep=' ')
    return len(words[-1])
```

## 66. Plus One 
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

    Input: digits = [1,2,3]
    Output: [1,2,4]

Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]

Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

    Input: digits = [9]
    Output: [1,0]

Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

### Solution

```python
class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    n = len(digits)
    for i in range(n - 1, -1, -1):
      digits[i] += 1

      if digits[i] < 10:
        return digits
      
      digits[i] = 0

    return [1] + digits 
```

## 67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:

    Input: a = "11", b = "1"
    Output: "100"

Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"
 

Constraints:

- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.

### Solution

```python
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    sum_ab = int(a, 2) + int(b, 2)
    return bin(sum_ab)[2:]        
```

## 69. Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.

Example 2:

    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

### Solution 1
runtime 1087 ms
```python
class Solution:
  def mySqrt(self, x: int) -> int:
    if (x == 0 or x == 1):
      return x

    result, i = 1, 1
    
    while (result <= x):
      i += 1
      result = i * i

    return i - 1
```

### Solution 2
binary search

runtime 35 ms
```python
class Solution:
  def mySqrt(self, x: int) -> int:
    if x == 0:
      return 0
    
    left, right = 1, x
    while left <= right:
      mid = (left + right) // 2
      if mid * mid == x:
        return mid
      elif mid * mid < x:
        left = mid + 1
      else:
        right = mid - 1
    
    return right
```

## 70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

### Solution 1
[dynamic programming](https://youtu.be/4ikxUxiEB10)

```python
class Solution:
  def climbStairs(self, n: int) -> int:
    if n == 1:
      return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

### Solution 2
```python
class Solution:
  def climbStairs(self, n: int) -> int:
    a, b = 0, 1
    for i in range(n):
      a, b = b, a + b
    return b
```

## 83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

    Input: head = [1,1,2]
    Output: [1,2]

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    while (cur and cur.next):      
      if (cur.val == cur.next.val):
        cur.next = cur.next.next
      else:
        cur = cur.next    
    return head
```

## 88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].

Example 3:

    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

### Solution 1
```python
class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    res = (nums1 + nums2)

    total = m + n

    c = 0
    for i in range(m, total):
      if n > 0:
        nums1[i] = nums2[c]
        c += 1  

    nums1.sort()
```

### Solution 2
```python
class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    a, b, write_index = m-1, n-1, m + n - 1

    while b >= 0:
      if a >= 0 and nums1[a] > nums2[b]:
        nums1[write_index] = nums1[a]
        a -= 1
      else:
        nums1[write_index] = nums2[b]
        b -= 1

      write_index -= 1
```

## 94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.



![](./assets/inorder_1.jpg)

Example 1:

    Input: root = [1,null,2,3]
    Output: [1,3,2]

Example 2:

    Input: root = []
    Output: []

Example 3:

    Input: root = [1]
    Output: [1]

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

### Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:    
    res = []
    if root is None:
      return res

    stack = []
    cur = root

    while cur or stack:
      while cur:
        stack.append(cur)
        cur = cur.left

      cur = stack.pop()
      res.append(cur.val)
      cur = cur.right
    
    return res
```

## 100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Example 1:

![](./assets/ex1.jpg)

    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:

![](./assets/ex2.jpg)

    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:

![](./assets/ex3.jpg)

    Input: p = [1,2,1], q = [1,1,2]
    Output: false

### Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
      return True
    elif not p or not q:
      return False
    
    queue = [(p, q)]

    while queue:
      node_p, node_q = queue.pop(0)

      if not node_p and not node_q:
        continue
      elif not node_p or not node_q:
        return False
      elif node_p.val != node_q.val:
        return False
      
      queue.append((node_p.left, node_q.left))
      queue.append((node_p.right, node_q.right))

    return True 
```

## 101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1

![](./assets/symtree1.jpg)

    Input: root = [1,2,2,3,4,4,3]
    Output: true

Example 2

![](./assets/symtree2.jpg)

    Input: root = [1,2,2,null,3,null,3]
    Output: false

### Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return True
  
    stack = [(root.left, root.right)]

    while stack:
      left, right = stack.pop()
      if not left and not right:
          continue
      if not left or not right or left.val != right.val:
          return False
      stack.append((left.left, right.right))
      stack.append((left.right, right.left))

    return True
```

## 104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

![](./assets/tmp-tree.jpg)

    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:

    Input: root = [1,null,2]
    Output: 2

### Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    max_depth = 0

    if not root:
      return max_depth
    
    queue = [(root, 1)]

    while queue:
      node, depth = queue.pop(0)
      max_depth = max(max_depth, depth)

      if node.left:
        queue.append((node.left, depth + 1))

      if node.right:
        queue.append((node.right, depth + 1))

    return max_depth
```

## 121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

[Solution](./121.py)

## 125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:
    
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
 

[Solution](./125.py)

## 136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

    Example 1:
    Input: nums = [2,2,1]
    Output: 1

    Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

    Example 3:
    Input: nums = [1]
    Output: 1

[Solution](./136.py)

## 168. Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
 
    Example 1:
    Input: columnNumber = 1
    Output: "A"

    Example 2:
    Input: columnNumber = 28
    Output: "AB"

    Example 3:
    Input: columnNumber = 701
    Output: "ZY"

[Solution](./168.py)

## 169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    Example 1:
    Input: nums = [3,2,3]
    Output: 3

    Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Follow-up: Could you solve the problem in linear time and in O(1) space?

[Solution](./169.py)

## 171. Excel Sheet Column Number
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

    For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    

    Example 1:

    Input: columnTitle = "A"
    Output: 1
    Example 2:

    Input: columnTitle = "AB"
    Output: 28
    Example 3:

    Input: columnTitle = "ZY"
    Output: 701

## 190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

    Example 1:
    Input: n = 00000010100101000001111010011100
    Output:    964176192 (00111001011110000010100101000000)
    Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

    Example 2:
    Input: n = 11111111111111111111111111111101
    Output:   3221225471 (10111111111111111111111111111111)
    Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 
Constraints:

The input must be a binary string of length 32

[Solution](./190.py)

## 191. Number of 1 Bits
Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).

    Example 1:
    Input: n = 11
    Output: 3
    Explanation:
    The input binary string 1011 has a total of three set bits.

    Example 2:
    Input: n = 128
    Output: 1
    Explanation:
    The input binary string 10000000 has a total of one set bit.

    Example 3:
    Input: n = 2147483645
    Output: 30

    Explanation:
    The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

[Solution](./191.py)

## 202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

    Example 1:

    Input: n = 19
    Output: true
    Explanation:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
    Example 2:

    Input: n = 2
    Output: false

[Solution](./202.py)

## 205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

    Input: s = "egg", t = "add"
    Output: true
    Example 2:

    Input: s = "foo", t = "bar"
    Output: false
    Example 3:

    Input: s = "paper", t = "title"
    Output: true

[Solution](./205.py)

## 217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

    Input: nums = [1,2,3,1]
    Output: true
    Example 2:

    Input: nums = [1,2,3,4]
    Output: false
    Example 3:

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true
 
[Solution](./217.py)

## 219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

    Input: nums = [1,2,3,1], k = 3
    Output: true
    Example 2:

    Input: nums = [1,0,1,1], k = 1
    Output: true
    Example 3:

    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

[Solution](./219.py)

PS: Иными словами, мы ищем пару элементов с одинаковыми значениями, которые находятся на расстоянии не более k друг от друга. Если такая пара существует, возвращаем True, иначе возвращаем False.

## 228. Summary Ranges
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b
 

Example 1:

    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"

Example 2:

    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
    [0,0] --> "0"
    [2,4] --> "2->4"
    [6,6] --> "6"
    [8,9] --> "8->9"

[Solution](./228.py)

## 231. Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
    Input: n = 1
    Output: true
    Explanation: 20 = 1

Example 2:

    Input: n = 16
    Output: true
    Explanation: 24 = 16

Example 3:

    Input: n = 3
    Output: false

[Solution](./231.py)

## 232. Implement Queue using Stacks
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:

- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
Example 1:

    Input
    ["MyQueue", "push", "push", "peek", "pop", "empty"]
    [[], [1], [2], [], [], []]
    Output
    [null, null, null, 1, 1, false]

    Explanation
    MyQueue myQueue = new MyQueue();
    myQueue.push(1); // queue is: [1]
    myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
    myQueue.peek(); // return 1
    myQueue.pop(); // return 1, queue is [2]
    myQueue.empty(); // return false

[Solution](./232.py)

## 242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:

    Input: s = "rat", t = "car"
    Output: false

[Solution](./242.py)

## 258. Add Digits
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

    Input: num = 38
    Output: 2
    Explanation: The process is
    38 --> 3 + 8 --> 11
    11 --> 1 + 1 --> 2 
    Since 2 has only one digit, return it.

Example 2:

    Input: num = 0
    Output: 0


[Solution](./258.py)

P.S.: Для решения этой задачи есть несколько подходов, но один из самых эффективных использует математическое свойство, известное как "цифровой корень" (digital root). Это свойство позволяет быстро найти результат без необходимости многократного сложения цифр.

## 263. Ugly Number
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:

    Input: n = 6
    Output: true
    Explanation: 6 = 2 × 3

Example 2:

    Input: n = 1
    Output: true
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:

    Input: n = 14
    Output: false
    Explanation: 14 is not ugly since it includes the prime factor 7.

[Solution](./263.py)

## 268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:

    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

[Solution](./268.py)

P.S.: Чтобы решить задачу нахождения пропущенного числа в массиве различных чисел в
диапазоне [0, 𝑛], можно использовать математический подход, который использует
свойства арифметической последовательности. Сумма первых 𝑛n натуральных чисел
вычисляется по формуле:

n * (n + 1) / 2

Посчитав эту сумму и вычтя сумму чисел в массиве, мы можем найти пропущенное
число.

## 283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:

    Input: nums = [0]
    Output: [0]

[Solution](./283.py)

## 278. First Bad Version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:

    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.

Example 2:

    Input: n = 1, bad = 1
    Output: 1

[Solution](./278.py)

## 290. Word Pattern
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true

Example 2:

    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false

Example 3:

    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false

[Solution](./290.py)


## 292. Nim Game
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

Example 1:

    Input: n = 4
    Output: false
    Explanation: These are the possible outcomes:

    1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
    2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
    3. You remove 3 stones. Your friend removes the last stone. Your friend wins.

    In all outcomes, your friend wins.

Example 2:

    Input: n = 1
    Output: true

Example 3:

    Input: n = 2
    Output: true

[Solution](./292.py)

P.S.: Ним — это игра в теории игр, где два игрока поочередно берут от 1 до 3 камней из кучки, и тот, кто берет последний камень, выигрывает

## 242. Valid Anagram
Given an integer array nums, handle multiple queries of the following type:

1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 
Example 1:

    Input
    ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    Output
    [null, 1, -1, -3]

    Explanation
    NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
    numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
    numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
    numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3


[Solution](./303.py)

## 326. Power of Three
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:

    Input: n = 27
    Output: true
    Explanation: 27 = 33

Example 2:

    Input: n = 0
    Output: false
    Explanation: There is no x where 3x = 0.

Example 3:

    Input: n = -1
    Output: false
    Explanation: There is no x where 3x = (-1).

[Solution](./326.py)

## 338. Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10

Example 2:

    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101

[Solution](./338.py)

## 342. Power of Four
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:

    Input: n = 16
    Output: true

Example 2:

    Input: n = 5
    Output: false

Example 3:

    Input: n = 1
    Output: true

[Solution](./342.py)

## 344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:

    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

[Solution](./344.py)

## 345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

    Input: s = "hello"
    Output: "holle"

Example 2:

    Input: s = "leetcode"
    Output: "leotcede"

[Solution](./344.py)

## 349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.

Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.

[Solution](./349.py)

## 350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]
    Explanation: [9,4] is also accepted.


[Solution](./350.py)

## 367. Valid Perfect Square
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:

    Input: num = 16
    Output: true
    Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:

    Input: num = 14
    Output: false
    Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

[Solution](./367.py)

## 374. Guess Number Higher or Lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

- -1: Your guess is higher than the number I picked (i.e. num > pick).
- 1: Your guess is lower than the number I picked (i.e. num < pick).
- 0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Example 1:

    Input: n = 10, pick = 6
    Output: 6

Example 2:

    Input: n = 1, pick = 1
    Output: 1

Example 3:

    Input: n = 2, pick = 1
    Output: 1

[Solution](./367.py)

P.S.: Решать будем с помощью бинарного поиска

## 383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:

    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:

    Input: ransomNote = "aa", magazine = "aab"
    Output: true

[Solution](./383.py)

## 387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

    Input: s = "leetcode"
    Output: 0

Example 2:

    Input: s = "loveleetcode"
    Output: 2

Example 3:

    Input: s = "aabb"
    Output: -1

[Solution](./387.py)

## 389. Find the Difference
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

Example 1:

    Input: s = "abcd", t = "abcde"
    Output: "e"
    Explanation: 'e' is the letter that was added.

Example 2:

    Input: s = "", t = "y"
    Output: "y"

[Solution](./389.py)

## 392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:

    Input: s = "axc", t = "ahbgdc"
    Output: false

[Solution](./392.py)


## 412. Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.
 
Example 1:

    Input: n = 3
    Output: ["1","2","Fizz"]

Example 2:

    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

Example 3:

    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

[Solution](./412.py)

## 414. Third Maximum Number
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:

    Input: nums = [3,2,1]
    Output: 1
    Explanation:
    The first distinct maximum is 3.
    The second distinct maximum is 2.
    The third distinct maximum is 1.

Example 2:

    Input: nums = [1,2]
    Output: 2
    Explanation:
    The first distinct maximum is 2.
    The second distinct maximum is 1.
    The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:

    Input: nums = [2,2,3,1]
    Output: 1
    Explanation:
    The first distinct maximum is 3.
    The second distinct maximum is 2 (both 2's are counted together since they have the same value).
    The third distinct maximum is 1.

[Solution](./414.py)

## 415. Third Maximum Number
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

    Input: num1 = "11", num2 = "123"
    Output: "134"

Example 2:

    Input: num1 = "456", num2 = "77"
    Output: "533"

Example 3:

    Input: num1 = "0", num2 = "0"
    Output: "0"

[Solution](./415.py)

## 434. Number of Segments in a String
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

Example 1:

    Input: s = "Hello, my name is John"
    Output: 5
    Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:

    Input: s = "Hello"
    Output: 1

[Solution](./434.py)

## 441. Arranging Coins
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:

![](./assets/arrangecoins1-grid.jpg)

    Input: n = 5
    Output: 2
    Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:

![](./assets/arrangecoins2-grid.jpg)

    Input: n = 8
    Output: 3
    Explanation: Because the 4th row is incomplete, we return 3.

[Solution](./441.py)

## 448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]

Example 2:

    Input: nums = [1,1]
    Output: [2]

[Solution](./448.py)

## 455. Assign Cookies
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Example 1:

    Input: g = [1,2,3], s = [1,1]
    Output: 1
    Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
    And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
    You need to output 1.

Example 2:

    Input: g = [1,2], s = [1,2,3]
    Output: 2
    Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
    You have 3 cookies and their sizes are big enough to gratify all of the children, 
    You need to output 2.

[Solution](./455.py)

## 459. Repeated Substring Pattern
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:

    Input: s = "abab"
    Output: true
    Explanation: It is the substring "ab" twice.

Example 2:

    Input: s = "aba"
    Output: false

Example 3:

    Input: s = "abcabcabcabc"
    Output: true
    Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

[Solution](./459.py)

## 463. Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:

![island](./assets/island.png)

    Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    Output: 16
    Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

    Input: grid = [[1]]
    Output: 4

Example 3:

    Input: grid = [[1,0]]
    Output: 4
[Solution](./463.py)

## 476. Number Complement
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:

    Input: num = 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

    Input: num = 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

[Solution](./471.py)

## 482. License Key Formatting
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Example 1:

    Input: s = "5F3Z-2e-9-w", k = 4
    Output: "5F3Z-2E9W"
    Explanation: The string s has been split into two parts, each part has 4 characters.
    Note that the two extra dashes are not needed and can be removed.

Example 2:

    Input: s = "2-5g-3-J", k = 2
    Output: "2-5G-3J"
    Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

[Solution](./482.py)

## 485. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

    Input: nums = [1,0,1,1,0,1]
    Output: 2

[Solution](./485.py)

## 492. Construct the Rectangle
A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

Example 1:

    Input: area = 4
    Output: [2,2]
    Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
    But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

Example 2:

    Input: area = 37
    Output: [37,1]

Example 3:

    Input: area = 122122
    Output: [427,286]

[Solution](./485.py)

## 495. Teemo Attacking
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

Example 1:

    Input: timeSeries = [1,4], duration = 2
    Output: 4
    Explanation: Teemo's attacks on Ashe go as follows:
    - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
    - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
    Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

Example 2:

    Input: timeSeries = [1,2], duration = 2
    Output: 3
    Explanation: Teemo's attacks on Ashe go as follows:
    - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
    - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
    Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.

[Solution](./495.py)

## 496. Next Greater Element I
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

    Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    Output: [-1,3,-1]
    Explanation: The next greater element for each value of nums1 is as follows:
    - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
    - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
    - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

    Input: nums1 = [2,4], nums2 = [1,2,3,4]
    Output: [3,-1]
    Explanation: The next greater element for each value of nums1 is as follows:
    - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
    - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

[Solution](./496.py)

## 500. Keyboard Row
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

- the first row consists of the characters "qwertyuiop",
- the second row consists of the characters "asdfghjkl", and
- the third row consists of the characters "zxcvbnm".

![](./assets/keyboard.png)

Example 1:

    Input: words = ["Hello","Alaska","Dad","Peace"]
    Output: ["Alaska","Dad"]

Example 2:

    Input: words = ["omk"]
    Output: []

Example 3:

    Input: words = ["adsdf","sfd"]
    Output: ["adsdf","sfd"]

[Solution](./500.py)

## 504. Base 7
Given an integer num, return a string of its base 7 representation.

Example 1:

    Input: num = 100
    Output: "202"

Example 2:

    Input: num = -7
    Output: "-10"

[Solution](./504.py)

## 506. Relative Ranks
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

- The 1st place athlete's rank is "Gold Medal".
- The 2nd place athlete's rank is "Silver Medal".
- The 3rd place athlete's rank is "Bronze Medal".
- For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:

    Input: score = [5,4,3,2,1]
    Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
    Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:

    Input: score = [10,3,8,9,4]
    Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
    Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

[Solution](./506.py)

## 507. Perfect Number
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:

    Input: num = 28
    Output: true
    Explanation: 28 = 1 + 2 + 4 + 7 + 14
    1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:

    Input: num = 7
    Output: false

[Solution](./507.py)

## 509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

[Solution](./509.py)


## 520. Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:

- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.

Example 1:

    Input: word = "USA"
    Output: true

Example 2:

    Input: word = "FlaG"
    Output: false

[Solution](./520.py)

## 521. Longest Uncommon Subsequence I
Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If no such uncommon subsequence exists, return -1.

An uncommon subsequence between two strings is a string that is a 
subsequence of exactly one of them.

Example 1:

    Input: a = "aba", b = "cdc"
    Output: 3
    Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
    Note that "cdc" is also a longest uncommon subsequence.

Example 2:

    Input: a = "aaa", b = "bbb"
    Output: 3
    Explanation: The longest uncommon subsequences are "aaa" and "bbb".

Example 3:

    Input: a = "aaa", b = "aaa"
    Output: -1
    Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a. So the answer would be -1.

[Solution](./521.py)

## 541. Reverse String II
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:

    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

Example 2:

    Input: s = "abcd", k = 2
    Output: "bacd"

[Solution](./541.py)

## 551. Student Attendance Record I
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

- 'A': Absent.
- 'L': Late.
- 'P': Present.

The student is eligible for an attendance award if they meet both of the following criteria:

- The student was absent ('A') for strictly fewer than 2 days total.
- The student was never late ('L') for 3 or more consecutive days.

Return true if the student is eligible for an attendance award, or false otherwise.

Example 1:

    Input: s = "PPALLP"
    Output: true
    Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

Example 2:

    Input: s = "PPALLL"
    Output: false
    Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

[Solution](./551.py)
