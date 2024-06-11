-- 602. Friend Requests II: Who Has the Most Friends
SELECT
  id,
  COUNT(id) AS num
FROM
  (
    SELECT
      accepter_id AS id
    FROM
      RequestAccepted
    UNION ALL
    SELECT
      requester_id AS id
    FROM
      RequestAccepted
  ) t1
GROUP BY
  id
ORDER BY
  num DESC
LIMIT
  1
