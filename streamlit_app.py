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
st.text_area('Type a message that I will not read')
st.multiselect('I would like:', ['orange', 'apples', 'peach'])
st.checkbox('I did not read but I agree')
st.write("Please contact us to get the details!")

colA, colB, colC, colD, colE = st.columns(5)
with colA:
    button1 = st.button('Click me')
    #st.text(button1)
with colB:
    button2 = st.button('Do not click')
    #st.text(button2)
with colC:
    button3 = st.button('Alright click')
    #st.text(button3)

''' PLEASE TRY TO LOG IN '''

#col4, col5 = st.columns(2)
#with col4:
#    st.text(fname)
#with col5:
#    st.text(f'I was here at {time}')


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





col100, col101 = st.columns(2)
col100.write("This is column 1")
col101.write("This is column 2")

with col100:
    col100.write("This is column 1 too")
with col101:
    col101.write("This is column 2")
    col101.write("This is column 2")


'''==     =    =   =  = = SPACE = =  =   =    =     =='''
color1 = st.color_picker('Pick a color') 
st.text(f'You chose color: {color1}')

tab1, tab2, tab3, tab4 = st.tabs(["Tab 1", 
                                "Hidden here", 
                                "you can guess",
                                "Check here",
                                "Another Tab",
                                "And another one"])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        task1 = st.text_input('Task')
    with col2:
        start_date = st.date_input('Start:')
        end_date = st.date_input('End:')
    with col3:
        start_time = st.time_input('What time did you start?')
        end_time = st.time_input('What time did you end?')

with tab2:

    col1, col2, col3, col4,col5,col6 = st.columns(6)
    col1.write('I will figure out')
    col2.write('Column')
    col2.write('Column')
    col2.write('Column')

with tab3:
    tab3.write("I see some improvement")
    file = st.file_uploader("Upload a file to nowhere")

with tab4:
    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input("Father`s name:").upper()
    with col2:
        fdb = st.date_input('Father`s birthday')
    faddress = st.text_input('Father`s address:').upper()
    tab4.text(f'Your fist name is: {fname}')
    with col1:
        mname = st.text_input('Mother`s Name:').upper()
    with col2:
        mdb = st.date_input('Father`s birthday')
    maddress = st.text_input('Mother`s address:').upper()


with tab5:
    tab5.write("This is you told me so far")
    tab5.text(f'Your fist name is: {fname}')
    tab5.text(f'Your last name is: {lname}')
    tab5.text(f'Your e-mail is : {email}')

with tab6:
    tab6.write("This is you told me so far")
    tab6.text(f'Your fist name is: {fname}')
    tab6.text(f'Your last name is: {lname}')
    tab6.text(f'Your e-mail is : {email}')

'''==     =    =   =  = = MORE SPACE = =  =   =    =     =='''
'''==     =    =   =  = = MORE SPACE = =  =   =    =     =='''

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
