import streamlit as st

st.title('My Parents New healthy diner')
st.header('Lunch Menu')
st.text('Luchi')
st.text('Aloo dum')
st.text('ghugni')
st.title("My smoothie")

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Orange','Cherries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
