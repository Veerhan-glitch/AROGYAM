SELECT userid,   
      name, MAX(last_active) AS last_active
FROM (
  SELECT u.userid, u.name, MAX(n.datetime)::date AS last_active
  FROM users u, notifications n WHERE u.userid = n.userid
  AND n.datetime >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 year')
  AND n.datetime < CURRENT_DATE  GROUP BY u.userid, u.name
  UNION
  SELECT u.userid, u.name, MAX(o.date) AS last_active
  FROM users u, orders o WHERE u.userid = o.userid
  AND o.date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 year')
  AND o.date < CURRENT_DATE  GROUP BY u.userid, u.name) AS recent_activity
GROUP BY userid, name
ORDER BY last_active DESC;