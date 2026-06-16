from fastapi import FastAPI
from pydantic import BaseModel

from sqlalchemy import text
from database import engine

import joblib
import pandas as pd


app = FastAPI()

model = joblib.load(
    "models/best_xgboost.pkl"
)

preprocessor = joblib.load(
    "models/preprocessor.pkl"
)


class DeploymentRequest(BaseModel):

    systems_impacted: int
    num_files_changed: int
    deployment_hour: int
    deployment_day: str
    engineer_experience: int
    historical_failures: int
    dependency_count: int
    rollback_required: int
    test_coverage: int
    change_type: str


@app.post("/predict")
def predict(request: DeploymentRequest):

    data = pd.DataFrame([request.dict()])

    data["complexity_score"] = (
        data["systems_impacted"]
        * data["dependency_count"]
    )

    data["after_hours"] = (
        data["deployment_hour"] > 18
    ).astype(int)

    data["weekend_deployment"] = (
        data["deployment_day"]
        .isin(["Saturday", "Sunday"])
    ).astype(int)

    X = preprocessor.transform(data)

    probability = model.predict_proba(X)[0][1]

    risk = (
        "HIGH"
        if probability > 0.7
        else "LOW"
    )



    with engine.connect() as conn:

        conn.execute(
            text(
                """
                INSERT INTO deployments
                (
                    risk_score,
                    prediction
                )
                VALUES
                (
                    :risk_score,
                    :prediction
                )
                """
            ),
            {
                "risk_score": float(probability),
                "prediction": risk
            }
        )

        conn.commit()

    return {
        "risk_score": round(
            float(probability),
            2
        ),
        "risk": risk
    }