-- https://leetcode.com/problems/combine-two-tables/

-- Write your PostgreSQL query statement below
SELECT firstName, lastName, city, state
FROM Person p LEFT JOIN Address a
    ON a.personId = p.personId;