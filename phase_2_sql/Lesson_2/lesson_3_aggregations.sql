-- Finding total salary of employees
select sum(salary) as total_salary
from employees

select min(salary) as least_salary
from employees


select department, count(*) as num_employees
from employees
GROUP BY department
HAVING avg(salary) > 65000;