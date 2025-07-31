
# Define connection parameters
connection_parameters = {
    "account": "PWRZITO-SFB66087",
    "user": "CHINNA32",
    "password": "Gogulamudi@526k",
    "role": "SYSADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "SMOOTHIES",
    "schema": "PUBLIC"
}
# Import python packages
import streamlit as st
import requests
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark import Session
def get_snowpark_session():
    """ Get or create a Snowpark session """
    return Session.builder.configs(connection_parameters).create()

# Use this function to get a single session instead of creating new ones
session = get_snowpark_session()

smoothiefroot_response = requests.get("https://my.fruityvice.com/api/fruit/watermelon")
st.text(smoothiefroot_response)

# Write directly to the app
st.title(f" :cup_with_straw: Customise Your Smoothie :cup_with_straw:")
st.write(
  """Choose the fruit you want to your custom smoothie!
  """
)
def get_snowpark_session():
    """ Get or create a Snowpark session """
    return Session.builder.configs(connection_parameters).create()

# Use this function to get a single session instead of creating new ones
session = get_snowpark_session()

from snowflake.snowpark.functions import col


my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
name_on_order =st.text_input('Name On Smoothie :')

ingredients_list=st.multiselect('Choose upto 5 items:',my_dataframe,max_selections=5)
st.write('The Name On Order is:',name_on_order)
if ingredients_list:
    st.write(ingredients_list)
    st.text(ingredients_list)
    
    ingredients_string=''
    for each_fruit in ingredients_list:
        ingredients_string +=each_fruit + ' '

    st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""

    #st.write(my_insert_stmt)
    #st.stop()
    time_to_insert=st.button('Submit Order')
      

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
    st.success("Congratulations, {}! You have successfully Ordered your Smoothie.".format(name_on_order))
