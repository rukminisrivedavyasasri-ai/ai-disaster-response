# ============================================================
# RESOURCE ALLOCATION AGENT
# ============================================================

DEFAULT_RESOURCES = {
    "ambulances": 5,
    "fire_trucks": 3,
    "rescue_teams": 4
}


RESOURCE_REQUIREMENTS = {
    "earthquake": {
        "ambulances": 2,
        "rescue_teams": 2,
        "fire_trucks": 0
    },

    "flood": {
        "ambulances": 2,
        "rescue_teams": 2,
        "fire_trucks": 0
    },

    "cyclone": {
        "ambulances": 2,
        "rescue_teams": 2,
        "fire_trucks": 1
    },

    "tsunami": {
        "ambulances": 3,
        "rescue_teams": 3,
        "fire_trucks": 1
    },

    "landslide": {
        "ambulances": 2,
        "rescue_teams": 2,
        "fire_trucks": 1
    },

    "wildfire": {
        "ambulances": 1,
        "rescue_teams": 1,
        "fire_trucks": 2
    },

    "fire": {
        "ambulances": 1,
        "rescue_teams": 1,
        "fire_trucks": 2
    },

    "flash flood": {
        "ambulances": 2,
        "rescue_teams": 3,
        "fire_trucks": 0
    }
}


def allocate_resources(incident, available_resources):

    disaster_type = str(
        incident.get(
            "incident_type",
            incident.get("type", "unknown")
        )
    ).lower()

    requirements = RESOURCE_REQUIREMENTS.get(
        disaster_type,
        {
            "ambulances": 1,
            "rescue_teams": 1,
            "fire_trucks": 0
        }
    )

    allocation = {}
    fully_allocated = True

    for resource, required in requirements.items():

        available = available_resources.get(resource, 0)

        assigned = min(required, available)

        allocation[resource] = assigned

        available_resources[resource] = available - assigned

        if assigned < required:
            fully_allocated = False

    incident["allocated_resources"] = allocation

    incident["allocation_status"] = (
        "FULLY_ALLOCATED"
        if fully_allocated
        else "PARTIALLY_ALLOCATED"
    )

    incident["response_action"] = (
        f"Deploy resources to "
        f"{incident.get('location', 'unknown location')}"
    )

    return incident


def allocate_all_resources(incidents, resources=None):

    if resources is None:
        resources = DEFAULT_RESOURCES.copy()
    else:
        resources = resources.copy()

    allocation_results = []

    # Incidents must already be sorted by priority.
    for incident in incidents:

        incident = allocate_resources(
            incident,
            resources
        )

        allocation_results.append(incident)

    return allocation_results, resources