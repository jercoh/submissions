SELECT player1, SUM(totalcount)
FROM (
		(
		SELECT player1, SUM(count) AS totalcount
		FROM (
			SELECT player1, COUNT(*) AS count FROM us_men GROUP BY player1 
			UNION ALL
			SELECT player2, COUNT(*) AS count FROM us_men GROUP BY player2
			) AS mytable 
		GROUP BY player1 
		ORDER BY SUM(count) DESC
		)
		UNION ALL
		(
		SELECT player1, SUM(count) AS totalcount
		FROM (
			SELECT player1, COUNT(*) AS count FROM french_men GROUP BY player1 
			UNION ALL
			SELECT player2, COUNT(*) AS count FROM french_men GROUP BY player2
			) AS mytable1 
		GROUP BY player1 
		ORDER BY SUM(count) DESC
		)
		UNION ALL
		(SELECT player1, SUM(count) AS totalcount
		FROM (
			SELECT player1, COUNT(*) AS count FROM aus_men GROUP BY player1 
			UNION  ALL
			SELECT player2, COUNT(*) AS count FROM aus_men GROUP BY player2
			) AS mytable2
		GROUP BY player1 
		ORDER BY SUM(count) DESC
		)
) AS tournaments
GROUP BY player1 
ORDER BY SUM(totalcount);