# from src.preprocessing import load_and_preprocess_data


# def test_data_loading():

#     X_train, X_test, y_train, y_test, _ = (
#         load_and_preprocess_data(
#             "../data/deployment_data_engineered.csv"
#         )
#     )

#     assert X_train.shape[0] > 0
#     assert X_test.shape[0] > 0

from pathlib import Path
from src.preprocessing import load_and_preprocess_data

def test_data_loading():
    data_file = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "deployment_data_engineered.csv"
    )

    X_train, X_test, y_train, y_test, _ = (
        load_and_preprocess_data(str(data_file))
    )

    assert X_train.shape[0] > 0
    assert X_test.shape[0] > 0