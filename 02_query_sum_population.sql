SELECT
SUM(country.`Population`)


FROM
`country`,
`countrylanguage`

WHERE
country.`Continent` = 'Europe' AND
country.`Code` = countrylanguage.`CountryCode` AND
countrylanguage.`Language` = 'English'