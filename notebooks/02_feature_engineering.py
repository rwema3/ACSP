df["transaction_score"] = df["monthly_transactions"] * df["avg_transaction"]
df["risk_score"] = 1 - df["savings_score"]