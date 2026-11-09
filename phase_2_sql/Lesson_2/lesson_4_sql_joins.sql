CREATE TABLE departments (
    dept_id integer primary key,
    dept_name varchar(100),
    location varchar(100)
);

insert into departments (dept_id, dept_name, location)
values (1, 'Engineering', 'Building A'),
       (2, 'Marketing', 'Building B'),
	   (3, 'HR', 'Building C');

-- Using INNER JOIN to return rows where values match in both tables
SELECT e.name, d.location
from employees e
INNER JOIN departments d
ON e.department = d.dept_name
where location = 'Building A';