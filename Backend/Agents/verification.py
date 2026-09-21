# ============================================================
# VERIFICATION AGENT
# ============================================================

import json
import os

from dotenv import load_dotenv
from google import genai

from Agents.ingestion import ingest_all_sources


# ============================================================
# GEMINI SETUP
# ============================================================

load_dotenv("Backend/.env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found.")

client = genai.Client(api_key=api_key)

GEMINI_AVAILABLE = True


# ============================================================
# FALLBACK VERIFICATION
# ============================================================

def fallback_verification(report):

    disaster_type = report.get(
        "type",
        report.get("incident_type", "unknown")
    )

    location = report.get(
        "location",
        "unknown"
    )

    description = report.get(
        "description",
        f"{disaster_type} incident reported at {location}."
    )

    # Basic deterministic severity
    high_priority_types = {
        "tsunami",
        "earthquake",
        "cyclone",
        "flash flood"
    }

    if str(disaster_type).lower() in high_priority_types:
        severity = "high"
    else:
        severity = "medium"

    return {
        "incident_type": disaster_type,
        "location": location,
        "severity": severity,
        "summary": description,
        "confidence": 0.70,
        "credible": True,
        "verification_method": "deterministic_fallback"
    }


# ============================================================
# VERIFY ONE REPORT
# ============================================================

def verify_report(report):

    global GEMINI_AVAILABLE

    # Once a quota error occurs, don't keep calling Gemini.
    if not GEMINI_AVAILABLE:
        return fallback_verification(report)

    prompt = f"""
You are the Verification Agent in a disaster-response
system.

Analyze this disaster report:

{json.dumps(report, indent=2)}

Extract:

1. Incident type
2. Location
3. Severity: low, medium, or high
4. Short factual summary
5. Confidence from 0 to 1
6. Whether the report is credible

Do not invent information.

Return ONLY valid JSON:

{{
    "incident_type": "...",
    "location": "...",
    "severity": "...",
    "summary": "...",
    "confidence": 0.0,
    "credible": true,
    "verification_method": "gemini"
}}
"""

    try:

        response = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt
        )

        result = json.loads(
            response.output_text
        )

        return result

    except Exception as error:

        error_text = str(error)

        # ----------------------------------------------------
        # RATE LIMIT / QUOTA
        # ----------------------------------------------------

        if (
            "429" in error_text
            or "rate limit" in error_text.lower()
            or "too_many_requests" in error_text.lower()
            or "quota" in error_text.lower()
        ):

            print(
                "\nGemini quota reached."
                "\nSwitching to deterministic verification "
                "for the remaining incidents."
            )

            GEMINI_AVAILABLE = False

            return fallback_verification(report)

        # ----------------------------------------------------
        # OTHER GEMINI ERROR
        # ----------------------------------------------------

        print(
            f"\nGemini verification failed: {error}"
        )

        return fallback_verification(report)


# ============================================================
# VERIFY ALL REPORTS
# ============================================================

def verify_all_reports(incidents):

    verified_incidents = []

    for report in incidents:

        result = verify_report(report)

        verified_incident = {
            **report,
            **result
        }

        verified_incidents.append(
            verified_incident
        )

    return verified_incidents