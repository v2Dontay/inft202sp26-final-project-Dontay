SELECT 
    building.geographical_district, 
    COUNT(*)
FROM projects
INNER JOIN building 
    ON projects.building_id = building.building_id
GROUP BY building.geographical_district
ORDER BY COUNT(*) DESC;
