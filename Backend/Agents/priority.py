# ============================================================
# PRIORITY AGENT
# ============================================================

def calculate_priority(incident):
    """
    Calculate priority using deterministic Python rules.
    """

    disaster_type = str(
        incident.get(
            "incident_type",
            incident.get("type", "unknown")
        )
    ).lower()

    severity = str(
        incident.get("severity", "medium")
    ).lower()

    try:
        confidence = float(
            incident.get("confidence", 0.0)
        )
    except (ValueError, TypeError):
        confidence = 0.0

    confidence = max(0.0, min(1.0, confidence))

    score = 0

    # --------------------------------------------------------
    # SEVERITY
    # --------------------------------------------------------

    severity_scores = {
        "high": 50,
        "medium": 30,
        "low": 10
    }

    score += severity_scores.get(severity, 20)

    # --------------------------------------------------------
    # DISASTER TYPE
    # --------------------------------------------------------

    disaster_weights = {
        "tsunami": 30,
        "earthquake": 25,
        "cyclone": 25,
        "flood": 25,
        "flash flood": 30,
        "landslide": 20,
        "wildfire": 20,
        "fire": 20,
        "storm": 20,
        "drought": 10
    }

    score += disaster_weights.get(
        disaster_type,
        15
    )

    # --------------------------------------------------------
    # EARTHQUAKE MAGNITUDE
    # --------------------------------------------------------

    if disaster_type == "earthquake":

        try:
            magnitude = float(
                incident.get("magnitude", 0)
            )
        except (ValueError, TypeError):
            magnitude = 0

        if magnitude >= 6:
            score += 30

        elif magnitude >= 5:
            score += 20

        elif magnitude >= 4:
            score += 10

    # --------------------------------------------------------
    # CONFIDENCE
    # --------------------------------------------------------

    if confidence >= 0.90:
        score += 10

    elif confidence >= 0.70:
        score += 5

    # --------------------------------------------------------
    # FINAL PRIORITY
    # --------------------------------------------------------

    if score >= 80:
        priority = "CRITICAL"

    elif score >= 60:
        priority = "HIGH"

    elif score >= 35:
        priority = "MEDIUM"

    else:
        priority = "LOW"

    incident["priority_score"] = score
    incident["priority"] = priority

    return incident


# ============================================================
# PRIORITIZE ALL INCIDENTS
# ============================================================

def prioritize_incidents(incidents):

    prioritized = []

    for incident in incidents:

        prioritized.append(
            calculate_priority(incident)
        )

    prioritized.sort(
        key=lambda incident: incident.get(
            "priority_score",
            0
        ),
        reverse=True
    )

    return prioritized