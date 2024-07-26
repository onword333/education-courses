"""500. Keyboard Row"""


class Solution:
    def find_words(self, words):
        keybord = [
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm'
        ]

        res = []

        for word in words:
            word_lower = word.lower()
            for val in keybord:
                is_find = True  # отслеживает найдено ли слово
                for ch in range(len(word)):
                    if word_lower[ch] not in val:
                        # символы слова находятся в разных
                        # строках клавиатуры, прерываем цикл
                        is_find = False
                        break

                if is_find:
                    # все символы находятся в определенной 
                    # строке клавиатуры, дальше не ищем
                    res.append(word)
                    break


        return res

    def find_words_2(self, words):
        keybord = [
            set('qwertyuiop'),
            set('asdfghjkl'),
            set('zxcvbnm')
        ]

        res = []

        for word in words:
            word_set = set(word.lower())

            for row in keybord:
                if word_set.issubset(row):
                    res.append(word)

        return res
    
#words = ["Hello", "Alaska", "Dad", "Peace"]
#words = ["a", "b"]
words = ["abdfs","cccd","a","qwwewm"]



print(Solution().find_words(words))
print(Solution().find_words_2(words))
