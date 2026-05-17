import pickle

with open("credit_model.pkl", "wb") as f:
    pickle.dump(model, f)