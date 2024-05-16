# Import python packages
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Penguins App:")


# Get the current credentials
session = get_active_session()

# Use an interactive slider to get user input
penguins_df = session.table('penguins').to_pandas()

st.markdown('Use this Streamlit app to make your own scatterplot about penguins!') 
 
selected_x_var = st.selectbox('What do want the x variable to be?', 
  ['BILL_LENGTH_MM','BILL_DEPTH_MM','FLIPPER_LENGTH_MM', 'BODY_MASS_G']) 
selected_y_var = st.selectbox('What about the y?', 
  ['BILL_DEPTH_MM','BILL_DEPTH_MM', 'FLIPPER_LENGTH_MM', 'BODY_MASS_G']) 

sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
fig, ax = plt.subplots() 
ax = sns.scatterplot(data = penguins_df, x = selected_x_var, 
  y = selected_y_var, hue = 'SPECIES', markers = markers,
  style = 'SPECIES') 
plt.xlabel(selected_x_var) 
plt.ylabel(selected_y_var) 
plt.title("Scatterplot of Palmer's Penguins") 
st.pyplot(fig) 

changes = st.data_editor(penguins_df, 
                         use_container_width=True, 
                         key='tbl_changes')

st.write(st.session_state['tbl_changes'])
change_index = [i for i in st.session_state['tbl_changes'].get("edited_rows")]
update = changes.iloc[change_index]

st.dataframe(update)

sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
fig, ax = plt.subplots() 
ax = sns.scatterplot(data = changes, x = selected_x_var, 
  y = selected_y_var, hue = 'SPECIES', markers = markers,
  style = 'SPECIES') 
plt.xlabel(selected_x_var) 
plt.ylabel(selected_y_var) 
plt.title("Scatterplot of Palmer's Penguins") 
st.pyplot(fig)