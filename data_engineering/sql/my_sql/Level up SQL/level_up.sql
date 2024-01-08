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

-- 2. Create a list of sales people with 0 sales
