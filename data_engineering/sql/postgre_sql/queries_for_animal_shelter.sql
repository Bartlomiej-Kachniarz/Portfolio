SELECT *, 'SQL is FUN' as Fact
FROM Staff;
SELECT  *
FROM    staff
        INNER JOIN
        staff_roles
        ON 1=1;

SELECT A.name,
    AD.adopter_email,
    A.implant_chip_id,
    A.breed,
    A.admission_date
FROM animals as A
    LEFT OUTER JOIN adoptions as AD ON A.name = AD.name
        AND A.species = AD.species;

SELECT *
FROM animals AS A
    LEFT OUTER JOIN adoptions AS AD
    INNER JOIN persons as P ON P.email = AD.adopter_email ON A.name = AD.name
        AND A.species = AD.species;

SELECT *
FROM adoptions as AD
    INNER JOIN persons as P ON P.email = AD.adopter_email
    RIGHT OUTER JOIN animals as A ON AD.name = A.name
        AND AD.species = A.species;

SELECT A.name,
    A.species,
    A.primary_color,
    A.breed,
    V.vaccination_time,
    V.vaccine,
    P.first_name,
    P.last_name,
    SA.email,
    SA.role
FROM animals AS A
    LEFT OUTER JOIN persons as P
    INNER JOIN vaccinations as V
    INNER JOIN staff_assignments as SA ON V.email = SA.email ON P.email = V.email ON A.name = V.name
        AND A.species = V.species
ORDER BY A.name,
    A.species,
    A.breed,
    P.first_name;

SELECT  *
FROM    animals as A
WHERE   A.species = 'Dog'
        AND A.breed <> 'Bullmastiff';
        