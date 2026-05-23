SELECT 
    building.borough, 
    AVG(projects.construction_award)
FROM projects
INNER JOIN building 
    ON projects.building_id = building.building_id
WHERE UPPER(building.borough) LIKE '%QUEENS%' 
   OR UPPER(building.borough) LIKE '%BROOKLYN%'
GROUP BY building.borough;
