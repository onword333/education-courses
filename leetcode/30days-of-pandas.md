# 30 days of pandas
## 1741. Find Total Time Spent by Each Employee

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

## 511. Game Play Analysis I

```python
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
  res = activity[['player_id', 'event_date']]\
    .sort_values(by='event_date', ascending=True)\
    .groupby(['player_id'], as_index=False)\
    .first()\
    .rename(columns={'event_date': 'first_login'})
  return res
```

## 2356. Number of Unique Subjects Taught by Each Teacher

```python
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher[['teacher_id', 'subject_id']]\
      .groupby(['teacher_id'], as_index=False)\
      .nunique()\
      .rename(columns={'subject_id':'cnt'})
```

## 596. Classes More Than 5 Students

```python
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    res = courses.groupby(['class'], as_index=False)\
        .nunique()        

    return res[res['student'] > 4][['class']]
```

## 586. Customer Placing the Largest Number of Orders

```python
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    res = orders\
      .groupby(['customer_number'], as_index=False)\
      .nunique()\
      .sort_values(by='order_number', ascending=False)
    
    return res[0:1][['customer_number']]
```

## 1484. Group Sold Products By The Date

```python
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
  df = activities.groupby('sell_date')['product']\
    .agg([
        ('num_sold', 'nunique'),
        ('product', lambda x: ','.join(sorted(set(x))))            
    ])\
    .reset_index()\
    .rename(columns={'product': 'products'})
  return df
```

## 1693. Daily Leads and Partners
```python
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
  res = daily_sales.groupby(['date_id', 'make_name'], as_index=False)\
    .agg(
      unique_leads = ('lead_id', 'nunique'),
      unique_partners = ('partner_id', 'nunique')
    )
  return res
```