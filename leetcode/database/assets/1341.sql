-- 1341. Movie Rating
(
  SELECT
    u.name :: varchar AS results,    
  FROM
    MovieRating m
    LEFT JOIN Users u ON m.user_id = u.user_id
  GROUP BY
    m.user_id,
    u.name
  ORDER BY
    COUNT(m.rating) DESC,
    u.name
  LIMIT
    1
)
UNION ALL
  (
    SELECT
      m.title :: varchar AS results,      
    FROM
      MovieRating mr
      LEFT JOIN Movies m ON mr.movie_id = m.movie_id
    WHERE
      mr.created_at BETWEEN '2020-02-01'
      AND '2020-02-29'
    GROUP BY
      mr.movie_id,
      m.title
    ORDER BY
      AVG(mr.rating) DESC,
      m.title
    LIMIT
      1
  )