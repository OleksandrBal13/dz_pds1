use pds;
select * from employees order by FIRST_NAME;
select FIRST_NAME,LAST_NAME,SALARY,SALARY*0.15 from employees;
select sum(SALARY) from employees;
select max(salary),min(salary) from employees;
select avg(SALARY), count(EMPLOYEE_ID) from employees;