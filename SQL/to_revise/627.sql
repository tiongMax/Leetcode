-- https://leetcode.com/problems/swap-sex-of-employees/submissions/1868314606/

-- Write your PostgreSQL query statement below
UPDATE salary
SET sex =
    CASE
        WHEN sex = 'm' THEN 'f'
        ELSE 'm'
    END;