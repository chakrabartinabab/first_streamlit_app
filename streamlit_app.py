import streamlit as st
from urllib.error import URLError
import pandas
import requests
import snowflake.connector


st.title('My Parents New healthy diner')
st.header('Lunch Menu')
st.text('Luchi')
st.text('Aloo dum')
st.text('ghugni')
st.title("My smoothie")

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Orange','Cherries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)

# new section
st.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = st.text_input('What fruit would you like information about?')
   if not fruit_choice:
    st.error("Please select a fruit to get information.")
   else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "fruit_choice")
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    st.dataframe(fruityvice_normalized)

except URLError as e:
   st.error()
#import requests

#st.text(fruityvice_response.json())--commenting it out to remove from output screen

# normalizing the data 


#st.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
st.text("The fruit load list contains:")
st.dataframe(my_data_row)

# new section
fruit_choice = st.text_input('What fruit would you like to add?','Jackfruit')
st.write('Thanks for adding', fruit_choice)
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")

