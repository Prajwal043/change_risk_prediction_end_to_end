export default function MetricsCards({ stats }) {
  return (
    <div
      style={{
        display: "flex",
        gap: "20px",
        marginBottom: "20px",
      }}
    >
      <div
        style={{
          flex: 1,
          padding: "20px",
          border: "1px solid #ddd",
          borderRadius: "10px",
          background: "#fff",
        }}
      >
        <h3>Total Deployments</h3>
        <h2>{stats.totalDeployments}</h2>
      </div>

      <div
        style={{
          flex: 1,
          padding: "20px",
          border: "1px solid #ddd",
          borderRadius: "10px",
          background: "#fff",
        }}
      >
        <h3>Average Risk</h3>
        <h2>{stats.averageRisk}%</h2>
      </div>

      <div
        style={{
          flex: 1,
          padding: "20px",
          border: "1px solid #ddd",
          borderRadius: "10px",
          background: "#fff",
        }}
      >
        <h3>Failure Rate</h3>
        <h2>{stats.failureRate}%</h2>
      </div>
    </div>
  );
}