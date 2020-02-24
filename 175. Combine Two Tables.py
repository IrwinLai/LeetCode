# Write your MySQL query statement below
SELECT 
    FirstName,
    LastName,
    City,
    State
    FROM Person p LEFT OUTER JOIN Address a
    ON p.personid = a.personid;