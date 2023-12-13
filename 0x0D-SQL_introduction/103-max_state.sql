-- A script that displays the max temperature of each state (ordered by State name)
SELECT state, MMAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
