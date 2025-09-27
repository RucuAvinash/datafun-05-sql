--Give all Employess a 5 % raise where salary <100000
UPDATE employees
SET salary = salary * 1.05
WHERE salary <= 100000;

--Changes the location in Department table from Atlanta to St-Louis where department name is 'IT-Services'
UPDATE departments
SET location = 'St-Louis'
WHERE dept_name = 'IT Services';
