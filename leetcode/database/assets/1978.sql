-- 1978. Employees Whose Manager Left the Company
SELECT
  employee_id
FROM
  Employees e
WHERE
  manager_id NOT IN(
    SELECT
      employee_id
    FROM
      Employees
  )
  AND salary < 30000
ORDER BY
  employee_id