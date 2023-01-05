import streamlit as st
from database import *
import pandas as pd

def set_oper():
    result=set_oper2()
    df = pd.DataFrame(result, columns=['Restaurant_ID', "Restaurant_Name","Description","Phone_number","Street_name","City"])
    with st.expander("View Restaurants Details"):
        st.dataframe(df)