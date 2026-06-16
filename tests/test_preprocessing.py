from src.preprocessing import load_and_preprocess_data


def test_data_loading():

    X_train, X_test, y_train, y_test, _ = (
        load_and_preprocess_data(
            "../data/deployment_data_engineered.csv"
        )
    )

    assert X_train.shape[0] > 0
    assert X_test.shape[0] > 0