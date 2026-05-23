-- INFT221 Final Project: Import Data
-- Run these commands in Adminer or Beekeeper Studio while connected to
-- the Docker PostgreSQL database named final.
--
-- These files were generated from:
-- Active_Projects_Under_Construction_20260521.csv
--
-- Docker sees this project folder at /project.

COPY building (
    building_id,
    school_name,
    building_address,
    city,
    borough,
    borough_code,
    geographical_district,
    latitude,
    longitude
)
FROM '/project/data/building_import.csv'
DELIMITER ','
CSV HEADER;

COPY projects (
    project_id,
    building_id,
    project_description,
    construction_award,
    project_type
)
FROM '/project/data/projects_import.csv'
DELIMITER ','
CSV HEADER;

-- After importing, run these checks:
-- SELECT COUNT(*) FROM building;
-- SELECT COUNT(*) FROM projects;
