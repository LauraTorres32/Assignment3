import streamlit as st
import pickle
import pandas as pd

st.title('Sales Prediction advertising')
st.write('This web app predicts the **sales** in the advertising media')

# to read the model from the pickle file
model=pickle.load(open('Assignment3ADV.pkl','rb'))

# get the input from the user
TV=st.number_input('TV')
Radio=st.number_input('Radio')
Newspaper=st.number_input('Newspaper')

# convert the user input to a dataframe
user_data=pd.DataFrame({'TV':TV,
    'Radio':Radio,
    'Newspaper':Newspaper}, index=[0])

# predict the house price
prediction=model.predict(user_data)

if st.button('Predict'):
    st.write(f'The predicted sales is {prediction[0]}')