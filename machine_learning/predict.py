import pickle
from machine_learning.utlis import preprocess_text

with open('./machine_learning/models/multinomialnb.pkl', 'rb') as f:
    model = pickle.load(f)

with open('./machine_learning/models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def predict(text):
    test_preprocessed = preprocess_text(text)
    vec_test = vectorizer.transform([text])

    proba = model.predict_proba(vec_test)
    predicted = model.predict(vec_test)
    return predicted[0], proba[0][0]


if __name__ == "__main__":
    test = "Delivery reminder: the package is too large for the mailbox. Please choose a redelivery option via https://901758.reception-livreur.com"
    predicted, score = predict(test)

    result = {
        1: 'Spam',
        0: 'Not Spam',
    }

    print(f"model predict: {result[predicted]}")
    print(f"model predict: {score}")