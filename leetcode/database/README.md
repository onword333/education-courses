# Database
## 175. Combine Two Tables

Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

The result format is in the following example.

    Example 1:

    Input: 
    Person table:
    +----------+----------+-----------+
    | personId | lastName | firstName |
    +----------+----------+-----------+
    | 1        | Wang     | Allen     |
    | 2        | Alice    | Bob       |
    +----------+----------+-----------+
    Address table:
    +-----------+----------+---------------+------------+
    | addressId | personId | city          | state      |
    +-----------+----------+---------------+------------+
    | 1         | 2        | New York City | New York   |
    | 2         | 3        | Leetcode      | California |
    +-----------+----------+---------------+------------+
    Output: 
    +-----------+----------+---------------+----------+
    | firstName | lastName | city          | state    |
    +-----------+----------+---------------+----------+
    | Allen     | Wang     | Null          | Null     |
    | Bob       | Alice    | New York City | New York |
    +-----------+----------+---------------+----------+
    Explanation: 
    There is no address in the address table for the personId = 1 so we return null in their city and state.
    addressId = 1 contains information about the address of personId = 2.

[Solution](./assets/175.sql)

## 181. Employees Earning More Than Their Managers
Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

    Example 1:

    Input: 
    Employee table:
    +----+-------+--------+-----------+
    | id | name  | salary | managerId |
    +----+-------+--------+-----------+
    | 1  | Joe   | 70000  | 3         |
    | 2  | Henry | 80000  | 4         |
    | 3  | Sam   | 60000  | Null      |
    | 4  | Max   | 90000  | Null      |
    +----+-------+--------+-----------+
    Output: 
    +----------+
    | Employee |
    +----------+
    | Joe      |
    +----------+
    Explanation: Joe is the only employee who earns more than his manager.

[Solution](./assets/181.sql)

## 182. Duplicate Emails
Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.

    Example 1:

    Input: 
    Person table:
    +----+---------+
    | id | email   |
    +----+---------+
    | 1  | a@b.com |
    | 2  | c@d.com |
    | 3  | a@b.com |
    +----+---------+
    Output: 
    +---------+
    | Email   |
    +---------+
    | a@b.com |
    +---------+
    Explanation: a@b.com is repeated two times.

[Solution](./assets/182.sql)

## 197. Rising Temperature
Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.

    Example 1:

    Input: 
    Weather table:
    +----+------------+-------------+
    | id | recordDate | temperature |
    +----+------------+-------------+
    | 1  | 2015-01-01 | 10          |
    | 2  | 2015-01-02 | 25          |
    | 3  | 2015-01-03 | 20          |
    | 4  | 2015-01-04 | 30          |
    +----+------------+-------------+
    Output: 
    +----+
    | id |
    +----+
    | 2  |
    | 4  |
    +----+
    Explanation: 
    In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
    In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

[Solution](./assets/197.sql)

## 577. Employee Bonus

Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

Return the result table in any order.

The result format is in the following example.

    Example 1:

    Input: 
    Employee table:
    +-------+--------+------------+--------+
    | empId | name   | supervisor | salary |
    +-------+--------+------------+--------+
    | 3     | Brad   | null       | 4000   |
    | 1     | John   | 3          | 1000   |
    | 2     | Dan    | 3          | 2000   |
    | 4     | Thomas | 3          | 4000   |
    +-------+--------+------------+--------+
    Bonus table:
    +-------+-------+
    | empId | bonus |
    +-------+-------+
    | 2     | 500   |
    | 4     | 2000  |
    +-------+-------+
    Output: 
    +------+-------+
    | name | bonus |
    +------+-------+
    | Brad | null  |
    | John | null  |
    | Dan  | 500   |
    +------+-------+

[Solution](./assets/577.sql)

## 584. Find Customer Referee
Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The result format is in the following example.
 
    Example 1:

    Input: 
    Customer table:
    +----+------+------------+
    | id | name | referee_id |
    +----+------+------------+
    | 1  | Will | null       |
    | 2  | Jane | null       |
    | 3  | Alex | 2          |
    | 4  | Bill | null       |
    | 5  | Zack | 1          |
    | 6  | Mark | 2          |
    +----+------+------------+
    Output: 
    +------+
    | name |
    +------+
    | Will |
    | Jane |
    | Bill |
    | Zack |
    +------+

[Solution](./assets/577.sql)

## 610. Triangle Judgement
Report for every three line segments whether they can form a triangle.

Return the result table in any order.

The result format is in the following example.

    Example 1:

    Input: 
    Triangle table:
    +----+----+----+
    | x  | y  | z  |
    +----+----+----+
    | 13 | 15 | 30 |
    | 10 | 20 | 15 |
    +----+----+----+
    Output: 
    +----+----+----+----------+
    | x  | y  | z  | triangle |
    +----+----+----+----------+
    | 13 | 15 | 30 | No       |
    | 10 | 20 | 15 | Yes      |
    +----+----+----+----------+

[Solution](./assets/610.sql)

## 619. Biggest Single Number
A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null.

