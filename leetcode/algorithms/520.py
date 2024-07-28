"""520. Detect Capital"""


class Solution:
    def detect_capital_use(self, word: str) -> bool:

        if word.isupper():
            return True

        if word.islower():
            return True

        if word[0].isupper and word[1:].islower():
            return True

        return False

    def detect_capital_use_2(self, word: str):
        return word.isupper() or word.islower() or word.istitle()

word = 'USA'
word = 'FlaG'

print(Solution().detect_capital_use(word))
print(Solution().detect_capital_use_2(word))