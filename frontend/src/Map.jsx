import {
  MapContainer,
  TileLayer,
  Marker,
  Popup
} from "react-leaflet";

import "leaflet/dist/leaflet.css";

function Map() {

  const incidents = [
    {
      id: "INC-001",
      type: "Flood",
      severity: "Critical",
      confidence: 91,
      latitude: 17.385,
      longitude: 78.4867
    },
    {
      id: "INC-002",
      type: "Fire",
      severity: "High",
      confidence: 86,
      latitude: 17.400,
      longitude: 78.490
    },
    {
      id: "INC-003",
      type: "Flood",
      severity: "Medium",
      confidence: 78,
      latitude: 17.370,
      longitude: 78.475
    }
  ];

  return (
    <MapContainer
      center={[17.385, 78.4867]}
      zoom={12}
      style={{ height: "400px", width: "100%" }}
    >

      <TileLayer
        attribution="&copy; OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {incidents.map((incident) => (
        <Marker
          key={incident.id}
          position={[
            incident.latitude,
            incident.longitude
          ]}
        >
          <Popup>

            <strong>{incident.type}</strong>

            <br />

            Incident: {incident.id}

            <br />

            Severity: {incident.severity}

            <br />

            Confidence: {incident.confidence}%

          </Popup>
        </Marker>
      ))}

    </MapContainer>
  );
}

export default Map;