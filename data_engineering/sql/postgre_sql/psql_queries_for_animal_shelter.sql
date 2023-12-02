SELECT
        *,
        'SQL is FUN' AS Fact
FROM
        Staff;

SELECT
        *
FROM
        staff
        INNER JOIN staff_roles ON 1 = 1;

SELECT
        A.name,
        AD.adopter_email,
        A.implant_chip_id,
        A.breed,
        A.admission_date
FROM
        animals AS A
        LEFT OUTER JOIN adoptions AS AD ON A.name = AD.name
        AND A.species = AD.species;

SELECT
        *
FROM
        animals AS A
        LEFT OUTER JOIN adoptions AS AD
INNER JOIN persons AS P ON P.email = AD.adopter_email ON A.name = AD.name
        AND A.species = AD.species;

SELECT
        *
FROM
        adoptions AS AD
        INNER JOIN persons AS P ON P.email = AD.adopter_email
        RIGHT OUTER JOIN animals AS A ON AD.name = A.name
                AND AD.species = A.species;

SELECT
        A.name,
        A.species,
        A.primary_color,
        A.breed,
        V.vaccination_time,
        V.vaccine,
        P.first_name,
        P.last_name,
        SA.email,
        SA.role
FROM
        animals AS A
        LEFT OUTER JOIN persons AS P
INNER JOIN vaccinations AS V
INNER JOIN staff_assignments AS SA ON V.email = SA.email ON P.email = V.email ON A.name = V.name
        AND A.species = V.species
ORDER BY
        A.name,
        A.species,
        A.breed,
        P.first_name;

SELECT
        *
FROM
        animals AS A
WHERE
        A.species = 'Dog'
        AND A.breed <> 'Bullmastiff';

SELECT
        *
FROM
        animals
WHERE
        breed = 'Bullmastiff'
        OR breed IS NULL;

SELECT
        *
FROM
        animals AS A
WHERE
        breed IS DISTINCT FROM 'Bullmastiff';

SELECT
        *
FROM
        animals A
WHERE (breed = 'Bullmastiff') IS NOT TRUE;

SELECT
        species,
        COUNT(*) AS COUNT,
        MAX(NAME) AS NAME
FROM
        adoptions
GROUP BY
        species;

SELECT
        v.name,
        species,
        COUNT(*) AS COUNT
FROM
        vaccinations AS v
GROUP BY
        v.name,
        species;

SELECT
        species,
        breed,
        COUNT(*) AS number_of_animals
FROM
        animals
GROUP BY
        species,
        breed;

SELECT
        DATE_PART('YEAR', p.birth_date) AS Year_Born,
        COUNT(*) AS Number_of_persons
FROM
        persons AS P
GROUP BY
        DATE_PART('YEAR', p.birth_date);

SELECT
        DATE_PART('YEAR', NOW()) - DATE_PART('YEAR', p.birth_date) AS age,
        COUNT(*) AS number_of_persons
FROM
        persons AS P
GROUP BY
        DATE_PART('YEAR', p.birth_date);

SELECT
        V.species,
        V.name
FROM
        vaccinations AS V
GROUP BY
        V.species,
        V.name;

SELECT DISTINCT
        V.species,
        COUNT(*) AS num_vaccines
FROM
        vaccinations AS V
GROUP BY
        V.species,
        v.name
ORDER BY
        species,
        num_vaccines;

SELECT
        adopter_email,
        COUNT(*) AS number_of_adoptions
FROM
        adoptions
WHERE
        adopter_email NOT LIKE '%gmail.com'
GROUP BY
        adopter_email
HAVING
        COUNT(*) > 1
ORDER BY
        number_of_adoptions DESC;

SELECT
        A.name,
        A.species,
        MAX(A.primary_color) AS primary_color,
        -- Dummy             aggregate
        MAX(A.breed) AS breed,
        -- Dummy aggregate
        COUNT(V.vaccine) AS number_of_vaccinations
