SELECT name, maxfirstserve
FROM (
		SELECT player1 AS name, fsp_1 AS maxfirstserve FROM us_men WHERE fsp_1=(SELECT MAX(fsp_1) FROM us_men)
		UNION ALL
		SELECT player2 AS name, fsp_2 AS maxfirstserve FROM us_men WHERE fsp_2=(SELECT MAX(fsp_2) FROM us_men)
		UNION ALL
		SELECT player1 AS name, fsp_1 AS maxfirstserve FROM aus_men WHERE fsp_1=(SELECT MAX(fsp_1) FROM aus_men)
		UNION ALL
		SELECT player2 AS name, fsp_2 AS maxfirstserve FROM aus_men WHERE fsp_2=(SELECT MAX(fsp_2) FROM aus_men)
		UNION ALL
		SELECT player1 AS name, fsp_1 AS maxfirstserve FROM french_men WHERE fsp_1=(SELECT MAX(fsp_1) FROM french_men)
		UNION ALL
		SELECT player2 AS name, fsp_2 AS maxfirstserve FROM french_men WHERE fsp_2=(SELECT MAX(fsp_2) FROM french_men)
) AS t
ORDER BY maxfirstserve;