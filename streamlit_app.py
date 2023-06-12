import streamlit as st

st.title('My Parents New healthy diner')
st.header('Lunch Menu')
st.text('Luchi')
st.text('Aloo dum')
st.text('ghugni')

# adding a new dataframe to the application page
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
