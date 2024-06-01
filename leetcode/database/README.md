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