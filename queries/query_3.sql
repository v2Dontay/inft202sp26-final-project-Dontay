SELECT
    building.borough,
    AVG(projects.construction_award)
FROM projects
JOIN building
    ON projects.building_id = building.building_id
GROUP BY building.borough
ORDER BY AVG(projects.construction_award) DESC;
