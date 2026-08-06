# Write your MySQL query statement 
SELECT D.NAME AS DEPARTMENT, E.NAME AS EMPLOYEE , E.SALARY 
FROM EMPLOYEE E
LEFT JOIN DEPARTMENT D ON
    E.DEPARTMENTID = D.ID
WHERE (e.DepartmentId, e.Salary) IN (
    SELECT DepartmentId, MAX(Salary)
    FROM Employee
    GROUP BY DepartmentId
);


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna