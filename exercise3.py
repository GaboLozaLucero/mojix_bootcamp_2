import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gabo Loza Lucero Streamlit", layout="centered", initial_sidebar_state="collapsed")
st.title('EXERCISE 3 (Inventory Discrepancy)')

st.write('* Remove dups')
st.write('* Aggregate')
st.write('* Merge 2 datasets')

st.subheader('Read two datasets:')
read = '''df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)'''
st.code(read, language='python')

st.subheader('Check your data')
st.write('df_expected:')
df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
st.dataframe(df_expected)

st.write('df_counted')
df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)
st.dataframe(df_counted)

st.subheader('Remove duplicated data and rename to show real quantity')
df_counted = df_counted.drop_duplicates("RFID")
df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
duplicates = '''df_counted = df_counted.drop_duplicates("RFID")
df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})'''
st.code(duplicates, language='python')
st.dataframe(df_B)

st.subheader('Aggregate info')
st.write('Select and show rows by retail info')
rows_selected = ["Retail_Product_Color",
"Retail_Product_Level1",
"Retail_Product_Level1Name",
"Retail_Product_Level2Name",
"Retail_Product_Level3Name",
"Retail_Product_Level4Name",
"Retail_Product_Name",
"Retail_Product_SKU",
"Retail_Product_Size",
"Retail_Product_Style",
"Retail_SOHQTY"]
df_A = df_expected[rows_selected]
retail_info = '''rows_selected = ["Retail_Product_Color",
"Retail_Product_Level1",
"Retail_Product_Level1Name",
"Retail_Product_Level2Name",
"Retail_Product_Level3Name",
"Retail_Product_Level4Name",
"Retail_Product_Name",
"Retail_Product_SKU",
"Retail_Product_Size",
"Retail_Product_Style",
"Retail_SOHQTY"]
df_A = df_expected[rows_selected]'''
st.code(retail_info, language='python')
st.dataframe(df_A)

st.subheader('Time to merge')
df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True)
merging = '''df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True)'''
st.code(merging, language='python')
st.dataframe(df_discrepancy)

df_discrepancy["Retail_SOHQTY"] = df_discrepancy["Retail_SOHQTY"].fillna(0).astype(int)
df_discrepancy["Diff"] = df_discrepancy["Retail_CCQTY"] - df_discrepancy["Retail_SOHQTY"]

df_discrepancy.loc[df_discrepancy["Diff"]<0, "Unders"] = df_discrepancy["Diff"] * (-1)
df_discrepancy["Unders"] = df_discrepancy["Unders"].fillna(0).astype(int)

st.subheader('Now we check our new info')
st.write('These products need RFID as soon as possible')
#st.write('Product Level 1 Name:')
#df_size = df_discrepancy.groupby("Retail_Product_Size").sum()
#st.bar_chart(df_size.head())
df_unders = df_discrepancy.groupby(["Diff", "Retail_Product_Name"]).sum()
#st.dataframe(df_unders)

need = df_unders.head(5)
#need.drop('', inplace=True, axis=1)
st.dataframe(need)
#st.bar_chart(pd.DataFrame(need))


