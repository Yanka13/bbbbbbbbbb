import streamlit as st
from bbquote.api import quote

st.title("Breaking Bad API")

result = quote()

st.write(result)
