-- 182. Duplicate Emails
SELECT
  email
FROM 
  Person p
GROUP BY 
  email
HAVING COUNT(email) > 1