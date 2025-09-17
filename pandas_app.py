import streamlit as st
import pandas as pd

st.title("Pandas DataFrame Example")

# Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

# Display the DataFrame in Streamlit
st.write("Here is a sample DataFrame:")
st.dataframe(df)

# Editable DataFrame
st.subheader("Data editor")
edited_df = st.data_editor(df)

# Display the static DataFrame
st.subheader("static table")
st.dataframe(df)

# Display metrics
st.subheader("Metrics")
st.metric(label="rows", value=len(df))
st.metric(label="Average Age", value=df["Age"].mean())

st.subheader("JSON and Diictionary")
sample_dict = {"name": "Alice", 
               "number": 42,
               "is_student": False,
               "courses": ["Math", "Science", "Art"],
               "skills": ["python", "data analysis", "machine learning"]
               }

#show json
st.json(sample_dict)

#show dictionary
st.write("Dictionary view:", sample_dict)