import { useState } from "react";

function DemoSimulation() {
  const [status, setStatus] = useState("System ready");
  const [running, setRunning] = useState(false);

  const runSimulation = () => {
    setRunning(true);
    setStatus("📡 New emergency report received...");

    setTimeout(() => {
      setStatus("🔍 Verification Agent analyzing reports...");
    }, 1500);

    setTimeout(() => {
      setStatus("⚠️ Priority Agent classifying incident...");
    }, 3000);

    setTimeout(() => {
      setStatus("🚑 Resource Agent allocating resources...");
    }, 4500);

    setTimeout(() => {
      setStatus("🤖 Coordinator updating response plan...");
    }, 6000);

    setTimeout(() => {
      setStatus("✅ Emergency response plan updated");
      setRunning(false);
    }, 7500);
  };

  return (
    <div className="demo-panel">
      <div>
        <h2>🚨 Emergency Simulation</h2>
        <p>{status}</p>
      </div>

      <button
        className="simulate-btn"
        onClick={runSimulation}
        disabled={running}
      >
        {running ? "🤖 Agents Processing..." : "🚨 Simulate New Emergency"}
      </button>
    </div>
  );
}

export default DemoSimulation;