FROM
        animals AS A
        LEFT OUTER JOIN vaccinations AS V ON A.name = V.name
        AND A.species = V.species
WHERE
        V.vaccine IS DISTINCT FROM 'Rabies'
        AND A.species <> 'Rabbit'
GROUP BY
        A.name,
        A.species
HAVING
        MAX(V.vaccination_time) < '2019-10-01'
        OR MAX(V.vaccination_time) IS NULL
ORDER BY
        number_of_vaccinations DESC;

SELECT
        *
FROM
        animals
ORDER BY
        breed NULLS LAST,
        species,
        NAME;

-- don't use columns numbering!
SELECT DISTINCT
        adoption_date,
        species,
        NAME
FROM
        adoptions
ORDER BY
        adoption_date DESC;

SELECT
        *
FROM
        animals AS A
ORDER BY
        A.admission_date DESC
LIMIT 3 OFFSET 0;

SELECT
        MAX(A.adoption_fee)
FROM
        adoptions AS A;

SELECT
        *,
(((
                SELECT
                        MAX(A.adoption_fee)
                FROM adoptions AS A) - A.adoption_fee) * 100 /(
        SELECT
                MAX(A.adoption_fee)
        FROM adoptions AS A))
FROM
        adoptions AS A;

SELECT
        A1.species,
(
                SELECT
                        MAX(adoption_fee)
                FROM
                        adoptions AS A2
                WHERE
                        A2.species = A1.species) AS max_fee
FROM
        adoptions AS A1
GROUP BY
        A1.species;

SELECT
        COUNT(*)
FROM
        persons;

SELECT DISTINCT
        P.*
FROM
        persons AS P
        INNER JOIN adoptions AS A ON A.adopter_email = P.email;

SELECT
        *
FROM
        persons AS P
WHERE
        P.email IN (
                SELECT
                        A.adopter_email
                FROM
                        adoptions AS A);

-- Who adopted some animals?
SELECT
        *
FROM
        persons AS P
WHERE
        EXISTS (
                SELECT
                        NULL
                FROM
                        adoptions AS A -- it's always better to use aliases
                WHERE
                        A.adopter_email = P.email);

SELECT
        ALL * -- ALL / DISTINCT
        -- ALL is default
FROM
        adoptions;

-- Which animals where not adopted?
SELECT DISTINCT
        AN.name,
        AN.species
FROM
        animals AS AN
        LEFT OUTER JOIN adoptions AS AD ON AD.name = AN.name
        AND AD.species = AN.species
WHERE
        AD.name IS NULL;

-- or another solution
SELECT
        AN.name,
        AN.species,
        AN.breed
FROM
        animals AS AN
WHERE
        NOT EXISTS (
                SELECT
                        NULL
                FROM
                        adoptions AS AD
                WHERE
                        AD.name = AN.name
                        AND AD.species = AN.species);

-- Using SET OPERATORS:
SELECT
        NAME,
        species
FROM
        animals
EXCEPT
SELECT
        NAME,
        species
FROM
        adoptions;

-- Which breeds where never adopted?
SELECT
        species,
        breed
FROM
        animals
EXCEPT
SELECT
        AN.species,
        AN.breed
FROM
        animals AS AN
WHERE
        EXISTS (
                SELECT
                        NULL
                FROM
                        adoptions AS AD
                WHERE
                        AD.name = AN.name
                        AND AD.species = AN.species);

-- Another way:
SELECT
        species,
        breed
FROM
        animals
EXCEPT
SELECT
        A.species,
        A.breed
FROM
        animals AS A
        INNER JOIN adoptions AS AD ON A.name = Ad.name
                AND A.species = AD.species;

-- Without using set operators:
SELECT DISTINCT
        AN1.species,
        AN1.breed
FROM
        animals AS AN1
