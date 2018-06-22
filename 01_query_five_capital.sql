SELECT
city.`Name`,
city.`Population`,
country.`Name`

FROM
`country`,
`city`

WHERE country.`Capital` = city.`ID`

ORDER BY `Population` DESC

LIMIT 0,5;