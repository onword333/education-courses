"""551. Student Attendance Record I"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        # 'A': Absent.
        # 'L': Late.
        # 'P': Present.

        if s.count('A') < 2 and 'LLL' not in s:
            return True        

        return False

s = 'LALL'

print(Solution().checkRecord(s))