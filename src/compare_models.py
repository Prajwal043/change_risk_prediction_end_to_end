import pandas as pd

comparison = pd.read_csv(
    "../results/model_comparison.csv"
)

comparison = comparison.sort_values(
    by="ROC_AUC",
    ascending=False
)

print(comparison)

print("\nBest Model:")
print(comparison.iloc[0])