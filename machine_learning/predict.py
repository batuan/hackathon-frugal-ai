import pickle
from machine_learning.utlis import preprocess_text

with open('./machine_learning/models/classification_model.pkl', 'rb') as f:
    model_message = pickle.load(f)

with open('./machine_learning/models/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('./machine_learning/models/classification_model_sender.pkl', 'rb') as f:
    model_email = pickle.load(f)

def predict(text):
    test_preprocessed = preprocess_text(text)
    vec_test = vectorizer.transform([test_preprocessed])

    proba = model_message.predict_proba(vec_test)
    predicted = model_message.predict(vec_test)
    return predicted[0], proba[0][0]

def predict_email(text):
    test_preprocessed = preprocess_text(text)
    vec_test = vectorizer.transform([test_preprocessed])
    predicted = model_email.predict(vec_test)
    proba = model_message.predict_proba(vec_test)

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