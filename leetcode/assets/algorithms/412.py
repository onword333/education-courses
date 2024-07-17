"""412. Fizz Buzz"""


class Solution:

    def fizz_buzz(self, num: int) -> str:
        ans = []

        for i in range(1, num + 1):

            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(i)

        return ans



obj = Solution()

for n in [3, 5, 15]:
    print(obj.fizz_buzz(n))
