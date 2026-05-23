SELECT
    building.borough,
    COUNT(*),
    AVG(projects.construction_award)
FROM projects
JOIN building
    ON projects.building_id = building.building_id
GROUP BY building.borough
HAVING COUNT(*) > 100;
