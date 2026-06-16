import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)


def load_and_preprocess_data(filepath):

    df = pd.read_csv(filepath)

    X = df.drop(
        columns=["change_failed"]
    )

    y = df["change_failed"]

    numerical_features = [
        "systems_impacted",
        "num_files_changed",
        "deployment_hour",
        "engineer_experience",
        "historical_failures",
        "dependency_count",
        "rollback_required",
        "test_coverage",
        "complexity_score",
        "after_hours",
        "weekend_deployment"
    ]

    categorical_features = [
        "deployment_day",
        "change_type"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                StandardScaler(),
                numerical_features
            ),
            (
                "cat",
                OneHotEncoder(
                    handle_unknown="ignore"
                ),
                categorical_features
            )
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    X_train = preprocessor.fit_transform(
        X_train
    )

    X_test = preprocessor.transform(
        X_test
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor
    )