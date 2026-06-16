import mlflow
import joblib

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    roc_auc_score
)

from preprocessing import load_and_preprocess_data


X_train, X_test, y_train, y_test, preprocessor = (
    load_and_preprocess_data(
        "../data/deployment_data_engineered.csv"
    )
)

model = joblib.load(
    "../models/best_xgboost.pkl"
)


mlflow.set_tracking_uri(
    "sqlite:///C:/Users/DELL/Documents/brainfuel/projects/change_risk_prediction/change_risk_prediction_end_to_end/src/mlflow.db"
)

mlflow.set_experiment("Deployment Risk Prediction")



with mlflow.start_run() as run:

    y_pred = model.predict(X_test)

    y_prob = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    f1 = f1_score(
        y_test,
        y_pred
    )

    roc_auc = roc_auc_score(
        y_test,
        y_prob
    )

    mlflow.log_param(
        "model_type",
        "XGBoost"
    )

    mlflow.log_param(
        "model_version",
        "v1"
    )

    mlflow.log_metric(
        "accuracy",
        accuracy
    )

    mlflow.log_metric(
        "f1_score",
        f1
    )

    mlflow.log_metric(
        "roc_auc",
        roc_auc
    )

    mlflow.sklearn.log_model(
        sk_model=model,
        name="model"
    )

    # print("Run ID:", run.info.run_id)

    print("Run ID:", mlflow.active_run().info.run_id)

print("Run ID:", run.info.run_id)
print("MLflow run completed.")