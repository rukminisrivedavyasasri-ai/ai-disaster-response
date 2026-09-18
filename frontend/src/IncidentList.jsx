function IncidentList() {
  const incidents = [
    {
      id: "INC-001",
      type: "Flood",
      severity: "Critical",
      confidence: 91
    },
    {
      id: "INC-002",
      type: "Fire",
      severity: "High",
      confidence: 86
    },
    {
      id: "INC-003",
      type: "Flood",
      severity: "Medium",
      confidence: 78
    }
  ];

  return (
    <div className="incident-cards">

      {incidents.map((incident) => (

        <div
          className={`incident-card ${incident.severity.toLowerCase()}`}
          key={incident.id}
        >

          <div className="incident-card-top">

            <span className="incident-id">
              {incident.id}
            </span>

            <span
              className={`badge ${
                incident.severity === "Critical"
                  ? "critical-badge"
                  : incident.severity === "High"
                  ? "high-badge"
                  : "medium-badge"
              }`}
            >
              {incident.severity.toUpperCase()}
            </span>

          </div>

          <h3>{incident.type}</h3>

          <div className="incident-confidence">
            <span>Confidence</span>
            <strong>{incident.confidence}%</strong>
          </div>

          <div className="mini-confidence-bar">
            <div
              style={{
                width: `${incident.confidence}%`
              }}
            ></div>
          </div>

        </div>

      ))}

    </div>
  );
}

export default IncidentList;