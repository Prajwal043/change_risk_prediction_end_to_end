import { useState } from "react";

export default function PredictionForm() {
  const [form, setForm] = useState({
    systems_impacted: 12,
    num_files_changed: 30,
    dependency_count: 5,
    test_coverage: 65,
  });

  const [result, setResult] = useState(null);

  const predict = () => {
    let riskScore = 0;
    let riskLevel = "LOW";

    // Simple hardcoded risk logic for demo purposes
    if (
      form.dependency_count >= 7 ||
      form.test_coverage < 70 ||
      form.systems_impacted > 10
    ) {
      riskScore = 0.79;
      riskLevel = "HIGH";
    } else if (
      form.dependency_count >= 4 ||
      form.test_coverage < 85
    ) {
      riskScore = 0.52;
      riskLevel = "MEDIUM";
    } else {
      riskScore = 0.21;
      riskLevel = "LOW";
    }

    setResult({
      risk_score: riskScore,
      risk: riskLevel,
    });
  };

  return (
    <div
      style={{
        padding: "20px",
        backgroundColor: "#fff",
        borderRadius: "10px",
        boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
        marginTop: "20px",
      }}
    >
      <h2>Deployment Risk Prediction</h2>

      <div style={{ marginBottom: "15px" }}>
        <label>Systems Impacted</label>
        <br />
        <input
          type="number"
          value={form.systems_impacted}
          onChange={(e) =>
            setForm({
              ...form,
              systems_impacted: Number(e.target.value),
            })
          }
          style={{ width: "100%", padding: "8px" }}
        />
      </div>

      <div style={{ marginBottom: "15px" }}>
        <label>Files Changed</label>
        <br />
        <input
          type="number"
          value={form.num_files_changed}
          onChange={(e) =>
            setForm({
              ...form,
              num_files_changed: Number(e.target.value),
            })
          }
          style={{ width: "100%", padding: "8px" }}
        />
      </div>

      <div style={{ marginBottom: "15px" }}>
        <label>Dependencies</label>
        <br />
        <input
          type="number"
          value={form.dependency_count}
          onChange={(e) =>
            setForm({
              ...form,
              dependency_count: Number(e.target.value),
            })
          }
          style={{ width: "100%", padding: "8px" }}
        />
      </div>

      <div style={{ marginBottom: "15px" }}>
        <label>Test Coverage (%)</label>
        <br />
        <input
          type="number"
          value={form.test_coverage}
          onChange={(e) =>
            setForm({
              ...form,
              test_coverage: Number(e.target.value),
            })
          }
          style={{ width: "100%", padding: "8px" }}
        />
      </div>

      <button
        onClick={predict}
        style={{
          padding: "10px 20px",
          backgroundColor: "#1976d2",
          color: "white",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Predict
      </button>

      {result && (
        <div
          style={{
            marginTop: "20px",
            padding: "15px",
            border: "1px solid #ddd",
            borderRadius: "8px",
          }}
        >
          <h3>
            Failure Probability:{" "}
            {(result.risk_score * 100).toFixed(0)}%
          </h3>

          <h2
            style={{
              color:
                result.risk === "HIGH"
                  ? "red"
                  : result.risk === "MEDIUM"
                  ? "orange"
                  : "green",
            }}
          >
            Risk Level: {result.risk}
          </h2>

          <h4>Top Risk Factors</h4>
          <ul>
            {result.risk === "HIGH" && (
              <>
                <li>High dependency count</li>
                <li>Low test coverage</li>
                <li>Large deployment scope</li>
              </>
            )}

            {result.risk === "MEDIUM" && (
              <>
                <li>Moderate dependency count</li>
                <li>Average test coverage</li>
              </>
            )}

            {result.risk === "LOW" && (
              <>
                <li>Good test coverage</li>
                <li>Low deployment complexity</li>
              </>
            )}
          </ul>
        </div>
      )}
    </div>
  );
}