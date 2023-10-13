# Write your MySQL query statement below
# SELECT machine_id, COUNT(DISTINCT process_id) AS num 
# FROM Activity
# GROUP BY machine_id; 
# SELECT machine_id, AVG(end_time - start_time) AS processing_time
# FROM (
#     SELECT machine_id, process_id, activity_type,
#            MAX(CASE WHEN activity_type = "start" THEN timestamp END) AS start_time,
#            MAX(CASE WHEN activity_type = "end" THEN timestamp END) AS end_time
#     FROM Activity
#     WHERE activity_type IN ('start', 'end')
#     GROUP BY machine_id, process_id
# ) AS subquery
# GROUP BY machine_id, process_id;
SELECT a1.machine_id, round(AVG(a2.timestamp - a1.timestamp), 3) as processing_time
FROM Activity a1
JOIN Activity a2
ON a1.machine_id = a2.machine_id and a1.process_id = a2.process_id
and a1.activity_type='start' and a2.activity_type = "end"
GROUP BY a1.machine_id;
