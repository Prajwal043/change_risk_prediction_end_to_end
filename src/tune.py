import joblib

from xgboost import XGBClassifier

from sklearn.model_selection import RandomizedSearchCV

from sklearn.metrics import (
    roc_auc_score,
    f1_score
)

from preprocessing import load_and_preprocess_data


X_train, X_test, y_train, y_test, preprocessor = (
    load_and_preprocess_data(
        "../data/deployment_data_engineered.csv"
    )
)

model = XGBClassifier(
    random_state=42,
    eval_metric="logloss"
)

param_grid = {
    "n_estimators": [100, 200, 300, 500],
    "max_depth": [3, 4, 5, 6, 8, 10],
    "learning_rate": [0.01, 0.05, 0.1, 0.2, 0.3]
}

search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_grid,
    n_iter=20,
    scoring="roc_auc",
    cv=5,
    verbose=2,
    random_state=42,
    n_jobs=-1
)

search.fit(X_train, y_train)

best_model = search.best_estimator_

y_pred = best_model.predict(X_test)

y_prob = best_model.predict_proba(X_test)[:, 1]

print("Best Parameters:")
print(search.best_params_)

print("\nF1 Score:")
print(f1_score(y_test, y_pred))

print("\nROC AUC:")
print(roc_auc_score(y_test, y_prob))

joblib.dump(
    best_model,
    "../models/best_xgboost.pkl"
)

joblib.dump(
    preprocessor,
    "../models/preprocessor.pkl"
)

print("\nBest model saved.")