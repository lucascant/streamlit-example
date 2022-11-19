from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to My Application!

Complete the form to customize this app

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.title('Uber not pickups')

fname = st.text_input('Fist name:')
lname = st.text_input('Last name:')
email = st.text_input('E-mail:')
st.selectbox('Pick one', ['Too Young', 'A little Lost','Too old'])
dbirth = st.date_input('Ok tell me your birthday')
time = st.time_input('What time ?')
st.checkbox('I did not read but I agree')
st.button('Click me')
st.button('Do not click')
button1 = st.button('Alright click then')
st.write("Please contact us to get access!")
st.text_area('Type a message that I will not read')
st.color_picker('Pick a color if you wish')

col4, col5 = st.columns(2)
with col4:
    st.text(button1)
with col5:
    st.text(time)
    st.text('I am here')


with st.form(key='Form name'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')
    st.form_submit_button('Cancel')

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
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.time_input('Meeting time')
st.color_picker('Pick a color')
'''

col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

with col1:
    col1.write("This is column 1 too")
with col2:
    col2.write("This is column 3")
    col2.write("This is column 4")

''' ============== SPACE ============'''

tab1, tab2, tab3, tab4 = st.tabs(["Tab 1", "Hidden here", "you can guess","Check here"])

with tab1:
    with col1:
        task1 = st.text_input('Task')
    with col2:
        starttime = st.date_input('Start:')
        time_start = st.time_input('What time ?')
    with col3:
        endtime = st.date_input('End:')
        time_end = st.time_input('What time ?')

with tab2:
    color1 = st.color_picker('Pick a color')
    color2 = st.color_picker('Pick a color')
    color3 = st.color_picker('Pick a color')
    color3 = st.color_picker('Pick a color')   

    col1, col2, col3, col4 = st.columns(4)
    col1.write('Color 1 code:', color1)
    col2.write('Color 2 code:', color2)
    col3.write('Color 3 code:', color3)
    col4.write('Color 4 code:', color4)

with tab3:
    st.file_uploader("Upload a file to nowhere")

with tab4:
    tab4.write("This is you told me so far")
    tab4.write(fname)
    tab4.write(lname)
    tab4.write(email)




''' ============== MORE SPACE ============'''
''' ============== MORE SPACE ============'''

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral LLL", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral LLL", 1, 100, 5)

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
