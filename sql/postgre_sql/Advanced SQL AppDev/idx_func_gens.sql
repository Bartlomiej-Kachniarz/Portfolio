-- CREATE INDEX idx_first_last ON customers USING tree(first_name, last_name);
-- CREATE INDEX idx_product_name ON products USING HASH (product_name);
-- Generating series
WITH sensors_datetimes AS (
    SELECT
        *
    FROM (
        SELECT
            *
        FROM
            generate_series(1, 100)) AS t1,
(
        SELECT
            *
        FROM
            generate_series('2021-01-01 00:00'::timestamp, '2021-02-15'::timestamp, '1 days')) AS t2
)
SELECT
    sd.*,
    floor(random() * 30) AS temperature,
    floor(random() * 80 + random() * 20) AS humidity
FROM
    sensors_datetimes sd;

CREATE TABLE iot_sensors AS (
    WITH sensors_ids AS (
    SELECT
        i
    FROM
        generate_series(1, 100
) AS i
)
        SELECT
            i AS id,
            'Sensor ' || i::text AS sensor_name
        FROM
            sensors_ids
);

EXPLAIN
SELECT
    *
FROM
    iot_sensors AS s
    RIGHT JOIN orders AS o ON o.order_id = s.id;

-- CREATING FUNCTIONS
CREATE OR REPLACE FUNCTION harmonic_mean(x numeric, y numeric)
    RETURNS numeric
    AS $$
    SELECT
        ROUND(((2 * x * y) /(x + y))::numeric, 2)
$$
LANGUAGE sql;

-- Checking if that function works:
SELECT
    harmonic_mean(2, 7);

-- Overloading functions
CREATE OR REPLACE FUNCTION harmonic_mean(x text, y text)
    RETURNS numeric
    AS $$
    SELECT
        ROUND(((2 * x::numeric * y::numeric) /(x::numeric + y::numeric))::numeric, 2)
$$
LANGUAGE sql;

-- Does it work? yeap it does!
SELECT
    harmonic_mean(2, 7),
    harmonic_mean('2', '7');

-- CREATE EXTENSION plpython3u; in my case works on another postgreSQL installation port 5433
CREATE OR REPLACE FUNCTION isPalindrome(x text)
    RETURNS boolean
    AS $$
    SELECT
(REVERSE(x) = x)
$$
LANGUAGE SQL
IMMUTABLE;

SELECT
    isPalindrome('kajaka'),
    isPalindrome('kajak');

-- key-value pairs
CREATE EXTENSION hstore;

CREATE TABLE books(
    id serial PRIMARY KEY,
    title text,
    attributes hstore
);

INSERT INTO books(title, attributes)
    VALUES ('SQL for Data Science', 'language=>English, page_cnt=>500, pub_year=>2022');

INSERT INTO books(title, attributes)
    VALUES ('SQL for Data Science 2', 'language=>English, page_cnt=>600, pub_year=>2023');

SELECT
    *
FROM
    books;

SELECT
    title,
    attributes -> 'pub_year' AS pub_year
FROM
    books
WHERE
    attributes -> 'page_cnt' = '500';

-- JSON
CREATE TABLE customer_summary(
    id serial PRIMARY KEY,
    customer_doc jsonb
);

INSERT INTO customer_summary(customer_doc)
    VALUES ('{
        "customer_name":
            {
                "first_name":"Alice", 
                "last_name":"Johnson"
                },
        "address":
            {
                "street":"5432 Port Ave", 
                "city":"Boston", 
                "state":"MA"
                },
        "purchase_history":
            {
                "annual_purchase_value":[100, 200, 300], 
                "lifetime_value":1500
                }
        }');

SELECT
    customer_doc -> 'customer_name' ->> 'first_name'
FROM
    customer_summary;

CREATE EXTENSION ltree;

-- LTREEs
CREATE TABLE paths_to_nodes(
    id serial PRIMARY KEY,
    node text,
    path ltree
);

CREATE INDEX idx_path_to_nodes ON paths_to_nodes USING gist(path);

INSERT INTO paths_to_nodes(node, path)
    VALUES ('A', 'A');

INSERT INTO paths_to_nodes(node, path)
    VALUES ('B', 'A.B');

INSERT INTO paths_to_nodes(node, path)
    VALUES ('C', 'A.C');

INSERT INTO paths_to_nodes(node, path)
    VALUES ('D', 'A.B.D');

INSERT INTO paths_to_nodes(node, path)
    VALUES ('E', 'A.B.E');

INSERT INTO paths_to_nodes(node, path)
    VALUES ('F', 'A.C.F');

INSERT INTO paths_to_nodes(node, path)
    VALUES ('G', 'A.C.G');

INSERT INTO paths_to_nodes(node, path)
    VALUES ('H', 'A.B.D.H');

INSERT INTO paths_to_nodes(node, path)
    VALUES ('I', 'A.B.D.I');

INSERT INTO paths_to_nodes(node, path)
    VALUES ('J', 'A.B.D.J');

INSERT INTO paths_to_nodes(node, path)
    VALUES ('K', 'A.C.F.K');

SELECT
    *
FROM
    paths_to_nodes;

SELECT
    *
FROM
    paths_to_nodes
WHERE
    'A.B' @> path;

-- Show only those nodes that have B in the middle
SELECT
    *
FROM
    paths_to_nodes
WHERE
    '*.B.*{1}' ~ path;

WITH paths_to_follow AS (
    SELECT
        *
    FROM
        paths_to_nodes p2
    WHERE
        path ~ '*.C.*'
)
SELECT
    p1.id,
    p1.node,
    p1.path,
    p1.path || p2.path -- returns ltree
FROM
    paths_to_nodes p1,
    paths_to_follow p2
WHERE
    p1.path ~ '*.B.*';

