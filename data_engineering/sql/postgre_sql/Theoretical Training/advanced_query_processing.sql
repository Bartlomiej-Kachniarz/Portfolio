-- Query Tuning DB
EXPLAIN ANALYZE
SELECT
    last_name
FROM
    staff;

--
EXPLAIN ANALYZE
SELECT
    *
FROM
    staff
WHERE
    salary > 75000;

-- INDEXES
CREATE INDEX idx_staff_salary ON staff(salary);

--
EXPLAIN
SELECT
    *
FROM
    staff
WHERE
    salary > 150000;

-- Sequence scan all table
EXPLAIN
SELECT
    *
FROM
    staff
WHERE
    email = 'bphillips5@time.com';

--
CREATE INDEX idx_staff_email ON staff(email);

-- Now it does index scan which is much faster
EXPLAIN
SELECT
    *
FROM
    staff
WHERE
    email = 'bphillips5@time.com';

--
DROP INDEX idx_staff_email;

-- BITMAP index is creating on the fly in PostgreSQL
SELECT DISTINCT
    job_title
FROM
    staff
ORDER BY
    job_title;

-- Without index this is a sequence scan:
EXPLAIN
SELECT
    *
FROM
    staff
WHERE
    job_title = 'Operator';

--
CREATE INDEX idx_staff_job_title ON staff(job_title);

-- Now it is a Bitmap Heap Scan:
EXPLAIN
SELECT
    *
FROM
    staff
WHERE
    job_title = 'Operator';

-- Hash index
CREATE INDEX idx_staff_email ON staff USING HASH (email);

-- 8.02 computational units (CU)
EXPLAIN
SELECT
    *
FROM
    staff
WHERE
    email = 'bphillips5@time.com';

--
DROP INDEX idx_staff_email;

-- b-tree index
CREATE INDEX idx_staff_email ON staff(email);

-- 8.29 CU
EXPLAIN
SELECT
    *
FROM
    staff
WHERE
    email = 'bphillips5@time.com';

--
DROP INDEX idx_staff_email;

-- BLOOM FILTER index adding to PostgreSQL:
-- This is a probabilistic index
CREATE EXTENSION IF NOT EXISTS bloom;


/*
PostgreSQL native indexes:
- GiST
- Generalized Search Tree
- Framework for implementing custom indexes

SP-GiST
- Space-partitioned GiST
- Useful for skewed distributions and unbalanced data
- Partitions can have different sizes\

GIN
- Used for text indexing
- Lookups are faster than GiST but builds are slower
- indexes 2 to 3 times bigger than GiST

BRIN
- Block range indexing for large dataset
i.e. binning data like age 65+



JOINS
Nested Loops:
+ Works with all conditions
+ Low overhead
+ Work well with small datasets
- can be slow
- tables should fit in memory
- indexes can improve performance 
 */
-- Example:
-- this command by default runs Hash Join
EXPLAIN
SELECT
    s.id,
    s.last_name,
    s.job_title,
    cr.country
FROM
    staff AS s
    INNER JOIN company_regions AS cr ON cr.region_id = s.region_id;

-- How to force nested loops joining?:
-- Run this whole block of code from HERE...
SET enable_nestloop = TRUE;

SET enable_hashjoin = FALSE;

SET enable_mergejoin = FALSE;

EXPLAIN
SELECT
    s.id,
    s.last_name,
    s.job_title,
    cr.country
FROM
    staff AS s
    INNER JOIN company_regions AS cr ON cr.region_id = s.region_id;

-- ... TO HERE
/*


HASH joins
1. build hash table:
1.1 use smaller table
1.2 compute and store the hash value in the table

2. probe phase
2.1 step through larger table
2.2 compute hash value
2.3 compare with values in hash table

- only equality can be checked
- time is based on table size:
rows in smaller table for build;
and rows in larger table for probe table;
+ provides fast lookup
 */
-- Hash join example:
SET enable_nestloop = FALSE;

SET enable_hashjoin = TRUE;

SET enable_mergejoin = FALSE;

EXPLAIN
SELECT
    s.id,
    s.last_name,
    s.job_title,
    cr.country
FROM
    staff AS s
    INNER JOIN company_regions AS cr ON cr.region_id = s.region_id;


/*
MERGE JOINS
- equality only
- time based on table size: time to sort and time to scan 
+ works well with data not-fitting in the memory
+ produces output in sorted order 
 */
SET enable_nestloop = FALSE;

SET enable_hashjoin = FALSE;

SET enable_mergejoin = TRUE;

EXPLAIN
SELECT
    s.id,
    s.last_name,
    s.job_title,
    cr.country
FROM
    staff AS s
    INNER JOIN company_regions AS cr ON cr.region_id = s.region_id;

-- Partitioning by RANGE
CREATE TABLE iot_measurements(
    location_id int NOT NULL,
    measurement_datetime timestamp NOT NULL,
    temp_celsius int,
    rel_humidity_pct int
)
PARTITION BY RANGE (measurement_datetime);

CREATE TABLE iot_measurements_wk3_2024 PARTITION OF iot_measurements
FOR VALUES FROM ('2024-01-15') TO ('2024-01-22');

-- Partition by LIST
CREATE TABLE products(
    location_id int NOT NULL,
    measurement_datetime timestamp NOT NULL,
    temp_celsius int,
    rel_humidity_pct int,
    prod_category text
)
PARTITION BY LIST (prod_category);

CREATE TABLE products_cloth PARTITION OF products
FOR VALUES IN ('casual', 'business', 'formal');

-- Partition by HASH
--
--
--
/*
Materialized views
- duplicate data
- there are some inconsistencies
- they are not being updated on their own
+ good if speed is more important than storage
 */
CREATE MATERIALIZED VIEW mv_staff AS
SELECT
    s.last_name,
    s.department,
    s.job_title,
    cr.company_regions
FROM
    staff AS s
    INNER JOIN company_regions AS cr ON cr.region_id = s.region_id;

-- REFRESHING MATERIALIZED VIEW
REFRESH MATERIALIZED VIEW mv_staff;

-- Potentially use triggers for refreshing views.
