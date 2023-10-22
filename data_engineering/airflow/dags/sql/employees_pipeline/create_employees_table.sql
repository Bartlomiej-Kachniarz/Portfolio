-- Creating employees table...
DROP TABLE IF EXISTS employees;
    CREATE TABLE employees (
                "Serial Number" NUMERIC PRIMARY KEY,
                "Company Name" TEXT,
                "Employee Markme" TEXT,
                "Description" TEXT,
                "Leave" INTEGER
            );