WHERE (AN1.Species, AN1.Breed)
NOT IN (
        SELECT
                AN2.Species,
                AN2.Breed
        FROM
                Animals AS AN2
                INNER JOIN Adoptions AS AD ON AD.name = AN2.name
                        AND AD.species = AN2.species
        WHERE
                AN2.breed IS NOT NULL);

-- OR:
SELECT DISTINCT
        A.species,
        A.breed
FROM
        animals AS A
WHERE
        NOT EXISTS (
                SELECT
                        NULL
                FROM
                        animals AS AN
                WHERE
                        EXISTS (
                                SELECT
                                        NULL
                                FROM
                                        adoptions AS AD
                                WHERE
                                        AD.name = AN.name
                                        AND AD.species = AN.species
                                        AND AD.species = A.species
                                        AND A.breed IS NOT DISTINCT FROM AN.breed));

-- ...this eliminates NULLs.
-- Adopters who adopted 2 animals on 1 day?
SELECT
        A1.adopter_email,
        A1.adoption_date,
        A1.name AS Name1,
        A1.species AS Species1,
        A2.name AS Name2,
        A2.species AS Species2
FROM
        adoptions AS A1
        INNER JOIN adoptions AS A2 ON A1.adopter_email = A2.adopter_email
                AND A1.adoption_date = A2.adoption_date
                AND ((A1.name = A2.name
                                AND A1.species > A2.species)
                        OR (A1.name > A2.name
                                AND A1.species = A2.species)
                        OR (A1.name <> A2.name
                                AND A1.species > A2.species))
        ORDER BY
                A1.adopter_email,
                A1.adoption_date;

-- Show all animals with their most recent vaccinations:
SELECT
        A.name,
        A.species,
        A.primary_color,
        A.breed,
        last_vaccinations.*
FROM
        animals AS A
        CROSS JOIN LATERAL (
                SELECT
                        V.vaccine,
                        V.vaccination_time
                FROM
                        vaccinations AS V
                WHERE
                        V.name = A.name
                        AND V.species = A.species
                ORDER BY
                        V.vaccination_time DESC
                LIMIT 3 OFFSET 0) AS last_vaccinations;

-- But how to include not vaccinated animals?
SELECT
        A.name,
        A.species,
        A.primary_color,
        A.breed,
        last_vaccinations.*
FROM
        animals AS A
        LEFT OUTER JOIN LATERAL (
        SELECT
                V.vaccine,
                V.vaccination_time
        FROM
                vaccinations AS V
        WHERE
                V.name = A.name
                AND V.species = A.species
        ORDER BY
                V.vaccination_time DESC
        LIMIT 3 OFFSET 0) AS last_vaccinations ON TRUE;

-- Matching breeds animals:
SELECT
        A.name,
        A.species,
        A.breed,
        A.gender,
        PB.*
FROM
        animals AS A
        INNER JOIN LATERAL (
                SELECT
                        A2.gender,
                        A2.name,
                        A2.species,
                        A2.breed
                FROM
                        animals AS A2
                WHERE
                        A.breed = A2.breed
                        AND A.name <> A2.name
                        AND A.gender > A2.gender) AS PB ON TRUE;

-- another solution:
SELECT
        A.species,
        A.name,
        A.breed,
        A.gender,
        A2.gender,
        A2.name,
        A2.breed
FROM
        animals AS A
        INNER JOIN animals AS A2 ON A.breed = A2.breed
                AND A.species = A2.species
                AND A.name <> A2.name
                AND A.gender > A2.gender;

-- Group adoptions by date and filter to have more than one adoption
SELECT
        a.adoption_date,
        SUM(a.adoption_fee) AS total_fee,
        STRING_AGG(CONCAT(a.name, ' the ', a.species), ', ') AS adopted_animals
FROM
        adoptions AS a
GROUP BY
        adoption_date
HAVING
        COUNT(*) > 1;

