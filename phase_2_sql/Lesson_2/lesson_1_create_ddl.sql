-- DDL using CREATE: Creating a table called employees
create table employees (
	id integer primary key,
	name varchar(100),
	department varchar(50),
	salary integer
);

-- DML using INSERT: Inserting values into the newly created table
insert into employees (id, name, department, salary)
values (1, 'John Doe', 'Engineering', 75000),
       (2, 'Jane Smith', 'Marketing', 65000),
	   (3, 'Michael Johnson', 'Engineering', 80000),
	   (4, 'Emily Davis', 'HR', 60000),
	   (5, 'Michael Brown', 'Marketing', 60000);

-- DQL using SELECT:  Selecting all columns
select * from employees;

-- DML using UPDATE: Updating a data in a column called salary
update employees set salary = 68000 where id = 5;