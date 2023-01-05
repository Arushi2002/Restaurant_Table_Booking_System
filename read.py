import pandas as pd
import streamlit as st
import plotly.express as px
from database import *


def read():
    result = view_all_data_cust()
    # st.write(result)
    #st.write(result)
    #print(result)
    df = pd.DataFrame(result, columns=['C_ID','FirstName','LastName' ,'EmailID' ,'Phone_number'])
    with st.expander("View all Customers Details"):
        st.dataframe(df)
    # with st.expander("Customer Details"):
    #     st.dataframe(df)
    r2= view_all_data_rest()
    df2 = pd.DataFrame(r2, columns=['Restaurant_ID', "Restaurant_Name","Description","Phone_number","Street_name","City"])
    with st.expander("View all Restaurants Details"):
        st.dataframe(df2)

    r3= view_all_data_review()
    df = pd.DataFrame(r3, columns=["C_ID","Restaurant_ID","Review","Date_Recorded"])
    with st.expander("View all Review Details"):
        st.dataframe(df)

    r4=view_all_data_table()
    df = pd.DataFrame(r4, columns=["T_ID","Restaurant_ID","Capacity","Vacancy","Reserved"])
    with st.expander("View all restaurant table Details"):
        st.dataframe(df)

    r5=view_all_data_reservation()
    df = pd.DataFrame(r5, columns=["Reservation_ID","T_ID","C_ID","Restaurant_ID","R_Date","R_Time"])
    #df["R_Time"] = pd.to_timedelta(df["R_Time"])
    df = df.astype(str)
    df['R_Time'] = df['R_Time'].map(lambda a: a[7:])
    with st.expander("View all Reservation Details"):
        st.dataframe(df)