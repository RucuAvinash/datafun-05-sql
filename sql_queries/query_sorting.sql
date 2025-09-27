SELECT * FROM employees e
JOIN departments d
ON  d.dept_id = e.dept_id
WHERE d.dept_name = 'Finance' 
ORDER BY e.first_name DESC;

