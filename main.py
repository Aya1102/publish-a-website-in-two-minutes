import streamlit as st
import pandas

data = {
'series1':[1,3,4,6,7],
'series2':[15,46,78,89]
}

df = pandas.DataFrame(data)
st.title('Our first streamlist App')
st.subheader('Automate Everything with Python')
st.write('''Now add some text
Hope you like it
And enjoy''')
st.write(df)
