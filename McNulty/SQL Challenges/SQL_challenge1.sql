SELECT player1, SUM(totalcount)
FROM (
		(
		SELECT player1, SUM(count) AS totalcount
		FROM (
			SELECT player1, COUNT(*) AS count FROM us_women GROUP BY player1 
			UNION 
			SELECT player2, COUNT(*) AS count FROM us_women GROUP BY player2
			) AS mytable 
		GROUP BY player1 
		ORDER BY SUM(count) DESC
		)
		UNION
		(
		SELECT player1, SUM(count) AS totalcount
		FROM (
			SELECT player1, COUNT(*) AS count FROM french_women GROUP BY player1 
			UNION 
			SELECT player2, COUNT(*) AS count FROM french_women GROUP BY player2
			) AS mytable1 
		GROUP BY player1 
		ORDER BY SUM(count) DESC
		)
		UNION
		(SELECT player1, SUM(count) AS totalcount
		FROM (
			SELECT player1, COUNT(*) AS count FROM aus_women GROUP BY player1 
			UNION 
			SELECT player2, COUNT(*) AS count FROM aus_women GROUP BY player2
			) AS mytable2
		GROUP BY player1 
		ORDER BY SUM(count) DESC
		)
) AS tournaments
GROUP BY player1 
ORDER BY SUM(totalcount) DESC;