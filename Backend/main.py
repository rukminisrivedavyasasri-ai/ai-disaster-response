# ============================================================
# AI DISASTER RESPONSE SYSTEM
# MAIN COORDINATOR
# ============================================================

from Agents.ingestion import ingest_all_sources
from Agents.verification import verify_all_reports
from Agents.priority import prioritize_incidents
from Agents.allocation import allocate_all_resources


# ============================================================
# RESPONSE COORDINATOR
# ============================================================

def run_disaster_response():

    print("\n========================================")
    print("AI DISASTER RESPONSE SYSTEM")
    print("========================================")

    # --------------------------------------------------------
    # 1. INGESTION
    # --------------------------------------------------------

    print("\n[1] INGESTION AGENT")
    print("-------------------")

    incidents = ingest_all_sources()

    print(
        f"Received {len(incidents)} total incidents."
    )

    if not incidents:
        print("No incidents received.")
        return {
            "incidents": [],
            "remaining_resources": {}
        }

    # --------------------------------------------------------
    # SELECT REPRESENTATIVE INCIDENTS
    # --------------------------------------------------------
    # The ingestion layer contains many real USGS events
    # followed by simulated multi-disaster reports.
    #
    # We process a small representative set through Gemini
    # so the live demo remains fast and reliable.

    real_incidents = incidents[:1]

    simulated_incidents = [
        incident
        for incident in incidents
        if str(incident.get("source", "")).startswith("SIMULATED")
    ]

    incidents_to_process = (
        real_incidents +
        simulated_incidents
    )

    print(
        f"Selected {len(incidents_to_process)} incidents "
        "for the response pipeline."
    )

    # --------------------------------------------------------
    # 2. VERIFICATION
    # --------------------------------------------------------

    print("\n[2] VERIFICATION AGENT")
    print("----------------------")

    verified_incidents = verify_all_reports(
        incidents_to_process
    )

    print(
        f"Verified {len(verified_incidents)} incidents."
    )

    # --------------------------------------------------------
    # 3. PRIORITY
    # --------------------------------------------------------

    print("\n[3] PRIORITY AGENT")
    print("------------------")

    prioritized_incidents = prioritize_incidents(
        verified_incidents
    )

    print("Incidents prioritized.")

    # --------------------------------------------------------
    # 4. RESOURCE ALLOCATION
    # --------------------------------------------------------

    print("\n[4] RESOURCE ALLOCATION AGENT")
    print("-----------------------------")

    allocated_incidents, remaining_resources = (
        allocate_all_resources(
            prioritized_incidents
        )
    )

    print("Resources allocated.")

    # --------------------------------------------------------
    # 5. FINAL RESPONSE PLAN
    # --------------------------------------------------------

    print("\n[5] RESPONSE PLAN")
    print("-----------------")

    for incident in allocated_incidents:

        print(
            f"\n{incident.get('priority', 'UNKNOWN')} | "
            f"{incident.get('incident_type', 'UNKNOWN')} | "
            f"{incident.get('location', 'UNKNOWN')}"
        )

        print(
            f"Score: "
            f"{incident.get('priority_score', 0)}"
        )

        print(
            f"Resources: "
            f"{incident.get('allocated_resources', {})}"
        )

        print(
            f"Status: "
            f"{incident.get('allocation_status', 'UNKNOWN')}"
        )

    response_plan = {
        "incidents": allocated_incidents,
        "remaining_resources": remaining_resources
    }

    print("\n========================================")
    print("RESPONSE PLAN GENERATED")
    print("========================================")

    return response_plan


# ============================================================
# START SYSTEM
# ============================================================

if __name__ == "__main__":

    run_disaster_response()