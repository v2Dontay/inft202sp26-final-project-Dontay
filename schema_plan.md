# Schema Plan: Active School Construction Projects

## Project Focus

The main question we want the database to help answer is:

> Which borough has the most active school construction projects?

To answer that well, the database needs to connect each construction project to the school building where it is happening. The building table will store borough and location details. The project table will store the construction work and award amount.

## Table 1: `buildings`

One row in `buildings` represents one school building or construction site.

| Column name | Comes from CSV column | Suggested type | Notes |
|---|---|---|---|
| `building_id` | `Building ID` | `TEXT` | Primary key. This identifies one building/site. |
| `school_name` | `School Name` | `TEXT` | Name of the school or site. |
| `building_address` | `Building Address` | `TEXT` | Street address. |
| `city` | `City` | `TEXT` | City name from the address. |
| `borough` | `Borough` | `TEXT` | Borough name, useful for the main analysis question. |
| `borough_code` | `BoroughCode` | `TEXT` | Short borough code. |
| `geographical_district` | `Geographical District` | `INTEGER` | School district number. |
| `latitude` | `Latitude` | `NUMERIC` | Building latitude. Some rows are blank. |
| `longitude` | `Longitude` | `NUMERIC` | Building longitude. Some rows are blank. |

### Key

`building_id` should be the primary key for this table.

### Columns intentionally left out

To keep the schema simpler, we are not keeping these detailed location columns:

- `Postcode`
- `Community Board`
- `Council District`
- `BIN`
- `BBL`
- `Census Tract (2020)`
- `Neighborhood Tabulation Area (NTA) (2020)`
- `Location 1`

`Location 1` is also repeated information because latitude and longitude already store the same basic location.

## Table 2: `projects`

One row in `projects` represents one active construction project.

| Column name | Comes from CSV column | Suggested type | Notes |
|---|---|---|---|
| `project_id` | New column | `INTEGER` | Primary key. The original CSV does not include a clear project ID. |
| `building_id` | `Building ID` | `TEXT` | Foreign key that connects the project to `buildings`. |
| `project_description` | `Project Description` | `TEXT` | Description of the construction work. |
| `construction_award` | `Construction Award` | `NUMERIC` | Dollar amount for the project. The CSV value has commas, so it will need cleaning during import. |
| `project_type` | `Project type` | `TEXT` | Project category, mostly CIP or CAP. |

### Keys

`project_id` should be the primary key for this table.

`building_id` should be a foreign key that points to `buildings(building_id)`.

## Relationship

The relationship is:

> One building can have many projects.

In database terms:

`buildings.building_id` connects to `projects.building_id`.

This is useful because the project table does not need to repeat the full school address and borough information every time. Instead, each project stores the building ID, and PostgreSQL can connect it to the building details when needed.

## Why This Design Fits the Data

The CSV has 936 project rows but only 690 unique building IDs. That means some buildings have more than one active construction project. Splitting the data into `buildings` and `projects` matches the real structure of the data:

- Building information belongs in `buildings`.
- Construction work information belongs in `projects`.
- `building_id` links the two together.

## Future Query Ideas

This schema will support questions like:

1. Which borough has the most active construction projects?
2. Which borough has the highest average construction award?
3. Which project types are most common?
4. Which buildings have multiple active projects?
5. Which school districts have the most active projects?
