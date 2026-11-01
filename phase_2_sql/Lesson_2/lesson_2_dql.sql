-- DQL using WHERE: Select all columns where department is exactly Marketing
select * from employees
where department = 'Marketing'

-- DQL using WHERE: Select only the name and salary columns where salary is more than 70000
select name, salary from employees
where salary > 70000;

-- DQL using WHERE and OR: Select all columns where department is Engineering OR salary is exactly 60000
select * from employees
where department = 'Engineering' OR salary = 60000;

-- DQL using ORDER BY, AND and DESC: Select all column where salary is greater than 65000 and department is Engineering sorted in descending order
select * from employees
where salary > 65000 and department = 'Engineering'
order by salary desc;

-- DQL using ORDER BY: Select all columns and sort the result in Ascending order
select * from employees
order by name asc;