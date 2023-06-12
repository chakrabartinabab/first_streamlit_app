import streamlit as st

st.title('My Parents New healthy diner')
st.header('Lunch Menu')
st.text('Luchi')
st.text('Aloo dum')
st.text('ghugni')

st.title("my smoothie")

# adding a new dataframe to the application page
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# Let's put a pick list here so they can pick the fruit they want to include 
st.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
st.dataframe(my_fruit_list)