-- Rank animals based on no of vaccinations
SELECT
        NAME,
        species,
        COUNT(*) AS number_of_vaccinations
FROM
        vaccinations
GROUP BY
        NAME,
        species
ORDER BY
        species,
        number_of_vaccinations DESC;

-- Statistical analysis functions
-- What would be the rank of an hypothetical animal that recieved X vaccinations?
WITH vaccinations_ranking AS (
        SELECT
                NAME,
                species,
                COUNT(*) AS num_v
        FROM
                vaccinations
        GROUP BY
                NAME,
                species
)
SELECT
        species,
        MAX(num_v) AS max_v,
        MIN(num_v) AS min_v,
        CAST(AVG(num_v) AS DECIMAL(9, 2)) AS avg_v,
        -- The cast function reduces number of digits after point
        DENSE_RANK(5) WITHIN GROUP (ORDER BY num_v DESC) AS how_would_5_rank,
        CAST(PERCENT_RANK(5) WITHIN GROUP (ORDER BY num_v DESC) AS DECIMAL(9, 2)) AS top_percentage_5_would_have,
        PERCENTILE_CONT(0.3333) WITHIN GROUP (ORDER BY num_v DESC) AS inverse_continuous, -- interpolated values
        PERCENTILE_DISC(0.3333) WITHIN GROUP (ORDER BY num_v DESC) AS inverse_discrete -- picks an existing value higher than the interpolated one
        -- but only within the existing group values
FROM
        vaccinations_ranking
GROUP BY
        species;

-- Show the number of annual, monthly and overall adoptions=
SELECT
        -- Monthly:
        DATE_PART('YEAR', adoption_date) AS in_year,
        DATE_PART('MONTH', adoption_date) AS in_month,
        COUNT(*) AS monthly_adptns
FROM
        adoptions
GROUP BY
        in_year,
        in_month
UNION ALL
SELECT
        -- Annual
        DATE_PART('YEAR', adoption_date) AS in_year,
        NULL AS in_month,
        COUNT(*) AS adptns_yearly
FROM
        adoptions
GROUP BY
        in_year
UNION ALL
SELECT
        -- Overall
        NULL AS in_year,
        NULL AS in_month,
        COUNT(*) AS total_adptns
FROM
        adoptions
GROUP BY
        ();

-- The same but using with clause
WITH in_month AS (
        SELECT
                DATE_PART('YEAR', adoption_date) AS in_year,
                DATE_PART('MONTH', adoption_date) AS in_month,
                COUNT(*) AS monthly_adptns
        FROM
                adoptions
        GROUP BY
                DATE_PART('YEAR', adoption_date),
                DATE_PART('MONTH', adoption_date))
SELECT
        *
FROM
        in_month
UNION ALL
SELECT
        in_year,
        NULL,
        COUNT(*)
FROM
        in_month
GROUP BY
        in_year
UNION ALL
SELECT
        NULL,
        NULL,
        COUNT(*)
FROM
        in_month
GROUP BY
        ();

-- Grouping sets
SELECT
        -- Monthly:
        DATE_PART('YEAR', adoption_date) AS in_year,
        DATE_PART('MONTH', adoption_date) AS in_month,
        COUNT(*) AS monthly_adptns
FROM
        adoptions
GROUP BY
        GROUPING SETS (in_year,
                in_month) -- this should be with double parentheses: GROUPING SETS (in_year, in_month)
UNION ALL
SELECT
        -- Annual
        DATE_PART('YEAR', adoption_date) AS in_year,
        NULL AS in_month,
        COUNT(*) AS adptns_yearly
FROM
        adoptions
GROUP BY
        GROUPING SETS (in_year)
UNION ALL
SELECT
        -- Overall
        NULL AS in_year,
        NULL AS in_month,
        COUNT(*) AS total_adptns
FROM
        adoptions
GROUP BY
        GROUPING SETS (());

