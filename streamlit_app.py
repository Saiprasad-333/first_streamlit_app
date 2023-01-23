import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale,spinach & Rocket smoothie')
streamlit.text('🐔Hard-boiled Free-range Egg')
streamlit.text('🥝🍞Avacado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
