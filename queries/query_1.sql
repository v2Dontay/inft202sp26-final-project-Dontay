SELECT 
    building.school_name, 
    projects.project_description, 
    building.borough, 
    projects.construction_award
FROM projects
INNER JOIN building 
    ON projects.building_id = building.building_id
WHERE UPPER(building.borough) LIKE '%QUEENS%'
ORDER BY projects.construction_award DESC
LIMIT 10;
