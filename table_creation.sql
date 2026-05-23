-- INFT221 Final Project: Table Creation Worksheet
-- Dataset: Active School Construction Projects
--
-- Open this file in Adminer or Beekeeper Studio while connected to the
-- PostgreSQL database named final.
--
-- Your job:
-- 1. Drop old tables if they already exist.
-- 2. Create the buildings table.
-- 3. Create the projects table.
-- 4. Add primary keys.
-- 5. Add the foreign key that connects projects to buildings.
--
-- Reminder:
-- The projects table depends on the buildings table, so if you use
-- DROP TABLE IF EXISTS, drop projects first, then buildings.


-- STEP 1: Drop tables if they already exist.
-- Write your DROP TABLE IF EXISTS statements below.
-- Hint: dependency order matters.



-- STEP 2: Create the buildings table.
-- One row should represent one school building or construction site.
--
-- Suggested columns:
-- building_id              TEXT      primary key
-- school_name              TEXT
-- building_address         TEXT
-- city                     TEXT
-- borough                  TEXT
-- borough_code             TEXT
-- geographical_district    INTEGER
-- latitude                 NUMERIC
-- longitude                NUMERIC
--
-- Think:
-- Which column identifies one building?
-- Which columns should probably be NOT NULL?



-- STEP 3: Create the projects table.
-- One row should represent one active construction project.
--
-- Suggested columns:
-- project_id               INTEGER   primary key
-- building_id              TEXT      foreign key to buildings
-- project_description      TEXT
-- construction_award       NUMERIC
-- project_type             TEXT
--
-- Think:
-- Which column identifies one project?
-- Which column connects the project back to a building?



-- STEP 4: After running your CREATE TABLE statements, you can check
-- that the tables exist by looking in Adminer or Beekeeper Studio.
--
-- When your table creation SQL runs without errors, come back to Codex
-- and tell me the tables were created.