-- GROUP BY clause is the same as one GROUPING SET
SELECT
        -- Monthly:
        DATE_PART('YEAR', adoption_date) AS in_year,
        DATE_PART('MONTH', adoption_date) AS in_month,
        COUNT(*) AS monthly_adptns
FROM
        adoptions
GROUP BY
        GROUPING SETS ((in_year,
                        in_month),
                in_year,
())
ORDER BY
        in_year,
        in_month;

-- Annual number of adoptions and adoptions per email
SELECT
        -- Monthly:
        DATE_PART('YEAR', adoption_date) AS in_year,
        adopter_email,
        COUNT(*) AS monthly_adptns
FROM
        adoptions
GROUP BY
        GROUPING SETS (in_year,
                adopter_email)
ORDER BY
        adopter_email;

-- How to distinguish between two records: one for all species and all breeds
-- and another for those animals with NULLs in both species and breed?
SELECT
        CASE WHEN GROUPING (species) = 1 THEN
                'All'
        ELSE
                species
        END AS species,
        CASE WHEN GROUPING (breed) = 1 THEN
                'All'
        ELSE
                breed
        END AS breed,
        count(*) AS no_of_animals
FROM
        animals
GROUP BY
        GROUPING SETS (species,
                breed,
());

-- Count the number of vaccinations per year, staff, staff & species,
-- species, species & year. Give latest vaccination year for each group.
SELECT
        -- CASE WHEN COALESCE(CAST(DATE_PART('YEAR', V.vaccination_time) AS VARCHAR(10)), 'all years') IS NULL THEN
        --         'all'
        -- ELSE
        --         CAST(DATE_PART('YEAR', V.vaccination_time) AS VARCHAR(10))
        -- END AS in_year,
        COALESCE(CAST(DATE_PART('YEAR', V.vaccination_time) AS VARCHAR(10)), 'all years') AS in_year,
        CASE WHEN GROUPING (species) = 1 THEN
                'all species'
        ELSE
                species
        END AS species,
        CASE WHEN GROUPING (V.email) = 1 THEN
                'all staff'
        ELSE
                MAX(CONCAT(P.first_name || ' ' || P.last_name))
        END AS name,
        COUNT(*) AS num_of_v,
        DATE_PART('YEAR', MAX(V.vaccination_time)) AS last_v
FROM
        vaccinations AS V
        INNER JOIN persons AS P ON P.email = V.email
GROUP BY
        GROUPING SETS ((),
        in_year,
        V.email,
        species,
(in_year,
                species),
(V.email,
                species))
ORDER BY
        in_year,
        species,
        V.email;

-- Recursion
SELECT
        CAST(DAY AS date) AS day
FROM
        GENERATE_SERIES('2019-01-01'::date, -- Start::Type
                '2019-12-31', '1 DAY') AS days_of_2019(day)
ORDER BY
        day ASC;

-- Another way of recursion
WITH RECURSIVE days_of_2019(
        day
) AS (
        SELECT
                CAST('20190101' AS date)
        UNION ALL
        SELECT
                -- DATEADD(DAY, 1, day) -- SQL Server
                CAST(day + interval '1 DAY' AS date)
        FROM
                days_of_2019
        WHERE
                day < CAST('20191231' AS date))
SELECT
        *
FROM
        days_of_2019
ORDER BY
        day ASC;

-- WINDOW FUNCTIONS tutorial
-- Query 1 ...
SELECT
        species,
        name,
        primary_color,
        admission_date,
(
                SELECT
                        count(*)
                FROM
                        animals
                WHERE
                        admission_date >= '2017-01-01')
FROM
        animals
WHERE
        admission_date >= '2017-01-01'
ORDER BY
        admission_date ASC;

-- ... is equivalent to:
SELECT
        species,
        name,
        primary_color,
        admission_date,
        COUNT(*) OVER () AS number_of_animals
FROM
        animals
WHERE
        admission_date >= '2017-01-01'
