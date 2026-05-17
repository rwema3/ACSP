import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/processed_features.csv")
df["risk_score"].hist()
plt.show()