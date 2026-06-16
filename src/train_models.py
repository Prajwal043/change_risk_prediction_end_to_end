import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

# from lightgbm import LGBMClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from preprocessing import load_and_preprocess_data


X_train, X_test, y_train, y_test, preprocessor = (
    load_and_preprocess_data(
        "../data/deployment_data_engineered.csv"
    )
)

models = {

    "Logistic Regression": None,

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42
    ),

    "XGBoost": XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        random_state=42,
        eval_metric="logloss"
    )
}

results = []

for name, model in models.items():

    if model is None:
        continue

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    y_prob = model.predict_proba(X_test)[:, 1]

    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1": f1_score(y_test, y_pred),
        "ROC_AUC": roc_auc_score(y_test, y_prob)
    })

results_df = pd.DataFrame(results)

print(results_df)

results_df.to_csv(
    "../results/model_comparison.csv",
    index=False
)