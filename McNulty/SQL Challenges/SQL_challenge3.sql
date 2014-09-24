SELECT name, SUM(totalwins) AS wins, ROUND(SUM(totalufe)*100/SUM(totaltpw)) AS ufe_percentage
FROM (
		(
		SELECT name, SUM(wins) AS totalwins, SUM(ufe) AS totalufe, SUM(tpw) AS totaltpw 
		FROM (
			SELECT player2 AS name, SUM(CASE WHEN result = 0 THEN 1 END) AS wins, SUM(ufe_2) AS ufe, SUM(tpw_1) AS tpw FROM aus_men GROUP BY player2
			UNION ALL
			SELECT player1 AS name, SUM(CASE WHEN result = 1 THEN 1 END) AS wins, SUM(ufe_1) AS ufe, SUM(tpw_2) AS tpw FROM aus_men GROUP BY player1
			) AS mytable1 
		GROUP BY name
		)
		UNION ALL
		(
		SELECT name, SUM(wins) AS totalwins, SUM(ufe) AS totalufe, SUM(tpw) AS totaltpw 
		FROM (
			SELECT player2 AS name, SUM(CASE WHEN result = 0 THEN 1 END) AS wins, SUM(ufe_2) AS ufe, SUM(tpw_1) AS tpw FROM french_men GROUP BY player2
			UNION ALL
			SELECT player1 AS name, SUM(CASE WHEN result = 1 THEN 1 END) AS wins, SUM(ufe_1) AS ufe, SUM(tpw_2) AS tpw FROM french_men GROUP BY player1
			) AS mytable1 
		GROUP BY name
		)
		UNION ALL
		(
		SELECT name, SUM(wins) AS totalwins, SUM(ufe) AS totalufe, SUM(tpw) AS totaltpw 
		FROM (
			SELECT player2 AS name, SUM(CASE WHEN result = 0 THEN 1 END) AS wins, SUM(ufe_2) AS ufe, SUM(tpw_1) AS tpw FROM us_men GROUP BY player2
			UNION ALL
			SELECT player1 AS name, SUM(CASE WHEN result = 1 THEN 1 END) AS wins, SUM(ufe_1) AS ufe, SUM(tpw_2) AS tpw FROM us_men GROUP BY player1
			) AS mytable1 
		GROUP BY name
		)
) AS tournaments
GROUP BY name 
ORDER BY wins;