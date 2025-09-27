SELECT 'Highest Paid' AS type, first_name, last_name, salary
FROM Employees
WHERE salary = (SELECT MAX(salary) FROM Employees)
UNION ALL
SELECT 'Lowest Paid' AS type, first_name, last_name, salary
FROM Employees
WHERE salary = (SELECT MIN(salary) FROM Employees);

