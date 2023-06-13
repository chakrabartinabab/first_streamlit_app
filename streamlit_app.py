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

#create a repeatable code block called a function
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

# new section
st.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = st.text_input('What fruit would you like information about?')
   if not fruit_choice:
      st.error("Please select a fruit to get information.") 
   else:
      back_from_function=get_fruityvice_data(fruit_choice)
      st.dataframe(back_from_function)

except URLError as e:
   st.error()
#import requests

#st.text(fruityvice_response.json())--commenting it out to remove from output screen

# normalizing the data 




#import snowflake.connector

#my_cur = my_cnx.cursor()
 
#st.text("The fruit load list contains:")
#st.dataframe(my_data_row)

st.header("The fruit load list contains:")
#snowflake related function
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from fruit_load_list")
      return my_cur.fetchall()
   
 # add a button to load the fruit
if st.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
   my_data_row = get_fruit_load_list()
   st.dataframe(my_data_row)

def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values('"+new_fruit+"')")
      return ('Thanks for adding'+new_fruit)
st.stop()
   
   
      

# new section
fruit_choice = st.text_input('What fruit would you like to add?','Jackfruit')
st.write('Thanks for adding', fruit_choice)
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")