ORDER BY
        admission_date ASC;

-- Count number of animals of the same species
SELECT
        species,
        name,
        primary_color,
        admission_date,
        COUNT(*) OVER (PARTITION BY species) AS number_of_animals
FROM
        animals
WHERE
        admission_date >= '2017-01-01'
ORDER BY
        species,
        admission_date;

-- Cumulative number of animals of the same species that were in the shelter before the current one
SELECT
        species,
        name,
        primary_color,
        admission_date,
        COUNT(*) OVER (PARTITION BY species ORDER BY admission_date ASC RANGE BETWEEN UNBOUNDED PRECEDING AND '1 day' PRECEDING) AS running_sum_number_of_animals
FROM
        animals
ORDER BY
        species,
        admission_date;

-- Return animal's species, name, checkup time, heart rate, and whether their heart rate was always higher than average of their species.
-- This is only partially accurate since it is not showing every checkup:
WITH avg_hr AS (
        SELECT
                species,
                CAST(AVG(heart_rate) AS Decimal(9, 2)) AS avg_hr_species
        FROM
                routine_checkups
        GROUP BY
                species
)
SELECT
        R.name,
        R.species,
        MAX(R.checkup_time) AS last_checkup_time,
        MIN(R.heart_rate) AS min_heart_rate,
        MIN(avg_hr_species) AS avg_hr_species,
        CASE WHEN MIN(R.heart_rate) > MIN(avg_hr_species) THEN
                TRUE
        ELSE
                FALSE
        END AS at_risk
FROM
        avg_hr
        JOIN routine_checkups AS R ON avg_hr.species = R.species
GROUP BY
        GROUPING SETS (R.name,
                R.species)
ORDER BY
        R.name,
        R.species;

-- Full solution
-- Using aggregate window functions:
WITH avg_routine_checkups AS (
        SELECT
                R.name,
                R.species,
                R.checkup_time,
                R.heart_rate,
                AVG(R.heart_rate) OVER (PARTITION BY species) AS avg_per_species
        FROM
                routine_checkups AS R
)
SELECT
        *,
        EVERY(heart_rate >= avg_per_species) OVER (PARTITION BY species, name) AS at_risk
        FROM
                avg_routine_checkups
        ORDER BY
                name ASC,
                species ASC,
                checkup_time ASC;

-- How many non-null names in species groups?
SELECT
        species,
        COUNT(*) AS group_,
        SUM(COUNT(name)) OVER () AS window_
FROM
        animals
GROUP BY
        species;

-- Show year, month, monthly revenue, and monthly revenue as percent of current year
WITH monthly_grouped_adoptions AS (
        SELECT
                DATE_PART('YEAR', adoption_date) AS year_,
                DATE_PART('MONTH', adoption_date) AS month_,
                SUM(adoption_fee) AS monthly_sum
        FROM
                adoptions
        GROUP BY
                DATE_PART('YEAR', adoption_date),
                DATE_PART('MONTH', adoption_date))
SELECT
        *,
        CAST(100 * monthly_sum / SUM(monthly_sum) OVER (PARTITION BY year_) AS DECIMAL(5, 2)) AS annual_percent
FROM
        monthly_grouped_adoptions
ORDER BY
        year_,
        month_;

-- Show all years when animals were vaccinated and total of vaccinations, add average of 2 prior years, add percent difference between current year and the calculated 2-year average
WITH total_per_year AS (
        SELECT
                DATE_PART('YEAR', vaccination_time) AS year_,
                count(*) AS total_v
        FROM
                vaccinations
        GROUP BY
                year_
        ORDER BY
                year_
)
SELECT
        year_,
        total_v,
        CAST(AVG(total_v) OVER (ORDER BY year_ ASC RANGE BETWEEN 2 PRECEDING AND 1 PRECEDING) AS DECIMAL(5, 1)) AS avg_2y_before,
        CAST(100 *(total_v) / AVG(total_v) OVER (ORDER BY year_ ASC RANGE BETWEEN 2 PRECEDING AND 1 PRECEDING) AS decimal(5, 2)) AS percent_diff
