use pds;
#1
select count(EMPLOYEE_ID) from employees;
#2 
select avg(SALARY), count(EMPLOYEE_ID) from employees where DEPARTMENT_ID = 90;
#3
select jobs.JOB_TITLE, count(employees.EMPLOYEE_ID) from employees left join jobs on employees.JOB_ID = jobs.JOB_ID group by employees.JOB_ID;
#4 
select employees.FIRST_NAME, employees.LAST_NAME, employees.DEPARTMENT_ID, departments.DEPARTMENT_NAME from employees left join departments on employees.DEPARTMENT_ID = departments.DEPARTMENT_ID;
#5
select employees.FIRST_NAME, employees.LAST_NAME, jobs.JOB_TITLE, departments.DEPARTMENT_ID from employees 
left join jobs on employees.JOB_ID = jobs.JOB_ID
left join departments on employees.DEPARTMENT_ID = departments.DEPARTMENT_ID
left join locations on departments.LOCATION_ID = locations.LOCATION_ID where CITY = "London";
