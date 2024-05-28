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

[Solution](./assets/algorithms/121.py)

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
 

[Solution](./assets/algorithms/125.py)