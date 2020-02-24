# Write your MySQL query statement below
SELECT 
    d.name as Department, e.name as Employee, e.Salary
    FROM 
        employee e, 
        department d,
        (SELECT departmentid as d, MAX(salary) as s 
            FROM employee
            GROUP BY d) m
    WHERE e.departmentid = m.d
    AND e.salary = m.s
    AND e.departmentid = d.id;