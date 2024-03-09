# 30 days of pandas

## 196. Delete Duplicate Emails
```python
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', ascending=True, inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)
```

## 1795. Rearrange Products Table
```python
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
  res = products.melt(
    id_vars=["product_id"], 
    var_name="store", 
    value_name="price").dropna()  
  return res
```

## 1907. Count Salary Categories
```python
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
  return pd.DataFrame({
    'category': ['Low Salary', 'Average Salary', 'High Salary'],
    'accounts_count': [
      accounts[accounts.income < 20000].shape[0],
      accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0],
      accounts[accounts.income > 50000].shape[0],
    ]
  })
```

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

## 1050. Actors and Directors Who Cooperated At Least 

```python
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
  df = actor_director
  df['_count'] = 1
  pivot = df.pivot_table(
      values='_count', 
      index=['actor_id', 'director_id'], 
      aggfunc={'_count': 'sum'}
    ).reset_index()
  return pivot.query('_count >= 3')[['actor_id', 'director_id']]
```

## 1378. Replace Employee ID With The Unique Identifier

```python
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
  df_merge = employees.merge(employee_uni, how='left', on='id')\
    .drop(columns=['id'])    
  return df_merge
```

## 1280. Students and Examinations
```python
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
  examinations.rename(columns={'subject_name': 'attended_exams'}, inplace=True)    

  exam = students.merge(subjects, how='cross')\
    .merge(
      examinations, 
      how='left', 
      left_on=['student_id', 'subject_name'], 
      right_on=['student_id', 'attended_exams']
    )    

  pivot = exam\
    .groupby(
      ['student_id', 'student_name', 'subject_name'], 
      as_index=False, 
      dropna=False)\
    .agg({'attended_exams': 'count'})
  
  if 'attended_exams' not in pivot.columns:
    pivot['attended_exams'] = np.nan
  return pivot
```

## 570. Managers with at Least 5 Direct Reports
```python
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
  count_employee = employee\
    .groupby(['managerId'], as_index=False)\
    .agg(count_emp=('id', 'count'))    

  min_5_empl = count_employee.query('count_emp > 4')['managerId']    
  return employee.query('id in @min_5_empl')[['name']]
```

## 607. Sales Person
```python
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
  merged = pd.merge(orders, company, on='com_id')
  result = sales_person[
    ~sales_person['sales_id']\
        .isin(
            merged[merged['name'] == 'RED']['sales_id']
        )
    ]
  
  return result[['name']]
```