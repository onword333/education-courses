-- 1661. Average Time of Process per Machine
-- 1-st variant
SELECT
  t1.machine_id,
  ROUND((SUM(t1.end) - SUM(t1.start)) :: NUMERIC / max(t1.proc_count),
  3
) AS processing_time
FROM
  (
    SELECT
      machine_id,
      process_id,
      SUM(timestamp) FILTER(
        WHERE
          activity_type = 'start'
      ) AS start,
      SUM(timestamp) FILTER(
        WHERE
          activity_type = 'end'
      ) AS
  end,
  COUNT(process_id) OVER(PARTITION BY machine_id) AS proc_count
FROM
  Activity a
GROUP BY
  machine_id,
  process_id
) t1
GROUP BY
  t1.machine_id 1


-- 2-end variant
SELECT
  m1.machine_id,
  ROUND(AVG(m2.timestamp - m1.timestamp) :: NUMERIC, 3) AS processing_time
FROM
  Activity m1
  JOIN Activity m2 ON m1.machine_id = m2.machine_id
  AND m1.process_id = m2.process_id
  AND m1.activity_type = 'start'
  AND m2.activity_type = 'end'
GROUP BY
  (m1.machine_id)
