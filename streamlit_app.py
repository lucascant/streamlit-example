from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.title('Uber pickups in NYC test')

st.text_input('Fist name:')
st.text_input('Last name:')
st.text_input('E-mail:')
st.selectbox('Pick one', ['Too Young', 'A little Lost','Too old'])
st.checkbox('I did not read but I agree')
st.button('Click me')
st.button('Do not click')
st.button('Alright click then')

#input widgets
#st.sidebar.subheader('input features')
#var1 = st.sidebar.slider('feature 1:', 1, 100, 5)
#var2 = st.sidebar.slider('feature 2:', 1, 1000, 100)
#var3 = st.sidebar.slider('feature 3:', 1, 1000, 100)

'''
st.button('Click me')
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
'''
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.color_picker('Pick a color')

'''
with st.form(key='Form name'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')
'''

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral LLL", 1, 5000, 1)
    num_turns = st.slider("Number of turns in spiral LLL", 1, 100, 1)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
