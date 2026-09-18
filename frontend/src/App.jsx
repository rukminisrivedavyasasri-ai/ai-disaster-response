import "./App.css";
import Map from "./Map";
import IncidentList from "./IncidentList";
import Resources from "./Resources";
import AgentActivity from "./AgentActivity";
import DemoSimulation from "./DemoSimulation";

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

  <div className="map-container">
    <Map />
  </div>

  <div className="markers">
    🔴 &nbsp; Critical &nbsp;&nbsp;
    🟠 &nbsp; High &nbsp;&nbsp;
    🟡 &nbsp; Medium
  </div>

</div>


        {/* INCIDENTS */}
        
<div className="panel">

  <h2>🚨 Active Incidents</h2>

  <IncidentList />

</div>

      </section>


      {/* RESOURCES */}
      <Resources />
{/* SIMULATION */}
<DemoSimulation />

      {/* AGENT ACTIVITY */}
      <AgentActivity />
    </div>
  );
}

export default App;