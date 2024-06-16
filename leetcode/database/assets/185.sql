-- 185. Department Top Three Salaries
-- 1-st variant
WITH top_salary AS (
  SELECT
    departmentId,
    salary,
    ROW_NUMBER() OVER(
      PARTITION BY departmentId
      ORDER BY
        salary DESC
    ) rnk
  FROM
    (
      SELECT
        departmentId,
        salary
      FROM
        Employee
      GROUP BY
        departmentId,
        salary
    ) t1
)
SELECT
  d.name AS Department,
  e.name AS Employee,
  ts.salary
FROM
  top_salary ts
  INNER JOIN Employee e ON ts.salary = e.salary
    AND ts.rnk <= 3
    AND ts.departmentId = e.departmentId
  LEFT JOIN Department d ON ts.departmentId = d.id

-- 2-end variant
WITH top_3_salaries AS (
  SELECT
    departmentId,
    id,
    name,
    salary,
    DENSE_RANK() OVER(
      PARTITION BY departmentId
      ORDER BY
        salary DESC
    ) AS rnk
  FROM
    Employee
  GROUP BY
    id,
    name,
    departmentId,
    salary
)
SELECT
  d.name AS Department,
  t.name AS Employee,
  salary
FROM
  top_3_salaries t
  JOIN Department d ON t.departmentId = d.id
WHERE
  rnk <= 3