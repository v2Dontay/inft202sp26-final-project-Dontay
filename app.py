import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
import psycopg2
import psycopg2.extras


load_dotenv()

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "final"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        host=os.getenv("DB_HOST", "postgres"),
        port=os.getenv("DB_PORT", "5432"),
    )


def fetch_all(query, params=None):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            if params is None:
                cur.execute(query)
            else:
                cur.execute(query, params)
            return cur.fetchall()


def fetch_one(query, params=None):
    rows = fetch_all(query, params)
    return rows[0] if rows else {}


@app.route("/")
def index():
    stats = {
        "projects": fetch_one("SELECT COUNT(*) AS value FROM projects")["value"],
        "buildings": fetch_one("SELECT COUNT(*) AS value FROM building")["value"],
        "avg_award": fetch_one("SELECT AVG(construction_award) AS value FROM projects")["value"],
        "top_borough": fetch_one(
            """
            SELECT building.borough AS value
            FROM projects
            JOIN building ON projects.building_id = building.building_id
            WHERE building.borough <> ''
            GROUP BY building.borough
            ORDER BY COUNT(*) DESC
            LIMIT 1
            """
        )["value"],
    }

    project_counts = fetch_all(
        """
        SELECT building.borough, COUNT(*) AS project_count
        FROM projects
        JOIN building ON projects.building_id = building.building_id
        WHERE building.borough <> ''
        GROUP BY building.borough
        ORDER BY project_count DESC
        """
    )

    avg_awards = fetch_all(
        """
        SELECT building.borough, ROUND(AVG(projects.construction_award), 2) AS avg_award
        FROM projects
        JOIN building ON projects.building_id = building.building_id
        WHERE building.borough <> ''
        GROUP BY building.borough
        ORDER BY avg_award DESC
        """
    )

    return render_template(
        "index.html",
        stats=stats,
        project_counts=project_counts,
        avg_awards=avg_awards,
    )


@app.route("/browse")
def browse():
    page = max(request.args.get("page", 1, type=int), 1)
    search = request.args.get("search", "").strip()
    per_page = 25
    offset = (page - 1) * per_page

    where = ""
    params = []
    if search:
        where = "WHERE school_name ILIKE %s"
        params.append(f"%{search}%")

    total = fetch_one(f"SELECT COUNT(*) AS value FROM building {where}", params)["value"]
    rows = fetch_all(
        f"""
        SELECT building_id, school_name, building_address, city, borough,
               geographical_district, latitude, longitude
        FROM building
        {where}
        ORDER BY school_name
        LIMIT %s OFFSET %s
        """,
        params + [per_page, offset],
    )

    has_next = offset + per_page < total
    has_prev = page > 1

    return render_template(
        "browse.html",
        rows=rows,
        page=page,
        search=search,
        total=total,
        has_next=has_next,
        has_prev=has_prev,
    )


@app.route("/insights")
def insights():
    queens_vs_brooklyn = fetch_all(
        """
        SELECT building.borough, ROUND(AVG(projects.construction_award), 2) AS avg_award
        FROM projects
        INNER JOIN building ON projects.building_id = building.building_id
        WHERE UPPER(building.borough) LIKE '%QUEENS%'
           OR UPPER(building.borough) LIKE '%BROOKLYN%'
        GROUP BY building.borough
        ORDER BY avg_award DESC
        """
    )

    district_counts = fetch_all(
        """
        SELECT building.geographical_district, COUNT(*) AS project_count
        FROM projects
        INNER JOIN building ON projects.building_id = building.building_id
        GROUP BY building.geographical_district
        ORDER BY project_count DESC
        LIMIT 10
        """
    )

    insights_data = [
        {
            "title": "Queens vs. Brooklyn Average Awards",
            "description": (
                "Queens has the higher average construction award compared with Brooklyn. "
                "This suggests that active construction projects in Queens are usually larger "
                "or more expensive than Brooklyn projects in this dataset."
            ),
            "rows": queens_vs_brooklyn,
        },
        {
            "title": "Top Geographical Districts by Active Projects",
            "description": (
                "The results reveal that construction activity is not spread evenly across "
                "the city, as certain areas see much higher development than others. The data "
                "shows that District 27 has the most active projects of any geographical "
                "district. This suggests that infrastructure needs or funding priorities may "
                "be focused on that particular region compared to the rest of the districts."
            ),
            "rows": district_counts,
        },
    ]

    return render_template("insights.html", insights=insights_data)


@app.template_filter("money")
def money(value):
    if value is None:
        return "N/A"
    return "${:,.0f}".format(float(value))


@app.template_filter("number")
def number(value):
    if value is None:
        return "N/A"
    return "{:,}".format(int(value))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
