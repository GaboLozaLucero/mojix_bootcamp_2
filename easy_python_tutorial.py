import streamlit as st

st.set_page_config(layout="wide")
st.title('Easy tutorial for PYTHON BEGINNERS')

st.write('Simple but effective tips for every python lovers')

st.header('1. Walrus operator')
st.text('The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that')
st.text('lets you assign value to a variable within an expression like conditional statements, loops, etc.')

st.subheader('Example')
code = '''Mylist = [1,2,3]
if(1 := len(Mylist > 2):
    print(1)'''
st.code(code, language='python')

