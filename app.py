import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Hello many world ")

df = pd.DataFrame({
    'A': [1,2,3,4],
    'B' : [5,6,7,8]
})

st.write("May data:")
st.write(df)
st.write("June data:")
st.table(df)
st.write("July data:")
st.dataframe(df)


# chart_data = pd.DataFrame(
#     np.random.randn(20,3), 
#     columns = ['a','b','c'])

# st.write('Line Chart Data: ')
# st.line_chart(chart_data)

# st.write('Area Chart Data: ')
# st.area_chart(chart_data)

# st.write('Bar Chart Data: ')
# st.bar_chart(chart_data)



# map_data = pd.DataFrame(np.random.randn(1000,2)/[50,50] + [52.52, 13.405], columns=['lat', 'lon'] )
# st.write('Map: ')

# st.map(map_data)

# x = st.slider('x')
# st.write(x, 'squared is ', x*x)


x = np.linspace(0, np.pi*2,100)

t = st.slider('t',0.0,10.0,1.0)

x0 = st.slider('x0',0.0, np.pi *2, 0.0)

y= np.sin(x*t+x0)


xydf = pd.DataFrame({'x':x,'y':y})
st.line_chart(xydf)


st.text_input("Your name",key = 'name')

st.session_state['name']


# if st.checkbox('show line chart'):
#     st.line_chart(pd.DataFrame({"sin(x*t+x0)":y}))





# st.sidebar

# with st.expander('Function Settings'):
#     st.write("This is the sidebar")
#     x = np.linspace(0, np.pi*2, 100)

#     t = st.slider('t', 0.0, 10.0, 1.0, key="t_slider")
#     x0 = st.slider('x0', 0.0, np.pi*2, 0.0, key="x0_slider")

#     function_name = st.selectbox(
#         'Function',
#         ['sin', 'cos', 'tan'],
#         key="function_select"
#     )

#     function_dict = {'sin': np.sin, 'cos': np.cos, 'tan': np.tan}

# if st.checkbox('show line chart', key="show_chart"):
#     y = function_dict[function_name](x*t + x0)
#     st.line_chart(pd.DataFrame({f"{function_name}(x*t+x0)": y}))

# st.write('You selected: ', function_name)

tabs = st.tabs(['charts', 'help'])

with tabs[0]:
    col1, col2 = st.columns(2)

    with col1:
        with st.expander('Function Settings'):
            st.write("This is the sidebar")
            x = np.linspace(0, np.pi*2, 100)

            t = st.slider('t', 0.0, 10.0, 1.0, key="Frequency")
            x0 = st.slider('x0', 0.0, np.pi*2, 0.0, key="x0_slider")

            function_name = st.selectbox(
                'Function',
                ['sin', 'cos', 'tan'],
                key="function_select"
            )

            function_dict = {'sin': np.sin, 'cos': np.cos, 'tan': np.tan}

        with col2:
            if st.checkbox('Show line chart'):
                y = function_dict[function_name](x*t + x0)
                st.line_chart(pd.DataFrame({f"{function_name}(x*t+x0)": y}))


with tabs[1]:
    st.header("Help")
    st.write("This is the help tab.")


st.write(st.session_state['Frequency'])
st.write(st.session_state['x0_slider'])