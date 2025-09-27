SELECT
    d.dept_name,
    COUNT(e.employee_id) AS total_employees
FROM
    Departments d
LEFT JOIN
    Employees e ON d.dept_id = e.dept_id
GROUP BY
    d.dept_name
ORDER BY
    total_employees DESC;