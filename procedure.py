import streamlit as st
from database import *
import pandas as pd

def procedure():
    list_of_r = [i[0] for i in view_only_restaurant_namess()]
    rname = st.selectbox("Restaurant name", list_of_r)
    if st.button("View reviews"):
        df=procedure2(rname)
        df.rename(columns = {0:"C_ID",1:"Restaurant_ID",2:"Review",3:"Date_Recorded",4:"Restaurant_Name"}, inplace = True)
        #df2=pd.DataFrame(df,columns=[ "C_ID" , "Restaurant_ID" , "Review","Date_Recorded" , "Restaurant_Name"])
        with st.expander("View all reviews for {}".format(rname)):
            st.dataframe(df)