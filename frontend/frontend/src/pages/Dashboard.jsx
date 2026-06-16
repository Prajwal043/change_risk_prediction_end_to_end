import MetricsCards from "../components/MetricsCards";
import PredictionForm from "../components/PredictionForm";
import AnalyticsCharts from "../components/AnalyticsCharts";

export default function Dashboard() {
  const stats = {
    totalDeployments: 1000,
    averageRisk: 37,
    failureRate: 12,
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Change Risk Prediction Dashboard</h1>

      <MetricsCards stats={stats} />

      <br />

      <PredictionForm />

      <br />

      <AnalyticsCharts />
    </div>
  );
}