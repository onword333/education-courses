"""495. Teemo Attacking"""

class Solution:
    def find_poisoned_duration(self, timeSeries, duration: int) -> int:        
        total = 0
        for t in range(len(timeSeries) - 1):
            
            if timeSeries[t + 1] - timeSeries[t] >= duration:
                total += duration
            else:
                total += timeSeries[t + 1] - timeSeries[t]


        return total+duration
    
    def find_poisoned_duration_2(self, timeSeries, duration: int) -> int:
        total = 0

        for t in range(len(timeSeries) - 1):
            total += min(timeSeries[t + 1] - timeSeries[t], duration)

        return total+duration
    
    def find_poisoned_duration_3(self, timeSeries, duration: int) -> int:
        if not timeSeries:
            return 0
        # общее время отравления
        total_poisoned_time = 0

        # отслеживает конец текущего интервала отравления
        end_time = 0

        for time in timeSeries:
            if time >= end_time:
                total_poisoned_time += duration
            else:
                total_poisoned_time += time + duration - end_time
            end_time = time + duration

        return total_poisoned_time


duration = 2

print(Solution().find_poisoned_duration([1,4], duration))
print(Solution().find_poisoned_duration([1,2], duration))

print(Solution().find_poisoned_duration_2([1,4], duration))
print(Solution().find_poisoned_duration_2([1,2], duration))

print(Solution().find_poisoned_duration_3([1,4], duration))
print(Solution().find_poisoned_duration_3([1,2], duration))
