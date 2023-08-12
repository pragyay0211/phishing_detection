import streamlit as st
import pickle
from preprocessing import get_df
from sklearn.preprocessing import StandardScaler

# Load the model from the pickle file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


st.title('Phishing Detection')

data = st.text_input("Enter The URL Here")

df = get_df(data)

scaler = StandardScaler()
df = scaler.fit_transform(df)

if st.button('Detect'):
    y_pred = model.predict(df)
    if y_pred[0] == 0:
        st.text('Not Phishing')
    else:
        st.text('Phishing')