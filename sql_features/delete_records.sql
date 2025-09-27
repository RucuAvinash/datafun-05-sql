-- Remove all employess with the Legal Department
DELETE FROM employees
WHERE dept_id = 8;

---Remove the Legal Department
DELETE FROM departments
WHERE dept_id = 8;
