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