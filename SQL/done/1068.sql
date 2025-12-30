-- https://leetcode.com/problems/product-sales-analysis-i/

-- Write your PostgreSQL query statement below
SELECT product_name, year, price
FROM Product p JOIN Sales s
    ON p.product_id = s.product_id