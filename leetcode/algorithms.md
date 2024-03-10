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