import streamlit as st
from database import *
import pandas as pd

def agg_cnt():
    result=agg_cnt2()
    df = pd.DataFrame(result, columns=['Number of Vacant Tables:'])
    with st.expander("Number of Vacant Tables:"):
        st.dataframe(df)
    