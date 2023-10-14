-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

-- Lists bands with Glam rock as their style ranked by longetivity

SELECT band_name, IF(split IS NULL, 2022 - formed, split - formed)
AS lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY lifespan DESC
