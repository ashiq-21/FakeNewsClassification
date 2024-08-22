from joblib import load

def load_model():
    model = load('model.pkl')
    vectorizer = load('vectorizer.pkl')
    return model, vectorizer

model, vectorizer = load_model()