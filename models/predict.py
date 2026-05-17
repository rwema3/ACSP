def predict_score(transactions, savings):
    score = transactions * savings

    if score > 30:
        return "Low Risk"
    elif score > 10:
        return "Medium Risk"
    return "High Risk"