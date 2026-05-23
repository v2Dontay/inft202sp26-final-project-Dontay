SELECT
    building.borough,
    COUNT(*)
FROM projects
JOIN building
    ON projects.building_id = building.building_id
GROUP BY building.borough
ORDER BY COUNT(*) DESC;
