# Write your MySQL query statement below
SELECT s.student_id, s.student_name, u.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students s
JOIN Subjects u 
LEFT JOIN Examinations e ON s.student_id = e.student_id AND u.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, u.subject_name
ORDER BY s.student_id, u.subject_name ASC