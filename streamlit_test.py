import streamlit as st
import pandas as pd 
import numpy as np 

#df = pd.read_csv('penguins_size.csv')
#st.dataframe(df)

#title = st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)
