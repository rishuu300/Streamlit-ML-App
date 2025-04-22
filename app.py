import streamlit as st # type: ignore
import pandas as pd
import numpy as np

# Title of the application
st.title("Hello streamlit")

# Display a simple text
st.write("This is a simple streamlit application.")

# Display a dataframe
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': ['A', 'B', 'C', 'D', 'E']
})
st.write("Here is a simple dataframe:")
st.dataframe(df)

# Display a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)