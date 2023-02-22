SELECT
    HOUR(DATETIME) HOUR,
    COUNT(DATETIME) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR>=9 AND HOUR<=19
ORDER BY HOUR;