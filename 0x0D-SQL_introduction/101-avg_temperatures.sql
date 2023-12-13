-- A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(vlaue) AS avg_temp FRM temperatures
	GROUP BY city ORDER BY avg_temp DESC;
