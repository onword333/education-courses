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