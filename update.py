import datetime

import pandas as pd
import streamlit as st
from database import *


def update_cust():
    result = view_all_data_cust()
    # st.write(result)
    df = pd.DataFrame(result, columns=['C_ID','FirstName','LastName' ,'EmailID' ,'Phone_number'])
    with st.expander("Current customers"):
        st.dataframe(df)
    list_of_customers = [i[0] for i in view_only_customer_names()]
    selected_cust = st.selectbox("Customer ID to Edit", list_of_customers)
    selected_result = get_details_cust(selected_cust)
    # st.write(selected_result)
    if selected_result:
        cid = selected_result[0][0]
        firstname = selected_result[0][1]
        lastname = selected_result[0][2]
        email = selected_result[0][3]
        phone = selected_result[0][4]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_cid = st.number_input("C_ID:", value=cid,min_value=1)
            new_firstname = st.text_input("First Name:", firstname)
            new_lastname = st.text_input("lastname:",lastname)
        with col2:
            new_email = st.text_input("email:",email)
            new_phone = st.number_input("phone", value=phone, min_value=1000000000)

        if st.button("Update Customer"):
            edit_details_cust(new_cid, new_firstname, new_lastname, new_email, new_phone, cid, firstname, lastname, email, phone)
            st.success("Successfully updated:: {} to ::{}".format(firstname, new_firstname))

    result2 = view_all_data_cust()
    df2 = pd.DataFrame(result2, columns=['C_ID','FirstName','LastName' ,'EmailID' ,'Phone_number'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_rest():
    result = view_all_data_rest()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Restaurant_ID', "Restaurant_Name","Description","Phone_number","Street_name","City"])
    with st.expander("Current restaurants"):
        st.dataframe(df)
    list_of_restaurants = [i[0] for i in view_only_restaurant_names()]
    selected_rest = st.selectbox("Restaurant ID to Edit", list_of_restaurants)
    selected_result = get_details_rest(selected_rest)
    # st.write(selected_result)
    if selected_result:
        rest_id = selected_result[0][0]
        rest_name = selected_result[0][1]
        descrip = selected_result[0][2]
        phone = selected_result[0][3]
        street_name = selected_result[0][4]
        city=selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_restaurant_id = st.number_input("Restaurant ID:",value=rest_id,min_value=1)
            new_rname = st.text_input("Restaurant Name:",rest_name)
            new_descrip = st.text_input("Description:",descrip)
        with col2:
            new_phone=st.number_input("Phone number:",value=phone,min_value=1000000000)
            new_street_name=st.text_input("Street Name:",street_name)
            new_city=st.text_input("City",city)

        if st.button("Update Restaurant"):
            edit_details_rest(new_restaurant_id,new_rname,new_descrip,new_phone,new_street_name,new_city,rest_id,rest_name,descrip,phone,street_name,city)
            st.success("Successfully updated:: {} to ::{}".format(rest_name, new_rname))

    result2 = view_all_data_rest()
    df2 = pd.DataFrame(result2, columns=['Restaurant_ID', "Restaurant_Name","Description","Phone_number","Street_name","City"])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_table():
    result = view_all_data_table()
    # st.write(result)
    df = pd.DataFrame(result, columns=["T_ID","Restaurant_ID","Capacity","Vacancy","Reserved"])
    with st.expander("Current Restaurant Tables"):
        st.dataframe(df)
    list_of_tables = [i[0] for i in view_only_table_id()]
    selected_table = st.selectbox("Table to Edit", list_of_tables)
    selected_result = get_details_table(selected_table)
    # st.write(selected_result)
    if selected_result:
        t_id = selected_result[0][0]
        restaurant_id = selected_result[0][1]
        capacity = selected_result[0][2]
        vacancy = selected_result[0][3]
        reserved = selected_result[0][4]
        if(vacancy=="Yes"):
            i1=0
        else:
            i1=1
        if(reserved=="Yes"):
            i2=0
        else:
            i2=1

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_t_id = st.number_input("Table ID:",value=t_id,min_value=1)
            new_restaurant_id = st.number_input("Restaurant ID:",value=restaurant_id,min_value=1)
            new_capacity = st.number_input("Capacity:",value=capacity,min_value=1)
        with col2: 
            new_vacancy= st.selectbox("Vacancy:", ["Yes","No"],index=i1)
            new_reserved=st.selectbox("Reserved:",["Yes","No"],index=i2)
    

        if st.button("Update Restaurant Table"):
            edit_details_table(new_t_id, new_restaurant_id, new_capacity, new_vacancy, new_reserved, t_id, restaurant_id, capacity, vacancy, reserved)
            st.success("Successfully updated:: {} to ::{}".format(t_id, new_t_id))

    result2 = view_all_data_table()
    df2 = pd.DataFrame(result2, columns=["T_ID","Restaurant_ID","Capacity","Vacancy","Reserved"])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_reservation():
    result = view_all_data_reservation()
    # st.write(result)
    df = pd.DataFrame(result, columns=["Reservation_ID","T_ID","C_ID","Restaurant_ID","R_Date","R_Time"])
    df = df.astype(str)
    df['R_Time'] = df['R_Time'].map(lambda a: a[7:])
    with st.expander("Current reservations"):
        st.dataframe(df)
    list_of_reservations = [i[0] for i in view_only_reservation_id()]
    selected_reserve = st.selectbox("Reservation to Edit", list_of_reservations)
    selected_result = get_details_reservation(selected_reserve)
    if selected_result:
        reservation_id = selected_result[0][0]
        t_id = selected_result[0][1]
        c_id = selected_result[0][2]
        rest_id = selected_result[0][3]
        r_date = selected_result[0][4]
        r_time=selected_result[0][5]

        # Layout of Create
    
        myobj = datetime.datetime.now()
        col1, col2 = st.columns(2)
        with col1:
            new_reservation_id=st.number_input("Reservation ID:",value=reservation_id,min_value=1,step=1)
            new_tid=st.number_input("Table ID:",value=t_id,min_value=1,step=1)
            new_cid=st.number_input("Customer ID:",value=c_id,min_value=1,step=1)
            
        
        with col2: 
            new_restaurant_id=st.number_input("Restaurant ID:",value=rest_id,min_value=1,step=1)
            new_r_date=st.date_input("Reservation Date:",r_date)
            new_r_time = st.time_input('Reservation Time', datetime.time(myobj.hour, myobj.minute))

        if st.button("Update Reservation"):
            edit_details_reservation(new_reservation_id,new_tid,new_cid,new_restaurant_id,new_r_date,new_r_time,reservation_id,t_id,c_id,rest_id,r_date,r_time)
            st.success("Successfully updated:: {} to ::{}".format(reservation_id, new_reservation_id))

    result2 = view_all_data_reservation()
    df2 = pd.DataFrame(result2, columns=["Reservation_ID","T_ID","C_ID","Restaurant_ID","R_Date","R_Time"])
    df2 = df2.astype(str)
    df2['R_Time'] = df2['R_Time'].map(lambda a: a[7:])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_review():
    result = view_all_data_review()
    # st.write(result)
    df = pd.DataFrame(result, columns=["C_ID","Restaurant_ID","Review","Date_Recorded"])
    with st.expander("Current Reviews"):
        st.dataframe(df)
    list_of_customers = [i[0] for i in view_only_cid()]
    list_of_rest=[i[0] for i in view_only_rid()]
    selected_cust = st.selectbox("Customer ID to Edit", list_of_customers)
    selected_rid= st.selectbox("Restaurant ID to Edit", list_of_rest)
    selected_result = get_details_review(selected_cust,selected_rid)
    # st.write(selected_result)
    if selected_result:
        cid = selected_result[0][0]
        rid = selected_result[0][1]
        review= selected_result[0][2]
        date_recorded = selected_result[0][3]

        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            new_c_id = st.number_input("Customer ID:",value=cid,min_value=1,step=1)
            new_restaurant_id = st.number_input("Restaurant ID:",value=rid,min_value=1,step=1)
        with col2: 
            new_review=st.text_input("Review:",review)
            new_date=st.date_input("Date Recorded:",date_recorded)


        if st.button("Update Review"):
            edit_details_rev(new_c_id, new_restaurant_id, new_review, new_date, cid, rid, review, date_recorded)
            st.success("Review Successfully updated")

    result2 = view_all_data_review()
    df2 = pd.DataFrame(result2, columns=["C_ID","Restaurant_ID","Review","Date_Recorded"])
    with st.expander("Updated data"):
        st.dataframe(df2)

 