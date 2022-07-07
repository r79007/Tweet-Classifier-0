import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Tweet Classifier")

input_sms = st.text_area("Enter the tweet")

if st.button('Predict'):


    transformed_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_sms])

    result = model.predict(vector_input)[0]

    classify = {'angry': 0, 'disgust': 1, 'disgust|angry': 2, 'happy': 3, 'happy|sad': 4, 'happy|surprise': 5,
                'not-relevant': 6, 'sad': 7, 'sad|angry': 8, 'sad|disgust': 9, 'sad|disgust|angry': 10, 'surprise': 11}

    new_dict = dict([(value, key) for key, value in classify.items()])

    st.header(new_dict[result])