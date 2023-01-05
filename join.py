import streamlit as st
from database import *
import pandas as pd

def join():
    p= join2()
    df2 = pd.DataFrame(p, columns=[ "C_ID" , "FirstName","LastName"])
    st.dataframe(df2)