FROM
        total_per_year
GROUP BY
        year_,
        total_v
ORDER BY
        year_;

SELECT
        MIN(MAX(admission_date)) OVER ()
FROM
        animals
GROUP BY
        species;

-- Show top 3 animals who had the most checkups including species with less than 3 animals
SELECT
        S.species,
        RC.name,
        COUNT(RC.checkup_time) AS num_of_checkups
FROM
        reference.species AS S
        LEFT OUTER JOIN routine_checkups AS RC ON S.species = RC.species
GROUP BY
        S.species,
        name
ORDER BY
        S.species ASC,
        num_of_checkups DESC;

-- ranks
WITH all_ranks AS (
        SELECT
                species,
                name,
                COUNT(*) AS num_of_checkups,
                ROW_NUMBER() OVER W AS row_number,
                        RANK() OVER W AS rank,
                                DENSE_RANK() OVER W AS dense_rank
                                FROM
                                        routine_checkups
                                GROUP BY species,
                                name
WINDOW W AS (PARTITION BY species ORDER BY COUNT(*) DESC))
SELECT
        *
FROM
        all_ranks
WHERE
        dense_rank <= 3
ORDER BY
        species ASC,
        num_of_checkups DESC;

-- Distribution window functions
WITH avg_weights AS (
        SELECT
                species,
                name,
                CAST(AVG(weight) AS DECIMAL(9, 2)) AS avg_weight
        FROM
                routine_checkups
        GROUP BY
                species,
                name
)
SELECT
        *,
        PERCENT_RANK() OVER W AS percent_rank,
        CUME_DIST() OVER W AS cume_dist
FROM
        avg_weights
WINDOW W AS (PARTITION BY species ORDER BY avg_weight)
ORDER BY
        species DESC,
        avg_weight DESC;

-- Show top 25% of animals per species that had
-- the fewest temperature anomalities. Ignore those with no checkups.
-- An temp anomaly is by +/-0.5% off in comparison to species' average.
-- If 2 or more have the same number of temp anomalies,
-- return those with most recent checkups.
-- No need to show those after top 25% mark.
-- If the number of animals does not divide by 4 with no remainder,
-- 1 more animal can be returned, not 1 less.
WITH avg_per_species AS (
        SELECT
                S.species,
                CAST(AVG(RC.temperature) AS DECIMAL(5, 2)) AS species_avg
        FROM
                routine_checkups AS RC
                JOIN reference.species S ON S.species = RC.species
        GROUP BY
                S.species
),
prcnt_diff AS (
        SELECT
                R.species,
                R.name,
                R.temperature,
                species_avg,
                CAST(100 *(R.temperature - species_avg) / species_avg AS DECIMAL(5, 2)) AS percent_diff
        FROM
                avg_per_species APS
                INNER JOIN routine_checkups R ON R.species = APS.species
),
anomalities AS (
        SELECT
                *,
                CASE WHEN ABS(percent_diff) > 0.5 THEN
                        1
                END AS is_anormal
        FROM
                prcnt_diff
),
no_of_anomalities AS (
        SELECT
                species,
                name,
                COUNT(is_anormal) AS no_of_anomalities
FROM
        anomalities
GROUP BY
        species,
        name
)
SELECT
        *,
        CAST(PERCENT_RANK() OVER W2 AS DECIMAL(4, 3)) AS percent_rank,
        CAST(CUME_DIST() OVER W2 AS DECIMAL(4, 3)) AS cume_dist,
        RANK() OVER W2 AS rank,
        DENSE_RANK() OVER W2 AS dense_rank
FROM
        no_of_anomalities
WINDOW W2 AS (PARTITION BY species ORDER BY no_of_anomalities ASC)
ORDER BY
        species,
        dense_rank;

