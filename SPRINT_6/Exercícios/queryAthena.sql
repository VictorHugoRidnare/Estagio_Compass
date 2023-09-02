SELECT nome, decada
FROM (
  SELECT
    nome,
    FLOOR(ano / 10) * 10 AS decada,
    SUM(total),
    ROW_NUMBER() OVER(PARTITION BY FLOOR(ano / 10) * 10 ORDER BY SUM(total) DESC) AS ordem
  FROM meubanco."tb_names"
  WHERE ano >= 1950 and ano <= 2011
  GROUP BY nome, FLOOR(ano / 10) * 10
) AS subquery
WHERE ordem <= 3
ORDER BY decada, ordem