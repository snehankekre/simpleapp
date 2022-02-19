import streamlit as st

st.title("Testing Apps!")

value = st.slider("Pick a number", 0, 15, 3)

st.write(value)

input = st.text_input("Tell me something", "Cantami o Diva")

st.write("Streamlit is fabulous!")
st.balloons()

print("write a log line")
