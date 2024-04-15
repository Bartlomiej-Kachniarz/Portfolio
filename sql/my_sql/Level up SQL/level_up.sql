-- 1. Create a list of employees and their first line managers
WITH managers_info AS (
    SELECT
        employeeId,
        firstName,
        lastName
    FROM
        employee
)
SELECT
    e.firstName AS EmployeeFirstName,
    e.lastName AS EmployeeLastName,
    mi.firstName AS ManagerFirstName,
    mi.lastName AS ManagerLastName
FROM
    managers_info mi
    RIGHT OUTER JOIN employee e ON mi.employeeId = e.managerId
ORDER BY
    mi.lastName,
    e.lastName;

-- self-join gives the same result
SELECT
    e.firstName AS EmployeeFirstName,
    e.lastName AS EmployeeLastName,
    mi.firstName AS ManagerFirstName,
    mi.lastName AS ManagerLastName
FROM
    employee mi
    INNER JOIN employee e ON mi.employeeId = e.managerId
ORDER BY
    mi.lastName,
    e.lastName;

-- 2. Create a list of sales people with 0 sales even if some data is lost
SELECT
    c.firstName,
    c.lastName,
    c.email,
    s.salesAmount,
    s.soldDate
FROM
    customer c
    INNER JOIN sales s ON c.customerId = s.customerId
UNION
-- union with customers who have no sales
SELECT
    c.firstName,
    c.lastName,
    c.email,
    s.salesAmount,
    s.soldDate
FROM
    customer c
    LEFT JOIN sales s ON c.customerId = s.customerId
WHERE
    s.salesID IS NULL
UNION
-- union with sales that have missing data
SELECT
    c.firstName,
    c.lastName,
    c.email,
    s.salesAmount,
    s.soldDate
FROM
    sales s
    LEFT JOIN customer c ON c.customerId = s.customerId
WHERE
    c.customerID IS NULL;

-- 3. How many cars have been sold per employee?
SELECT
    e.employeeID,
    e.firstName,
    e.lastName,
    COUNT(*) AS number_of_cars_sold
FROM
    employee e
    INNER JOIN sales s ON e.employeeId = s.employeeID
GROUP BY
    e.employeeID,
    e.firstName,
    e.lastName
ORDER BY
    number_of_cars_sold DESC;

-- 4. List the least and the most expensive cars sold by each employee in 2022.
SELECT
    s.employeeID,
    e.firstName,
    e.lastName,
    MIN(s.salesAmount) AS min_sales_amount,
    MAX(s.salesAmount) AS max_sales_amount
FROM
    sales s
    INNER JOIN employee e ON s.employeeId = e.employeeId
WHERE
    s.soldDate >= '2022-01-01'
    AND s.soldDate < '2022-12-31'
GROUP BY
    s.employeeID,
    e.firstName,
    e.lastName;

-- 5. List employees with more than 5 sales in 2022.
SELECT
    e.firstName,
    e.lastName,
    e.employeeId,
    count(s.salesId) AS num_of_sales
FROM
    employee e
    INNER JOIN sales s ON e.employeeId = s.employeeId
WHERE
    s.soldDate >= '2022-01-01'
    AND s.soldDate < '2022-12-31'
GROUP BY
    e.firstName,
    e.lastName,
    e.employeeId
HAVING
    num_of_sales > 5;

-- 6. Summarize sales per year
WITH sales_per_year AS (
    SELECT
        s.salesAmount AS sales_amount,
        DATE_FORMAT(s.soldDate, '%Y') AS year
    FROM
        sales s
)
SELECT
    CONCAT('$', FORMAT(sum(sales_amount), 2)) AS sales_sum,
    year
FROM
    sales_per_year
GROUP BY
    year
ORDER BY
    year;

-- 7. Show amount of sales per employee for each month of 2022
WITH sales_per_month AS (
    SELECT
        e.firstName AS name,
        e.lastName AS surname,
        s.salesAmount AS sales_amount,
        DATE_FORMAT(s.soldDate, '%M') AS month_of_sales,
        DATE_FORMAT(s.soldDate, '%m') AS month_number
    FROM
        sales s
        INNER JOIN employee e ON s.employeeId = e.employeeId
    WHERE
        s.soldDate >= '2022-01-01'
        AND s.soldDate < '2023-01-01'
)
SELECT
    name,
    surname,
    CONCAT('$', FORMAT(sum(sales_amount), 2)) AS sum_of_sales,
    month_of_sales,
    month_number
FROM
    sales_per_month
GROUP BY
    name,
    surname,
    month_of_sales,
    month_number
ORDER BY
    month_number,
    sum_of_sales DESC;

-- 8. Find all sales where the car was electric
SELECT
    s.soldDate,
    s.salesAmount,
    i.colour,
    i.year
FROM
    sales s
    INNER JOIN inventory i ON s.inventoryId = i.inventoryId
WHERE
    i.modelId IN (
        SELECT
            modelId
        FROM
            model
        WHERE
            EngineType = 'Electric');

-- 9. Show a list of salespeople and rank the car model they've sold the most
SELECT
    e.firstName,
    e.lastName,
    m.modelId,
    count(m.model) AS num_sold,
    RANK() OVER (PARTITION BY s.employeeId ORDER BY count(m.model) DESC) AS ranking
FROM
    sales s
    INNER JOIN employee e ON s.employeeId = e.employeeId
    INNER JOIN inventory i ON s.inventoryId = i.inventoryId
    INNER JOIN model m ON m.modelId = i.modelId
GROUP BY
    s.employeeId,
    m.modelId;

-- 10. Show total sales per month and an annual running total
WITH cte_sales AS (
    SELECT
        sum(s.salesAmount) AS sum_of_sales,
        DATE_FORMAT(s.soldDate, '%Y') AS year_of_sales,
        DATE_FORMAT(s.soldDate, '%m') AS month_of_sales
    FROM
        sales s
    GROUP BY
        month_of_sales,
        year_of_sales
    ORDER BY
        year_of_sales,
        month_of_sales
)
SELECT
    *,
    SUM(sum_of_sales) OVER (PARTITION BY year_of_sales ORDER BY year_of_sales, month_of_sales) AS annual_sales_running_total
    FROM
        cte_sales;

-- 11. Show the number of cars sold this month and last month
SELECT
    DATE_FORMAT(s.soldDate, '%Y-%m') AS month_of_sale,
    count(*) AS num_sold,
    LAG(count(*), 1, 0) OVER WINDOW_CAL_MONTH AS last_month_num_sold
FROM
    sales s
GROUP BY DATE_FORMAT(s.soldDate, '%Y-%m')
WINDOW WINDOW_CAL_MONTH AS (ORDER BY DATE_FORMAT(s.soldDate, '%Y-%m'))
ORDER BY
    DATE_FORMAT(s.soldDate, '%Y-%m');