The result format is in the following example.

    Example 1:

    Input: 
    MyNumbers table:
    +-----+
    | num |
    +-----+
    | 8   |
    | 8   |
    | 3   |
    | 3   |
    | 1   |
    | 4   |
    | 5   |
    | 6   |
    +-----+
    Output: 
    +-----+
    | num |
    +-----+
    | 6   |
    +-----+
    Explanation: The single numbers are 1, 4, 5, and 6.
    Since 6 is the largest single number, we return it.
    Example 2:

    Input: 
    MyNumbers table:
    +-----+
    | num |
    +-----+
    | 8   |
    | 8   |
    | 7   |
    | 7   |
    | 3   |
    | 3   |
    | 3   |
    +-----+
    Output: 
    +------+
    | num  |
    +------+
    | null |
    +------+
    Explanation: There are no single numbers in the input table so we return null.

[Solution](./assets/619.sql)

## 620. Not Boring Movies
Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.

The result format is in the following example.

    Example 1:

    Input: 
    Cinema table:
    +----+------------+-------------+--------+
    | id | movie      | description | rating |
    +----+------------+-------------+--------+
    | 1  | War        | great 3D    | 8.9    |
    | 2  | Science    | fiction     | 8.5    |
    | 3  | irish      | boring      | 6.2    |
    | 4  | Ice song   | Fantacy     | 8.6    |
    | 5  | House card | Interesting | 9.1    |
    +----+------------+-------------+--------+
    Output: 
    +----+------------+-------------+--------+
    | id | movie      | description | rating |
    +----+------------+-------------+--------+
    | 5  | House card | Interesting | 9.1    |
    | 1  | War        | great 3D    | 8.9    |
    +----+------------+-------------+--------+
    Explanation: 
    We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.

[Solution](./assets/620.sql)

## 627. Swap Salary
Write a solution to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.

Note that you must write a single update statement, do not write any select statement for this problem.

The result format is in the following example.

    Example 1:

    Input: 
    Salary table:
    +----+------+-----+--------+
    | id | name | sex | salary |
    +----+------+-----+--------+
    | 1  | A    | m   | 2500   |
    | 2  | B    | f   | 1500   |
    | 3  | C    | m   | 5500   |
    | 4  | D    | f   | 500    |
    +----+------+-----+--------+
    Output: 
    +----+------+-----+--------+
    | id | name | sex | salary |
    +----+------+-----+--------+
    | 1  | A    | f   | 2500   |
    | 2  | B    | m   | 1500   |
    | 3  | C    | f   | 5500   |
    | 4  | D    | m   | 500    |
    +----+------+-----+--------+
    Explanation: 
    (1, A) and (3, C) were changed from 'm' to 'f'.
    (2, B) and (4, D) were changed from 'f' to 'm'.

[Solution](./assets/627.sql)

## 1068. Product Sales Analysis I
Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

Return the resulting table in any order.

The result format is in the following example.

    Example 1:

    Input: 
    Sales table:
    +---------+------------+------+----------+-------+
    | sale_id | product_id | year | quantity | price |
    +---------+------------+------+----------+-------+ 
    | 1       | 100        | 2008 | 10       | 5000  |
    | 2       | 100        | 2009 | 12       | 5000  |
    | 7       | 200        | 2011 | 15       | 9000  |
    +---------+------------+------+----------+-------+
    Product table:
    +------------+--------------+
    | product_id | product_name |
    +------------+--------------+
    | 100        | Nokia        |
    | 200        | Apple        |
    | 300        | Samsung      |
    +------------+--------------+
    Output: 
    +--------------+-------+-------+
    | product_name | year  | price |
    +--------------+-------+-------+
    | Nokia        | 2008  | 5000  |
    | Nokia        | 2009  | 5000  |
    | Apple        | 2011  | 9000  |
    +--------------+-------+-------+
    Explanation: 
    From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
    From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
    From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.

[Solution](./assets/1068.sql)

## 1075. Project Employees I

Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

Return the result table in any order.

The query result format is in the following example.

    Example 1:

    Input: 
    Project table:
    +-------------+-------------+
    | project_id  | employee_id |
    +-------------+-------------+
    | 1           | 1           |
    | 1           | 2           |
    | 1           | 3           |
    | 2           | 1           |
    | 2           | 4           |
    +-------------+-------------+
    Employee table:
    +-------------+--------+------------------+
    | employee_id | name   | experience_years |
    +-------------+--------+------------------+
    | 1           | Khaled | 3                |
    | 2           | Ali    | 2                |
    | 3           | John   | 1                |
    | 4           | Doe    | 2                |
    +-------------+--------+------------------+
    Output: 
    +-------------+---------------+
    | project_id  | average_years |
    +-------------+---------------+
    | 1           | 2.00          |
    | 2           | 2.50          |
    +-------------+---------------+
    Explanation: The average experience years for the first project is (3 + 2 + 1) / 3 = 2.00 and for the second project is (3 + 2) / 2 = 2.50

[Solution](./assets/1075.sql)

## 1084. Sales Analysis III
Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

Return the result table in any order.

