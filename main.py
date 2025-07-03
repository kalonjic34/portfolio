import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile.jpg",width=450)

with col2:
    st.title("Christian Kalonji")
    content  = """
    Hi, I am Christian! I am an aspiring Python software engineer, currently a student at Eduvos pursuing a Bachelor in IT Software Engineering.
    I am in my third year of studies and passionate about building software solutions that solve real-world problems.
    Although I do not have any working experience yet, I am eager to learn, grow, and apply my knowledge in a professional environment.
    I am committed to continuously improving my skills, collaborating with others, and taking on new challenges as I work towards starting my career in software engineering.
    """
    st.info(content)
   
   
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
""" 
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        
        
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])