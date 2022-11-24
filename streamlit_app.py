import streamlit
streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.title('Omega 3 & Blueberry Oatmeal')
streamlit.title('Kale,Spinach & Rocket Smoothie')
streamlit.title('Hard-Boiled Free-Range Egg')
streamlit.header('Breakfast Favorites')
streamlit.title('🥣Omega 3 & Blueberry Oatmeal')
streamlit.title('🥗Kale,Spinach & Rocket Smoothie')
streamlit.title('Hard-Boiled Free-Range Egg')
streamlit.title('🥑🍞Avocado Toast')

streamlit.header('🍌🥭Build Your Own Fruit Smoothie🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.S3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)




