import streamlit as st

st.set_page_config(layout="wide")
st.title('Easy tutorial for PYTHON BEGINNERS')

st.write('Simple but effective tips for every python lovers')

st.subheader('1. Walrus operator')
st.text('The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat's house")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
