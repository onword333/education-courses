# 30 days of pandas
1741. Find Total Time Spent by Each Employee

```python
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
  employees['total_time'] = employees['out_time'] - employees['in_time']
  res = employees[['event_day', 'emp_id', 'total_time']]\
    .groupby(['event_day', 'emp_id'], as_index=False).sum()\
    .sort_values(by='total_time', ascending=False)\
    .rename(columns={'event_day': 'day'})
  return res
```