import pickle

with open('params.pickle', 'rb') as f:  # Python 3: open(..., 'rb')
    selected_features, w1, w2, n_hidden, lambdaval = pickle.load(f)
    
print("\n Selected Features:\n", selected_features)
print("\n W1:", w1)
print("\n W2:", w2)
print("\n Hidden nodes:", n_hidden)
print("\n Lambda Value:", lambdaval)
