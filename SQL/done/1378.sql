-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

-- Write your PostgreSQL query statement below
SELECT unique_id, name
FROM Employees e LEFT JOIN EmployeeUNI ei
    ON e.id = ei.id