CREATE TABLE employees (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,
    salary INTEGER,
    department TEXT
);

INSERT INTO employees (name, salary, department) VALUES
  ('Alice', 50000, 'marketing'),
  ('Bob', 60000, 'marketing'),
  ('Charlie', 55000, 'marketing'),
  ('David', 65000, 'marketing'),
  ('Eve', 70000, 'finance'),
  ('Frank', 52000, 'finance'),
  ('Grace', 58000, 'finance'),
  ('Hank', 62000, 'finance');
-- Do not modify above this line. --

SELECT e.name, e.salary
FROM employees e
INNER JOIN (
    SELECT department, AVG(salary) AS avg_salary 
    FROM employees 
    GROUP BY department
    ) AS marketing_dept_avg_salary
ON e.department = marketing_dept_avg_salary.department
WHERE e.department = 'marketing'
AND e.salary < marketing_dept_avg_salary.avg_salary
ORDER BY e.salary ASC;




