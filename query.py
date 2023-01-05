import streamlit as st
from database import *
import pandas as pd

def query():
    with st.form(key='query_form'):
                 
        raw_code = st.text_area("Type SQL query here")
        submit_code = st.form_submit_button("Execute!")

    if submit_code:
        st.code(raw_code)
        query_results,desc = sql_executor(raw_code) 
        cols=[i[0] for i in desc]
        df = pd.DataFrame(query_results,columns=cols)
        st.dataframe(df)