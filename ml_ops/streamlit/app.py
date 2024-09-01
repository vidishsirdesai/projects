import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("This is a subheader with a divider", divider="gray")
st.subheader("These subheaders have rotating dividers", divider=True)
st.subheader("One", divider=True)
st.subheader("Two", divider=True)
st.subheader("Three", divider=True)
st.subheader("Four", divider=True)