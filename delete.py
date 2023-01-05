import pandas as pd
import streamlit as st
from database import *


def delete_cust():
    result = view_all_data_cust()
    df = pd.DataFrame(result, columns=['C_ID','FirstName','LastName' ,'EmailID' ,'Phone_number'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_customers = [i[0] for i in view_only_customer_names()]
    selected_customer = st.selectbox("Customer to Delete", list_of_customers)
    st.warning("Do you want to delete customer with customer ID::{}?".format(selected_customer))
    if st.button("Delete Customer"):
        delete_data_cust(selected_customer)
        st.success("Customer has been deleted successfully")
    new_result = view_all_data_cust()
    df2 = pd.DataFrame(new_result, columns=['C_ID','FirstName','LastName' ,'EmailID' ,'Phone_number'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_rest():
    result = view_all_data_rest()
    df = pd.DataFrame(result, columns=['Restaurant_ID', "Restaurant_Name","Description","Phone_number","Street_name","City"])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_restaurants = [i[0] for i in view_only_restaurant_names()]
    selected_rest = st.selectbox("Restaurant to Delete", list_of_restaurants)
    st.warning("Do you want to delete restaurant with Restaurant ID::{}?".format(selected_rest))
    if st.button("Delete Restaurant"):
        delete_data_rest(selected_rest)
        st.success("Restaurant has been deleted successfully")
    new_result = view_all_data_rest()
    df2 = pd.DataFrame(new_result, columns=['Restaurant_ID', "Restaurant_Name","Description","Phone_number","Street_name","City"])
    with st.expander("Updated data"):
        st.dataframe(df2)


def delete_table():
    result = view_all_data_table()
    df = pd.DataFrame(result, columns=["T_ID","Restaurant_ID","Capacity","Vacancy","Reserved"])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_tables = [i[0] for i in view_only_table_id()]
    selected_table = st.selectbox("Table to Delete", list_of_tables)
    st.warning("Do you want to delete table with table ID::{}?".format(selected_table))
    if st.button("Delete Table"):
        delete_data_table(selected_table)
        st.success("Table has been deleted successfully")
    new_result = view_all_data_table()
    df2 = pd.DataFrame(new_result, columns=["T_ID","Restaurant_ID","Capacity","Vacancy","Reserved"])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_reservation():
    result = view_all_data_reservation()
    df = pd.DataFrame(result, columns=["Reservation_ID","T_ID","C_ID","Restaurant_ID","R_Date","R_Time"])
    df = df.astype(str)
    df['R_Time'] = df['R_Time'].map(lambda a: a[7:])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_reservation_ids = [i[0] for i in view_only_reservation_id()]
    selected_reservation_id = st.selectbox("Reservation to Delete", list_of_reservation_ids)
    st.warning("Do you want to delete reservation with Reservation ID::{}?".format(selected_reservation_id))
    if st.button("Delete Reservation"):
        selected_result=get_details_rid_tid_for_delete(selected_reservation_id)
        if selected_result:
            rid = selected_result[0][0]
            tid = selected_result[0][1]
        edit_vacancy_table("Yes","No",rid,tid)
        delete_data_reservation(selected_reservation_id)
        st.success("Reservation has been deleted successfully")
    new_result = view_all_data_reservation()
    df2 = pd.DataFrame(new_result, columns=["Reservation_ID","T_ID","C_ID","Restaurant_ID","R_Date","R_Time"])
    
    with st.expander("Updated data"):
        df2= df2.astype(str)
        df2['R_Time'] = df2['R_Time'].map(lambda a: a[7:])
        st.dataframe(df2)

def delete_review():
    result = view_all_data_review()
    df = pd.DataFrame(result, columns=["C_ID","Restaurant_ID","Review","Date_Recorded"])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_customers = [i[0] for i in view_only_cid()]
    list_of_rest=[i[0] for i in view_only_rid()]
    selected_cust = st.selectbox("Customer ID to Delete", list_of_customers)
    selected_rid= st.selectbox("Restaurant ID to Delete", list_of_rest)
    st.warning("Do you want to delete review?")
    if st.button("Delete Review"):
        delete_data_review(selected_cust,selected_rid)
        st.success("Review has been deleted successfully")
    new_result = view_all_data_review()
    df2 = pd.DataFrame(new_result, columns=["C_ID","Restaurant_ID","Review","Date_Recorded"])
    with st.expander("Updated data"):
        st.dataframe(df2)
    