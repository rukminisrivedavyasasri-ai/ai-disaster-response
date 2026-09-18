function AgentActivity() {
  const activities = [
    "Verification Agent — 3 reports merged",
    "Verification Agent — Conflict detected",
    "Priority Agent — INC-001 marked CRITICAL",
    "Resource Agent — 2 ambulances allocated",
    "Coordinator — Response plan updated"
  ];

  return (
    <div className="agent-panel">
      <h2>🤖 Agent Activity</h2>

      {activities.map((activity, index) => (
        <div className="agent-item" key={index}>
          ✓ {activity}
        </div>
      ))}
    </div>
  );
}

export default AgentActivity;