-- 1075. Project Employees I
SELECT
  project_id,
  ROUND(AVG(experience_years) :: NUMERIC, 2) AS average_years
FROM
  Project p
  LEFT JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY
  project_id