The result format is in the following example. 

    Example 1:

    Input: 
    Product table:
    +------------+--------------+------------+
    | product_id | product_name | unit_price |
    +------------+--------------+------------+
    | 1          | S8           | 1000       |
    | 2          | G4           | 800        |
    | 3          | iPhone       | 1400       |
    +------------+--------------+------------+
    Sales table:
    +-----------+------------+----------+------------+----------+-------+
    | seller_id | product_id | buyer_id | sale_date  | quantity | price |
    +-----------+------------+----------+------------+----------+-------+
    | 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
    | 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
    | 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
    | 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
    +-----------+------------+----------+------------+----------+-------+
    Output: 
    +-------------+--------------+
    | product_id  | product_name |
    +-------------+--------------+
    | 1           | S8           |
    +-------------+--------------+
    Explanation: 
    The product with id 1 was only sold in the spring of 2019.
    The product with id 2 was sold in the spring of 2019 but was also sold after the spring of 2019.
    The product with id 3 was sold after spring 2019.
    We return only product 1 as it is the product that was only sold in the spring of 2019.

[Solution](./assets/1084.sql)

## 1141. User Activity for the Past 30 Days I
Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

Return the result table in any order.

The result format is in the following example.

    Example 1:

    Input: 
    Activity table:
    +---------+------------+---------------+---------------+
    | user_id | session_id | activity_date | activity_type |
    +---------+------------+---------------+---------------+
    | 1       | 1          | 2019-07-20    | open_session  |
    | 1       | 1          | 2019-07-20    | scroll_down   |
    | 1       | 1          | 2019-07-20    | end_session   |
    | 2       | 4          | 2019-07-20    | open_session  |
    | 2       | 4          | 2019-07-21    | send_message  |
    | 2       | 4          | 2019-07-21    | end_session   |
    | 3       | 2          | 2019-07-21    | open_session  |
    | 3       | 2          | 2019-07-21    | send_message  |
    | 3       | 2          | 2019-07-21    | end_session   |
    | 4       | 3          | 2019-06-25    | open_session  |
    | 4       | 3          | 2019-06-25    | end_session   |
    +---------+------------+---------------+---------------+
    Output: 
    +------------+--------------+ 
    | day        | active_users |
    +------------+--------------+ 
    | 2019-07-20 | 2            |
    | 2019-07-21 | 2            |
    +------------+--------------+ 
    Explanation: Note that we do not care about days with zero active users.

<span style="color:red">Задание не корректно составлено, говорится, что "Note that we do not care about days with zero active users", но при этом правильноый ответ ожидает все записи и те кто ничего не сделал</span>

[Solution](./assets/1141.sql)

## 1179. Reformat Department Table
Reformat the table such that there is a department id column and a revenue column for each month.

Return the result table in any order.

The result format is in the following example.

    Example 1:

    Input: 
    Department table:
    +------+---------+-------+
    | id   | revenue | month |
    +------+---------+-------+
    | 1    | 8000    | Jan   |
    | 2    | 9000    | Jan   |
    | 3    | 10000   | Feb   |
    | 1    | 7000    | Feb   |
    | 1    | 6000    | Mar   |
    +------+---------+-------+
    Output: 
    +------+-------------+-------------+-------------+-----+-------------+
    | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
    +------+-------------+-------------+-------------+-----+-------------+
    | 1    | 8000        | 7000        | 6000        | ... | null        |
    | 2    | 9000        | null        | null        | ... | null        |
    | 3    | null        | 10000       | null        | ... | null        |
    +------+-------------+-------------+-------------+-----+-------------+
    Explanation: The revenue from Apr to Dec is null.
    Note that the result table has 13 columns (1 for the department id + 12 for the months).

[Solution](./assets/1179.sql)

## 1211. Queries Quality and Percentage
Table: Queries

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | query_name  | varchar |
    | result      | varchar |
    | position    | int     |
    | rating      | int     |
    +-------------+---------+
    This table may have duplicate rows.
    This table contains information collected from some queries on a database.
    The position column has a value from 1 to 500.
    The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
 

We define query quality as:

    The average of the ratio between query rating and its position.

We also define poor query percentage as:

    The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and poor_query_percentage.

Both quality and poor_query_percentage should be rounded to 2 decimal places.

Return the result table in any order.

The result format is in the following example.

    Example 1:

    Input: 
    Queries table:
    +------------+-------------------+----------+--------+
    | query_name | result            | position | rating |
    +------------+-------------------+----------+--------+
    | Dog        | Golden Retriever  | 1        | 5      |
    | Dog        | German Shepherd   | 2        | 5      |
    | Dog        | Mule              | 200      | 1      |
    | Cat        | Shirazi           | 5        | 2      |
    | Cat        | Siamese           | 3        | 3      |
    | Cat        | Sphynx            | 7        | 4      |
    +------------+-------------------+----------+--------+
    Output: 
    +------------+---------+-----------------------+
    | query_name | quality | poor_query_percentage |
    +------------+---------+-----------------------+
    | Dog        | 2.50    | 33.33                 |
    | Cat        | 0.66    | 33.33                 |
    +------------+---------+-----------------------+
    Explanation: 
    Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
    Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

    Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
    Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33

[Solution](./assets/1211.sql)