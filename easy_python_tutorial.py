import streamlit as st
from PIL import Image

image = Image.open('https://miro.medium.com/max/875/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg')

st.set_page_config(page_title="Gabo Loza Lucero Streamlit", layout="centered", initial_sidebar_state="auto")
st.title('Easy tutorial for PYTHON BEGINNERS')

st.write('Simple but effective tips for every python lovers')

st.image(image, caption='I hope this works')
st.write('The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.')
st.write('In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.')

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
st.write('This process is also called list unpacking and you can apply this method for more than 2 variables also!')

st.header('7. Remove duplicate list items')
st.write('Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.')

st.subheader('Example')
double = '''mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)'''
st.code(double, language='python')

st.subheader('Output')
outputD = '''{1, 2, 3, 4, 5, 6, 7, 8, 9}'''
st.code(outputD, language='python')

st.header('8. Lambda Function')
st.write('If you need a function that is not very complicated, it can be done easily in one line using lambda. They are also called anonymous functions and are used heavily in data science and web development.')

st.subheader('Example')
st.write('Let’s say you want to write a function to multiply two numbers. Instead of writing a conventional function, you can do that in one line using :')
lambdaF = '''mul = lambda a,b: a*b
mul(5,6)'''
st.code(lambdaF, language='python')

st.subheader('Output')
outputLF = '''30'''
st.code(outputLF, language='python')

st.header('9. Swapping variable value')
st.write('One of the first programs that we learn while learning about variables is swapping the values of two variables. In python you can achieve that with one line of code:')

st.subheader('Example')
sqap = '''a = 100
b = 200
a,b = b,a
print(f’a = ‘,a)
print(f’b = ‘,b)'''
st.code(sqap, language='python')

st.subheader('Output')
outputS = '''a = 200
b = 100'''
st.code(outputS, language='python')

st.header('10. Use a passwoird in your code')
st.write('This python trick is amazing for securing your code with a password. We will use the getpass() function from the library getpass which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!')

st.subheader('Example')
password = '''from getpass import getpass
password = getpass(“password: “)
if password == “abcd”:
    print(“welcome strnger!”)
else:
    print(“wrong password”)'''
st.code(password, language='python')

st.subheader('Output')
outputP = '''password: **** [abcd]
Welcome stranger!
Password: **** [abdc]
Wrong password'''
st.code(outputP, language='python')

st.header('Conclusion')
st.write('These were a few amazing Python tips and tricks which will make your work a lot easier while coding. There are many more shortcuts like these that you can explore from the official documentation or any other website.')
st.write('Note: This article contains an affiliate link. This means that if you click on it and choose to buy the resource I linked above, a small portion of your subscription fee will go to me.')
st.write('However, the recommended resource is experienced by me and helped me in my data science career journey.')
