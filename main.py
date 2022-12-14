import streamlit as st
import pandas

data = {
  'series_1':[1,2,3,4,5],
  'series_2':[12,23,31,13,41]
}

df = pandas.DataFrame(data)

st.title('my first streamlit app')
st.subheader('introducing streamlit with Automation with Python')
st.write('''This is our first web app, Enjoy!!''')

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('censius')
st.write(myslider,"in Fahrenheit is", myslider * 9/5 +35)