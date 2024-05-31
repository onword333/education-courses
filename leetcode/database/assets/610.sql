-- 610. Triangle Judgement
-- 1 variant
SELECT
  x,
  y,
  z,
  CASE
    WHEN x + y > z
    AND x + z > y
    AND y + z > x THEN 'Yes'
    ELSE 'No'
  END AS triangle
FROM
  triangle;

-- 2 variant
SELECT
  X,
  Y,
  Z,
  IF(
    X + Y > Z
    AND Y + Z > X
    AND Z + X > Y,
    'Yes',
    'No'
  ) as triangle
FROM
  Triangle