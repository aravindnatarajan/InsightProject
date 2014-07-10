
Facebook: How many people are using the product?

SQL session:

Table logs
user_id      Time
   1          t1 
   2          t2 
   3          t3 
   4          t4   

How many users logged in today, but not yesterday?
select A.user_id from logs a left outer join logs b on b.user_id=a.user_id and a.time = today() and b.user_id is NULL and b.time = yesterday()



"where" : filters out the data after you do the join.
"and": first do the filtering, then join.
Aggregates:  count, sum, max,min,avg
Use GROUP BY when using aggregates


SELECT
  CASE
    WHEN age < cutoff THEN "young"
    ELSE "old"
  END AS age_grp
  COUNT(*)
FROM content
GROUP BY 1
  



what the join does:

      a
user      time



2 kinds of join:
join
and left outer join (When you find data that is in table but not in another)

recurrent users, churn, etc.




