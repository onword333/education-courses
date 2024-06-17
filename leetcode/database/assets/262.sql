-- 262. Trips and Users
-- 1-st variant
SELECT
  t.request_at AS Day,
  ROUND(
    AVG(
      CASE
        WHEN t.status = 'completed' THEN 0
        ELSE 1
      END
    ),
    2
  ) AS "Cancellation Rate"
FROM
  Trips t
  INNER JOIN Users u 
    ON t.client_id = u.users_id
    AND u.banned = 'No'
  INNER JOIN Users ud 
    ON t.driver_id = ud.users_id
    AND ud.banned = 'No'
WHERE
  t.request_at BETWEEN '2013-10-01'
  AND '2013-10-03'
GROUP BY
  t.request_at

-- 2-en variant
with a as (
  select
    *
  from
    Trips
  where
    Client_Id not in (
      select
        Users_Id
      from
        Users
      where
        Banned = 'Yes'
    )
    and Driver_Id not in (
      select
        Users_Id
      from
        Users
      where
        Banned = 'Yes'
    )
)
select
  Request_at as Day,
  round(
    avg(
      case
        when Status = 'completed' then 0
        else 1
      end
    ),
    2
  ) as "Cancellation Rate"
from
  a
group by
  Day
having
  Request_at between '2013-10-01'
  and '2013-10-03'

-- 3-rd variant
select
  request_at as Day,
  ROUND(
    sum(
      case
        when status not in ('completed') then 1.00
        else 0
      end
    ) / count(id),
    2
  ) "Cancellation Rate"
from
  Trips
where
  client_id not in (
    select
      users_id
    from
      Users
    where
      banned = 'Yes'
  )
  and driver_id not in (
    select
      users_id
    from
      Users
    where
      banned = 'Yes'
  )
  and request_at between '2013-10-01'
  and '2013-10-03'
group by
  request_at