import pandas as pd

df = pd.read_csv("../data/raw_transactions.csv")
df.head()
df.describe()