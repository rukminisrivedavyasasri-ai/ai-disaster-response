import { useState } from "react";

function AgentActivity() {
  const [activeAgent, setActiveAgent] = useState("Verification Agent");

  const agents = [
    {
      name: "Verification Agent",
      icon: "🔍",
      status: "MONITORING",
      metric: "12",
      metricLabel: "Reports analyzed",
    },
    {
      name: "Priority Agent",
      icon: "⚠️",
      status: "READY",
      metric: "3",
      metricLabel: "Critical incidents",
    },
    {
      name: "Resource Agent",
      icon: "🚑",
      status: "READY",
      metric: "5",
      metricLabel: "Resources tracked",
    },
  ];

  const activity = [
    {
      time: "11:42:08",
      agent: "Verification",
      icon: "🔍",
      message: "Report validated",
      type: "verified",
    },
    {
      time: "11:41:36",
      agent: "Priority",
      icon: "⚠️",
      message: "INC-001 marked CRITICAL",
      type: "critical",
    },
    {
      time: "11:40:52",
      agent: "Resource",
      icon: "🚑",
      message: "2 ambulances assigned",
      type: "resource",
    },
    {
      time: "11:39:41",
      agent: "Verification",
      icon: "🔍",
      message: "Duplicate report detected",
      type: "verified",
    },
  ];

  return (
    <section className="agent-console">

      {/* HEADER */}
      <div className="agent-console-header">

        <div>
          <div className="agent-title">
            <span className="agent-title-icon">🧠</span>

            <div>
              <h2>AI Agent Activity</h2>
              <p>
                Autonomous agents coordinating disaster response
              </p>
            </div>
          </div>
        </div>

        <div className="agent-system-status">
          <span className="agent-live-dot"></span>
          SYSTEM ACTIVE
        </div>

      </div>


      {/* AGENT CARDS */}
      <div className="agent-cards">

        {agents.map((agent) => (
          <div
            key={agent.name}
            className={`agent-card ${
              activeAgent === agent.name ? "agent-card-active" : ""
            }`}
            onClick={() => setActiveAgent(agent.name)}
          >

            <div className="agent-card-top">

              <div className="agent-card-icon">
                {agent.icon}
              </div>

              <span className="agent-status">
                <span className="mini-live-dot"></span>
                {agent.status}
              </span>

            </div>

            <h3>{agent.name}</h3>

            <div className="agent-card-bottom">

              <div>
                <strong>{agent.metric}</strong>
                <span>{agent.metricLabel}</span>
              </div>

              <span className="agent-arrow">→</span>

            </div>

          </div>
        ))}

      </div>


      {/* COORDINATOR */}
      <div className="coordinator-bar">

        <div className="coordinator-left">

          <div className="coordinator-icon">
            🤖
          </div>

          <div>
            <span className="coordinator-label">
              ORCHESTRATOR
            </span>

            <strong>Coordinator Agent</strong>

            <p>
              Combining agent decisions and updating response plans
            </p>
          </div>

        </div>

        <div className="coordinator-status">
          <span></span>
          AUTONOMOUS
        </div>

      </div>


      {/* LIVE INTELLIGENCE */}
      <div className="intelligence-section">

        <div className="intelligence-header">

          <div>
            <h3>Live Intelligence</h3>
            <p>Recent autonomous agent decisions</p>
          </div>

          <span className="live-label">
            ● LIVE
          </span>

        </div>


        <div className="activity-feed">

          {activity.map((item, index) => (
            <div
              className="activity-row"
              key={index}
            >

              <span className="activity-time">
                {item.time}
              </span>

              <div className={`activity-icon ${item.type}`}>
                {item.icon}
              </div>

              <div className="activity-content">

                <strong>
                  {item.agent} Agent
                </strong>

                <span>
                  {item.message}
                </span>

              </div>

              <span className="activity-check">
                ✓
              </span>

            </div>
          ))}

        </div>

      </div>

    </section>
  );
}

export default AgentActivity;