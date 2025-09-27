INSERT INTO departments (dept_id, dept_name, location) VALUES
(1, 'Sales', 'New York'),
(2, 'Engineering', 'San Francisco'),
(3, 'Human Resources', 'Chicago'),
(4, 'Marketing', 'Los Angeles'),
(5, 'Finance', 'Boston'),
(6, 'Research & Development', 'Seattle'),
(7, 'Customer Support', 'Dallas'),
(8, 'Legal', 'Washington D.C.'),
(9, 'Operations', 'Houston'),
(10, 'IT Services', 'Atlanta');

INSERT INTO employees (employee_id, first_name, last_name, salary, dept_id) VALUES
(1001, 'Alice', 'Johnson', 75000.00, 1),   -- Sales
(1002, 'Bob', 'Smith', 120000.00, 2),     -- Engineering
(1003, 'Charlie', 'Brown', 60000.00, 3),  -- Human Resources
(1004, 'Diana', 'Prince', 80000.00, 1),   -- Sales (Another one in Dept 1)
(1005, 'Evan', 'Wright', 135000.00, 2),   -- Engineering (Another one in Dept 2)
(1006, 'Fiona', 'Chen', 92000.00, 4),     -- Marketing
(1007, 'George', 'Lopez', 150000.00, 5),  -- Finance
(1008, 'Hannah', 'Kim', 110000.00, 6),    -- R&D
(1009, 'Isaac', 'Davis', 55000.00, 7),    -- Customer Support
(1010, 'Jasmine', 'Reid', 180000.00, 8),  -- Legal
(1011, 'Kevin', 'Miller', 70000.00, 9),   -- Operations
(1012, 'Laura', 'Gomez', 95000.00, 10),   -- IT Services
(1013, 'Mark', 'Wilson', 93000.00, 4),    -- Marketing (Another one in Dept 4)
(1014, 'Nancy', 'Hall', 65000.00, 7),     -- Customer Support (Another one in Dept 7)
(1015, 'Oscar', 'Lee', 140000.00, 2),    -- Engineering (Third one in Dept 2)
(1016, 'Loren','Morgan',39000.00, 8),    -- Legal
(1018, 'Ashley','Elder', 45000.00,8),   -- Legal
(1019, 'Tina','Tripp', 80000.00,8);       -- Legal