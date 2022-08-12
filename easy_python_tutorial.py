import streamlit as st

st.set_page_config(page_title="Gabo Loza Lucero Streamlit", layout="centered", initial_sidebar_state="auto")
st.title('Easy tutorial for PYTHON BEGINNERS')

st.write('Simple but effective tips for every python lovers')

st.header('1. Walrus operator')
st.write('The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.')

st.subheader('Example')
walrus_operator = '''Mylist = [1,2,3]
if(list := len(Mylist > 2):
    print(list)'''
st.code(walrus_operator, language='python')

st.subheader('Output')
outputWO = '''3'''
st.code(outputWO, language='python')

st.header('2. Splitting a string')
st.write('If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!')

st.subheader('Example')
string_split = '''string = "hello world"
string.split()'''
st.code(string_split, language='python')

st.subheader('Output')
outputSS = '''['hello', 'world']'''
st.code(outputSS, language='python')

st.header('3. Reversing a string')
st.write('If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.')

st.subheader('Example')
reversing = '''string = "hello world"
a=string[::-1]
print(a)'''
st.code(reversing, language='python')

st.subheader('Output')
outputR = '''dlrow olleh'''
st.code(outputR, language='python')

st.header('4. Merging two dictionaries')
st.write('This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:')

st.subheader('Example')
dictionaries = '''d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)'''
st.code(dictionaries, language='python')

st.subheader('Output')
outputD = '''{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}'''
st.code(outputD, language='python')

st.header('5. The zip() function')
st.write('The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.')

st.subheader('Example')
zipFunction = '''colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)'''
st.code(zipFunction, language='python')

st.subheader('Output')
outputZF = '''{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}'''
st.code(outputZF, language='python')

st.write('The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.')
st.subheader('Example')
zipFunction1 = '''students = [“Rajesh”, “kumar”, “Kriti”]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)'''
st.code(zipFunction1, language='python')

st.subheader('Output')
outputZF1 = '''{‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}'''
st.code(outputZF1, language='python')

st.header('6. Assigning multiple list values to a variable')
st.write('If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique:')

st.subheader('Example')
value = '''mylist = [1,2,3,4,5]
a,*b = mylist
print(f”a =”,a)
print(f”b =”,b)'''
st.code(value, language='python')

st.subheader('Output')
outputV = '''a = 1
b = [2, 3, 4, 5]'''
st.code(outputV, language='python')
