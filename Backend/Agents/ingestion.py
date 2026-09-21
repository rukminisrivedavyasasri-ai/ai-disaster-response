import requests


# ============================================================
# USGS - REAL EARTHQUAKE DATA
# ============================================================

USGS_URL = (
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/"
    "summary/all_day.geojson"
)


def ingest_usgs_earthquakes():
    """Fetch real earthquake events from USGS."""

    print("Fetching earthquake data from USGS...")

    response = requests.get(USGS_URL, timeout=10)
    response.raise_for_status()

    data = response.json()

    incidents = []

    for event in data.get("features", []):

        properties = event.get("properties", {})
        coordinates = event.get("geometry", {}).get("coordinates", [])

        if len(coordinates) < 3:
            continue

        incidents.append({
            "id": event.get("id"),
            "source": "USGS",
            "type": "earthquake",
            "location": properties.get("place"),
            "magnitude": properties.get("mag"),
            "time": properties.get("time"),
            "longitude": coordinates[0],
            "latitude": coordinates[1],
            "depth_km": coordinates[2],
            "url": properties.get("url")
        })

    return incidents


# ============================================================
# IMD - REAL WEATHER WARNINGS
# ============================================================

IMD_WARNING_URL = (
    "https://mausam.imd.gov.in/api/"
    "warnings_district_api.php"
)


def ingest_imd_warning(district_id):
    """
    Fetch an official IMD district warning.

    district_id must be the official IMD district object ID.
    """

    print(f"Fetching IMD warning for district {district_id}...")

    url = f"{IMD_WARNING_URL}?id={district_id}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


# ============================================================
# SIMULATED REPORTS
# ============================================================
# These represent sources such as emergency calls,
# social-media reports and field reports.
#
# They are explicitly marked as SIMULATED.
# ============================================================

def ingest_simulated_reports():

    print("Loading simulated disaster reports...")

    reports = [

        {
            "id": "SIM-FLOOD-001",
            "source": "SIMULATED_EMERGENCY_REPORT",
            "type": "flood",
            "location": "Hyderabad, Telangana",
            "description":
                "Water level rising rapidly after heavy rainfall. "
                "Several roads are becoming difficult to cross."
        },

        {
            "id": "SIM-CYCLONE-001",
            "source": "SIMULATED_SOCIAL_REPORT",
            "type": "cyclone",
            "location": "Visakhapatnam, Andhra Pradesh",
            "description":
                "Strong winds and heavy rainfall reported near "
                "the coastal area."
        },

        {
            "id": "SIM-LANDSLIDE-001",
            "source": "SIMULATED_FIELD_REPORT",
            "type": "landslide",
            "location": "Nilgiris, Tamil Nadu",
            "description":
                "A landslide has blocked part of a mountain road."
        },

        {
            "id": "SIM-WILDFIRE-001",
            "source": "SIMULATED_SENSOR",
            "type": "wildfire",
            "location": "Nainital, Uttarakhand",
            "description":
                "Smoke and elevated temperature detected in "
                "a forest region."
        },

        {
            "id": "SIM-EARTHQUAKE-001",
            "source": "SIMULATED_EMERGENCY_REPORT",
            "type": "earthquake",
            "location": "Guwahati, Assam",
            "description":
                "Residents report strong shaking and possible "
                "structural damage."
        },

        {
            "id": "SIM-TSUNAMI-001",
            "source": "SIMULATED_COASTAL_ALERT",
            "type": "tsunami",
            "location": "Andaman and Nicobar Islands",
            "description":
                "Potential tsunami warning requiring coastal "
                "evacuation assessment."
        }
    ]

    return reports


# ============================================================
# UNIFIED INGESTION
# ============================================================

def ingest_all_sources():

    all_incidents = []

    # --------------------------------------------------------
    # 1. REAL USGS DATA
    # --------------------------------------------------------

    try:

        earthquakes = ingest_usgs_earthquakes()

        all_incidents.extend(earthquakes)

        print(
            f"USGS: {len(earthquakes)} real earthquake "
            f"incidents received."
        )

    except Exception as error:

        print(f"USGS ingestion failed: {error}")


    # --------------------------------------------------------
    # 2. SIMULATED MULTI-DISASTER REPORTS
    # --------------------------------------------------------

    simulated_reports = ingest_simulated_reports()

    all_incidents.extend(simulated_reports)

    print(
        f"Simulated reports: "
        f"{len(simulated_reports)} incidents received."
    )


    return all_incidents


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    incidents = ingest_all_sources()

    print("\n========================================")
    print("UNIFIED DISASTER INCIDENTS")
    print("========================================")

    print(f"Total incidents: {len(incidents)}")

    for incident in incidents[:15]:

        print("\n----------------------------------------")
        print(incident)