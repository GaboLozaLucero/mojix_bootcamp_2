import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gabo Loza Lucero Streamlit", layout="centered", initial_sidebar_state="auto")
st.title('EXERCISE 3 (Inventory Discrepancy)')

st.write('* Remove dups')
st.write('* Aggregate')
st.write('* Merge 2 datasets')

st.subheader('Read two datasets:')
read = '''df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)'''
st.code(read, language='python')

st.subheader('Check your data')
st.write('df expected:')
df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
st.table(df_expected)

st.write('df counted')
df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)
st.table(df_counted)