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