import {
  PieChart,
  Pie,
  Cell,
  Tooltip
} from "recharts";

const riskData = [
  { name: "Low", value: 40 },
  { name: "Medium", value: 35 },
  { name: "High", value: 25 }
];

export default function AnalyticsCharts() {

  return (
    <PieChart width={400} height={300}>
      <Pie
        data={riskData}
        dataKey="value"
        nameKey="name"
      />
      <Tooltip />
    </PieChart>
  );
}