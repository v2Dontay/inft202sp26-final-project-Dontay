# NYC School Construction Database Project

This project explores active school construction projects in New York City. It uses a PostgreSQL database with two related tables, student-written SQL queries, and a Flask dashboard that summarizes the results.

## Dataset

Dataset file:

- `Active_Projects_Under_Construction_20260521.csv`

The dataset contains active construction projects at NYC school buildings. Each row in the original CSV represents one construction project, including the school name, building ID, borough, project description, project type, and construction award amount.

The dataset has:

- 936 active construction project rows
- 690 unique school buildings
- 5 boroughs represented, plus a few rows with blank borough data
- Construction award amounts that can be compared by borough, district, and project type

## Data Exploration

The data exploration process showed that the original CSV repeats building information when a building has more than one active project. That made it a good fit for a relational database design.

Important observations:

- `Building ID` is the best identifier for a school building.
- `Construction Award` is the main numeric measurement.
- `Borough`, `Project type`, and `Geographical District` are useful grouping columns.
- Some location fields had blank values, so the final schema kept the location data simple.

Exploration notes are saved in:

- `data_exploration.md`

## Database Schema

The database is split into two related tables.

### `building`

One row represents one school building or construction site.

Main columns:

- `building_id`
- `school_name`
- `building_address`
- `city`
- `borough`
- `borough_code`
- `geographical_district`
- `latitude`
- `longitude`

### `projects`

One row represents one active construction project.

Main columns:

- `project_id`
- `building_id`
- `project_description`
- `construction_award`
- `project_type`

The relationship is:

`projects.building_id` connects to `building.building_id`.

Schema planning notes are saved in:

- `schema_plan.md`
- `table_creation.sql`

## Import Process

The original CSV was cleaned into two import files:

- `data/building_import.csv`
- `data/projects_import.csv`

The import commands are saved in:

- `import.sql`

After import, the database contained:

- `building`: 690 rows
- `projects`: 936 rows

## Guided SQL Queries

The project includes six guided SQL queries.

1. `queries/query_1.sql` - Shows the 10 highest-award Queens construction projects.
2. `queries/query_2.sql` - Counts active construction projects by borough.
3. `queries/query_3.sql` - Calculates average construction award amount by borough.
4. `queries/query_4.sql` - Shows boroughs with more than 100 projects and their average award.
5. `queries/query_5.sql` - Lists Queens construction projects with school and address details.
6. `queries/query_6.sql` - Calculates total construction award amount by borough.

## Discussion Queries

Two discussion queries were selected for deeper analysis.

### Queens vs. Brooklyn Average Awards

File:

- `discussion/discussion_1.sql`

Explanation:

Queens has the higher average construction award compared with Brooklyn. This suggests that active construction projects in Queens are usually larger or more expensive than Brooklyn projects in this dataset.

### Geographical District Project Counts

File:

- `discussion/discussion_2.sql`

Explanation:

The results reveal that construction activity is not spread evenly across the city, as certain areas see much higher development than others. The data shows that District 27 has the most active projects of any geographical district. This suggests that infrastructure needs or funding priorities may be focused on that particular region compared to the rest of the districts.

## Flask Dashboard

The project includes a Flask web dashboard connected to the PostgreSQL database.

Pages:

- `/` - Dashboard with summary statistics and Chart.js charts
- `/browse` - Searchable table of school buildings
- `/insights` - Discussion query results and explanations

Main app files:

- `app.py`
- `templates/base.html`
- `templates/index.html`
- `templates/browse.html`
- `templates/insights.html`

## Running the Project

Start the PostgreSQL database and Adminer:

```bash
docker compose up
```

Start the Flask app:

```bash
docker compose --profile app up --build
```

Open the app:

```text
http://localhost:5000
```

Open Adminer:

```text
http://localhost:8080
```

Adminer login:

- System: `PostgreSQL`
- Server: `postgres`
- Username: `postgres`
- Password: `postgres`
- Database: `final`

Beekeeper Studio connection:

- Connection type: `Postgres`
- Host: `localhost`
- Port: `5432`
- User: `postgres`
- Password: `postgres`
- Default database: `final`

## Environment File

The Flask app uses `.env` for database connection settings. This file is listed in `.gitignore` so the database password is not committed to GitHub.

## What This Project Demonstrates

This project demonstrates how to:

- Explore a real-world CSV dataset
- Design a relational PostgreSQL schema
- Split repeated CSV data into related tables
- Import cleaned data into PostgreSQL
- Write SQL using `SELECT`, `WHERE`, `GROUP BY`, `HAVING`, aggregate functions, and `JOIN`
- Build a Flask dashboard connected to a PostgreSQL database
