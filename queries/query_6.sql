SELECT 
    building.borough, 
    SUM(projects.construction_award)
FROM projects
INNER JOIN building 
    ON projects.building_id = building.building_id
GROUP BY building.borough
ORDER BY SUM(projects.construction_award) DESC;
