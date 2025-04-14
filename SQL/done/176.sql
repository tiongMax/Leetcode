https://leetcode.com/problems/second-highest-salary/description/

-- Write your PostgreSQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);