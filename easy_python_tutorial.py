import streamlit as st

st.set_page_config(layout="wide")
st.title('Easy tutorial for PYTHON BEGINNERS')

st.write('Simple but effective tips for every python lovers')

st.header('1. Walrus operator')
st.text_area('The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')

st.subheader('Example')
walrus_operator = '''Mylist = [1,2,3]
if(list := len(Mylist > 2):
    print(list)'''
st.code(walrus_operator, language='python')

st.subheader('Output')
outputWO = '''3'''
st.code(outputWO, language='python')

st.header('2. Splitting a string')
st.text_area('If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!')

st.subheader('Example')
string_split = '''string = "hello world"
string.split()'''
st.code(string_split, language='python')

st.subheader('Output')
outputSS = '''['hello', 'world']'''
st.code(outputSS, language='python')

st.header('3. Reversing a string')
st.text_area('If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.')

st.subheader('Example')
reversing = '''string = "hello world"
a=string[::-1]
print(a)'''
st.code(reversing, language='python')

st.subheader('Output')
outputR = '''['hello', 'world']'''
st.code(outputR, language='python')
