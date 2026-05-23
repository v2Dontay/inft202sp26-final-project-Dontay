# Data Exploration: Active Projects Under Construction

## Dataset File

File: `Active_Projects_Under_Construction_20260521.csv`

This dataset appears to describe active school construction projects in New York City. Each row looks like one construction project at one school/building, with project details, award amount, project type, and location information for the school building.

## Basic Shape

- Rows: 936
- Columns: 20
- Main subject: active construction projects at school buildings
- Likely source: NYC public school construction / active projects data

## First Impressions

One row appears to represent a single construction project. The school and building details repeat across rows when the same building has multiple active projects. That repetition is useful because it gives us a natural way to split the data into related database tables later.

## Important Columns

| Column | What it appears to represent | Possible PostgreSQL type |
|---|---|---|
| `School Name` | Name of the school or project site | `TEXT` |
| `Building ID` | Code identifying the school building | `TEXT` |
| `Building Address` | Street address of the school building | `TEXT` |
| `City` | City name from the address | `TEXT` |
| `Borough` | NYC borough name | `TEXT` |
| `BoroughCode` | Short borough code, such as Q, K, X, M, R | `TEXT` |
| `Geographical District` | NYC school district number | `INTEGER` or `TEXT` |
| `Project Description` | Description of construction work | `TEXT` |
| `Construction Award` | Dollar amount awarded for the project | `NUMERIC` |
| `Project type` | Project category, mainly CIP or CAP | `TEXT` |
| `Latitude` | Building latitude | `NUMERIC` |
| `Longitude` | Building longitude | `NUMERIC` |
| `Community Board` | NYC community board number | `TEXT` |
| `Council District` | NYC council district number | `INTEGER` or `TEXT` |
| `BIN` | Building Identification Number | `TEXT` |
| `BBL` | Borough Block Lot identifier | `TEXT` |
| `Census Tract (2020)` | 2020 census tract | `TEXT` |
| `Neighborhood Tabulation Area (NTA) (2020)` | NYC neighborhood tabulation area code | `TEXT` |
| `Location 1` | Combined latitude/longitude text value | `TEXT` |

## Repeated Values and Categories

The dataset has several columns that will be useful for grouping and comparing records:

- `Borough`: 5 boroughs, plus 4 blank values
- `Project type`: 2 values
  - CIP: 882 rows
  - CAP: 54 rows
- `Geographical District`: 34 different values
- `Community Board`: 59 different values
- `Council District`: 51 different values

Project counts by borough:

| Borough | Project count |
|---|---:|
| QUEENS | 295 |
| BROOKLYN | 282 |
| BRONX | 159 |
| MANHATTAN | 134 |
| STATEN IS | 62 |
| Blank | 4 |

## Numeric Notes

`Construction Award` is the main numeric measurement in the dataset.

- Number of award values: 936
- Minimum award: 0
- Maximum award: 119,840,000
- Average award: about 8,660,088

This column will be useful for questions about most expensive projects, average award amount by borough, or total construction dollars by project type.

## Possible IDs

`Building ID` looks like the strongest candidate for identifying a school building.

- Unique `Building ID` values: 690
- Total project rows: 936
- Buildings with more than one project: 194

This suggests that `Building ID` can connect a building/school table to a projects table.

Possible primary key and foreign key ideas:

- Candidate primary key for a future buildings table: `Building ID`
- Candidate foreign key in a future projects table: `Building ID`
- The project rows do not have an obvious unique project ID, so we may need to create one later or use a combination of columns.

## Data Quality Notes

Some fields have blank values:

- `Borough`: 4 blanks
- `Latitude`: 4 blanks
- `Longitude`: 4 blanks
- `Community Board`: 4 blanks
- `Council District`: 4 blanks
- `BIN`: 16 blanks
- `BBL`: 16 blanks
- `Census Tract (2020)`: 4 blanks
- `Neighborhood Tabulation Area (NTA) (2020)`: 4 blanks
- `Location 1`: 4 blanks

Other notes:

- `Construction Award` is stored with commas, so it will need cleaning before loading as a number.
- `Postcode` looks suspicious because several early rows show `10128`, even for schools outside Manhattan. We should be careful using it.
- `Location 1` duplicates the latitude and longitude values, so it may not be necessary to keep.
- `Borough` and `BoroughCode` contain similar information. We may keep both or choose one depending on the final schema.

## Interesting Analysis Questions

Here are some questions this dataset could support later:

1. Which borough has the most active school construction projects?
2. Which 10 active projects have the highest construction award amounts?
3. What is the average construction award amount by borough?
4. Which school buildings have more than one active construction project?
5. Which geographical districts have the highest total construction award amount?

## Early Table Ideas

A possible relational design would split the single CSV into two related tables:

| Table | One row represents | Possible key |
|---|---|---|
| `buildings` | One school building or construction site | `Building ID` |
| `projects` | One active construction project | A new project ID, with `Building ID` linking back to `buildings` |

This design would reduce repeated building information and make joins meaningful later.
