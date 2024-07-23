"""482. License Key Formatting"""


class Solution:
    def license_key_formatting(self, s: str, k: int) -> str:

        i = 0
        res = []
        for ch in s[::-1]:
            if ch == '-':
                continue

            if i % k == 0 and i != 0:
                res.append('-')
                res.append(ch.upper())
                i = 0
            else:
                res.append(ch.upper())
            
            i += 1                    
        return ''.join(res)[::-1]
    
    def license_key_formatting_2(self, s: str, k: int):
        res = []

        #  очистим строку от "-"
        s = s.replace('-', '').upper()

        # определим длину 1-ой группы
        head = len(s) % k

        if head:
            res.append(s[:head])

        # проходим с шагом k и добавляем в список
        for i in range(head, len(s), k):
            res.append(s[i : i + k])

        return '-'.join(res)

s1 = '5F3Z-2e-9-w'
s2 = '2-5g-3-J'
k1 = 4
k2 = 2

print(Solution().license_key_formatting(s1, k1))
print(Solution().license_key_formatting_2(s2, k2))