-- 181. Employees Earning More Than Their Managers
SELECT
  m.name AS Employee
FROM
  Employee e
  INNER JOIN Employee m ON e.id = m.managerId
WHERE
  m.salary > e.salary