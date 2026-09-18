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
    <div>

      {incidents.map((incident) => (

        <div className="incident" key={incident.id}>

          <div>
            <h3>{incident.type}</h3>
            <p>{incident.id}</p>
          </div>

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

          <p>
            Confidence: {incident.confidence}%
          </p>

        </div>

      ))}

    </div>
  );
}

export default IncidentList;