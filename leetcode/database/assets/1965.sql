-- 1965. Employees With Missing Information
SELECT
  COALESCE(e.employee_id, s.employee_id) AS employee_id
FROM
  Employees e FULL
  JOIN Salaries s ON e.employee_id = s.employee_id
WHERE
  e.employee_id IS NULL
  OR s.employee_id IS NULL