-- 1731. The Number of Employees Which Report to Each Employee
SELECT
  e.employee_id,
  e.name,
  COUNT(r.reports_to) AS reports_count,
  ROUND(AVG(r.age), 0) AS average_age
FROM Employees e
INNER JOIN Employees r ON e.employee_id = r.reports_to 
GROUP BY
  e.employee_id,
  e.name
ORDER BY
  e.employee_id