import streamlit as st

st.set_page_config(layout="wide")
st.title('Easy tutorial for PYTHON BEGINNERS')

st.write('Simple but effective tips for every python lovers')

st.header('1. Walrus operator')
st.text('''The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value \n to a variable within an expression like conditional statements, loops, etc.''')

st.subheader('Example')
walrus_operator = '''Mylist = [1,2,3]
if(list := len(Mylist > 2):
    print(list)'''
st.code(walrus_operator, language='python')

st.subheader('Output')
outputWO = '''3'''
st.code(outputWO, language='python')
