# Write your MySQL query statement below
select emp2.unique_id,emp1.name
From Employees as emp1
left join EmployeeUNI as emp2
    on emp1.id=emp2.id