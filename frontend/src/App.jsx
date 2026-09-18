import "./App.css";

function App() {
  return (
    <div className="dashboard">

      {/* HEADER */}
      <header className="header">
        <div>
          <h1>🚨 AI Disaster Response Center</h1>
          <p>Real-time autonomous emergency coordination</p>
        </div>

        <div className="status">
          🟢 System Active
        </div>
      </header>


      {/* STATISTICS */}
      <section className="stats">

        <div className="stat-card">
          <p>Total Incidents</p>
          <h2>8</h2>
        </div>

        <div className="stat-card critical">
          <p>Critical Incidents</p>
          <h2>2</h2>
        </div>

        <div className="stat-card">
          <p>Ambulances</p>
          <h2>3 / 5</h2>
        </div>

        <div className="stat-card">
          <p>Rescue Teams</p>
          <h2>2 / 3</h2>
        </div>

      </section>


      {/* MAIN CONTENT */}
      <section className="main-grid">

        {/* MAP */}
        <div className="panel map-panel">

          <h2>🗺️ Disaster Map</h2>

          <div className="map-placeholder">
            <div className="map-message">
              <span>🗺️</span>
              <h3>Disaster Monitoring Map</h3>
              <p>Incident locations will appear here</p>

              <div className="markers">
                🔴 &nbsp; Critical &nbsp;&nbsp;
                🟠 &nbsp; High &nbsp;&nbsp;
                🟡 &nbsp; Medium
              </div>
            </div>
          </div>

        </div>


        {/* INCIDENTS */}
        <div className="panel">

          <h2>🚨 Active Incidents</h2>

          <div className="incident">
            <div>
              <h3>Flood</h3>
              <p>INC-001</p>
            </div>

            <span className="badge critical-badge">
              CRITICAL
            </span>

            <p>Confidence: 91%</p>
          </div>


          <div className="incident">
            <div>
              <h3>Fire</h3>
              <p>INC-002</p>
            </div>

            <span className="badge high-badge">
              HIGH
            </span>

            <p>Confidence: 86%</p>
          </div>


          <div className="incident">
            <div>
              <h3>Flood</h3>
              <p>INC-003</p>
            </div>

            <span className="badge medium-badge">
              MEDIUM
            </span>

            <p>Confidence: 78%</p>
          </div>

        </div>

      </section>


      {/* RESOURCES */}
      <section className="panel">

        <h2>🚑 Resource Status</h2>

        <div className="resources">

          <div className="resource">
            <h3>🚑 Ambulances</h3>
            <h2>3 / 5</h2>
            <p>2 available</p>
          </div>

          <div className="resource">
            <h3>🧑‍🚒 Rescue Teams</h3>
            <h2>2 / 3</h2>
            <p>1 available</p>
          </div>

          <div className="resource">
            <h3>🏠 Shelters</h3>
            <h2>2</h2>
            <p>Available</p>
          </div>

        </div>

      </section>


      {/* AGENT ACTIVITY */}
      <section className="panel">

        <h2>🤖 Agent Activity</h2>

        <div className="agent">

          <div>✓</div>

          <div>
            <strong>Verification Agent</strong>
            <p>3 reports merged</p>
          </div>

        </div>


        <div className="agent">

          <div>✓</div>

          <div>
            <strong>Verification Agent</strong>
            <p>Conflict detected in severity reports</p>
          </div>

        </div>


        <div className="agent">

          <div>✓</div>

          <div>
            <strong>Priority Agent</strong>
            <p>INC-001 marked as CRITICAL</p>
          </div>

        </div>


        <div className="agent">

          <div>✓</div>

          <div>
            <strong>Resource Agent</strong>
            <p>2 ambulances allocated to INC-001</p>
          </div>

        </div>


        <div className="agent">

          <div>✓</div>

          <div>
            <strong>Coordinator</strong>
            <p>Response plan updated</p>
          </div>

        </div>

      </section>

    </div>
  );
}

export default App;