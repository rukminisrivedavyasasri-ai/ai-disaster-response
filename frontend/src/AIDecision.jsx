function AIDecision() {
  return (
    <div className="ai-decision">

      <div className="ai-header">
        <span>🧠</span>

        <div>
          <h2>AI Decision Center</h2>
          <p>Autonomous incident analysis</p>
        </div>
      </div>

      <div className="decision-incident">

        <div>
          <span className="decision-label">
            ACTIVE INCIDENT
          </span>

          <h1>INC-001</h1>

          <p>Flood detected in Hyderabad</p>
        </div>

        <span className="critical-badge">
          CRITICAL
        </span>

      </div>

      <div className="confidence">

        <div className="confidence-top">
          <span>AI Confidence</span>
          <strong>91%</strong>
        </div>

        <div className="confidence-bar">
          <div className="confidence-fill"></div>
        </div>

      </div>

      <div className="evidence">

        <h3>Evidence</h3>

        <p>✓ Multiple matching reports</p>
        <p>✓ Sensor confirmation</p>
        <p>✓ High affected population</p>

      </div>

      <div className="ai-action">

        <span>RECOMMENDED ACTION</span>

        <strong>
          🚑 Deploy 2 Ambulances
        </strong>

      </div>

    </div>
  );
}

export default AIDecision;