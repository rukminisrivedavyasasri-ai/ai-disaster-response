function Resources() {
  return (
    <section className="panel resources-panel">

      <div className="section-title">
        <div>
          <h2>🚑 Resource Status</h2>
          <p>Current emergency response capacity</p>
        </div>
      </div>

      <div className="resource-status-grid">

        <div className="resource-status-card">

          <div className="resource-icon">
            🚑
          </div>

          <div className="resource-info">
            <span>AMBULANCES</span>
            <strong>3 / 5</strong>
            <small>2 available</small>
          </div>

          <div className="resource-dots">
            ● ● ● ○ ○
          </div>

        </div>


        <div className="resource-status-card">

          <div className="resource-icon">
            🧑‍🚒
          </div>

          <div className="resource-info">
            <span>RESCUE TEAMS</span>
            <strong>2 / 3</strong>
            <small>1 available</small>
          </div>

          <div className="resource-dots">
            ● ● ○
          </div>

        </div>


        <div className="resource-status-card">

          <div className="resource-icon">
            🏠
          </div>

          <div className="resource-info">
            <span>SHELTERS</span>
            <strong>2</strong>
            <small>Available</small>
          </div>

          <div className="resource-available">
            AVAILABLE
          </div>

        </div>

      </div>

    </section>
  );
}

export default Resources;