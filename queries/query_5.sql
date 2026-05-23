SELECT 
    building.school_name, 
    building.building_address, 
    projects.project_description, 
    projects.construction_award
FROM projects
INNER JOIN building 
    ON projects.building_id = building.building_id
WHERE UPPER(building.borough) LIKE '%QUEENS%';
