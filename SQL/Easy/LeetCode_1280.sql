-- student_id is the primary key (column with unique values) for this table.
-- Each row of this table contains the ID and the name of one student in the school.


-- subject_name is the primary key (column with unique values) for this table.
-- Each row of this table contains the name of one subject in the school.


-- There is no primary key (column with unique values) for this table. It may contain duplicates.
-- Each student from the Students table takes every course from the Subjects table.
-- Each row of this table indicates that a student with ID student_id attended the exam of subject_name.


-- Write a solution to find the number of times each student attended each exam.

-- Return the result table ordered by student_id and subject_name.


SELECT
    st.student_id,
    st.student_name,
    sub.subject_name,
    COUNT(ex.student_id) AS attended_exams
FROM Students st
CROSS JOIN Subjects sub
LEFT JOIN Examinations ex
ON st.student_id = ex.student_id
AND ex.subject_name = sub.subject_name
GROUP BY st.student_id, st.student_name, sub.subject_name
ORDER BY st.student_id, sub.subject_name