-- solution:
WITH checkups AS (
        SELECT
                species,
                name,
                temperature,
                checkup_time,
                CAST(AVG(temperature) OVER (PARTITION BY species) AS decimal(5, 2)) AS species_avg_temp,
                CAST(temperature - AVG(temperature) OVER (PARTITION BY species) AS decimal(5, 2)) AS diff_from_avg
        FROM
                routine_checkups
),
indicator AS (
        SELECT
                *,
                CASE WHEN ABS(diff_from_avg / species_avg_temp) >= 0.005 THEN
                        1
                ELSE
                        0
                END AS is_exceptional
        FROM
                checkups
),
grouped AS (
        SELECT
                species,
                name,
                SUM(is_exceptional) AS no_of_exceptions,
        MAX(
                CASE WHEN is_exceptional = 1 THEN
                        checkup_time
                ELSE
                        NULL
                END) AS latest_exceptional_checkup
FROM
        indicator
GROUP BY
        species,
        name
),
ntiles AS (
        SELECT
                *,
                NTILE(4) OVER (PARTITION BY species ORDER BY no_of_exceptions ASC,
                        latest_exceptional_checkup DESC) AS ntile
        FROM
                grouped
)
SELECT
        species,
        name,
        no_of_exceptions,
        latest_exceptional_checkup
FROM
        ntiles
WHERE
        ntile = 1
ORDER BY
        species ASC,
        no_of_exceptions ASC,
        latest_exceptional_checkup DESC;

-- Show how much animals gained on weight in last 3 months
SELECT
        species,
        name,
        checkup_time,
        weight,
        weight - LAG(weight) OVER (PARTITION BY species, name ORDER BY checkup_time ASC) AS weight_diff
FROM
        routine_checkups
ORDER BY
        species ASC,
        name ASC,
        checkup_time ASC;

WITH weight_diff AS (
        SELECT
                species,
                name,
                checkup_time,
                weight,
                weight - FIRST_VALUE(weight) OVER (PARTITION BY species,
                        name ORDER BY CAST(checkup_time AS date) ASC RANGE BETWEEN '3 months' PRECEDING AND '1 day' PRECEDING) AS weight_diff
        FROM
                routine_checkups
        ORDER BY
                species ASC,
                name ASC,
                checkup_time ASC
),
percent_weight_diff AS (
        SELECT
                *,
                CAST(100 * weight_diff / weight AS DECIMAL(5, 2)) AS percent_diff
        FROM
                weight_diff
)
SELECT
        *
FROM
        percent_weight_diff
WHERE
        percent_diff IS NOT NULL
ORDER BY
        ABS(percent_diff) DESC;

-- Return top 5 most improved quarters in terms of
-- the number of adoptions, both per species and overall.
-- The first observation is the bottom line.
-- In case of a tie return the most recent quarter.
WITH quarter_and_year AS (
        SELECT
                species,
                name,
                adoption_date,
                EXTRACT(quarter FROM adoption_date) AS qrtr_,
                DATE_PART('YEAR', adoption_date) AS year_,
                CONCAT(EXTRACT(quarter FROM adoption_date), 'Q', DATE_PART('YEAR', adoption_date)) AS quarter_year
        FROM
                adoptions
        ORDER BY
                year_,
                qrtr_ ASC
),
count_by_quarter AS (
        SELECT
                species,
                quarter_year,
                COUNT(*) OVER (PARTITION BY species,
                        quarter_year) AS count_
        FROM
                quarter_and_year
        ORDER BY
                species,
                year_,
                qrtr_ ASC
)
SELECT
        species,
        quarter_year,
        COUNT(*) AS result
FROM
        count_by_quarter
GROUP BY
        GROUPING SETS ((),
        quarter_year,
        species,
(species,
                quarter_year))
ORDER BY
        species,
        result DESC,
        quarter_year;

--
