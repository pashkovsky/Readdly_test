SELECT
c.`Name`

FROM
`country` as c

WHERE
(SELECT COUNT(cl01.`CountryCode`)
	FROM `countrylanguage` as cl01
	WHERE
	c.`Code` = cl01.`CountryCode` AND
	cl01.`IsOfficial` = 'F'
	GROUP BY cl01.`CountryCode`)
	/
(SELECT COUNT(cl02.`CountryCode`)
	FROM `countrylanguage` as cl02
	WHERE
	c.`Code` = cl02.`CountryCode` AND
	cl02.`IsOfficial` = 'T'
	GROUP BY cl02.`CountryCode`
	HAVING COUNT(cl02.`CountryCode`) > 1)
	>= 2

-- Список стран с двумя и более официальными языками,
-- в которых количество неофициальных языков как минимум вдвое больше, чем официальных