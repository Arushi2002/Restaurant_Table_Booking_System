import streamlit as st
from database import *
#from datetime import datetime
import datetime
from procedure import procedure
from agg_cnt import agg_cnt
from set_oper import set_oper

def create_customer():
    col1, col2 = st.columns(2)
    with col1:
        c_id = st.number_input("Customer ID:",min_value=1,step=1)
        firstname = st.text_input("First Name:")
        lastname = st.text_input("Last Name:")
    with col2:
        email=st.text_input("Email_ID:") 
        phone= st.number_input("Phone number:",min_value=1000000000,step=1)


    if st.button("Add Customer"):
        add_data_cust(c_id, firstname, lastname, email, phone)
        st.success("Successfully added Customer: {}".format(firstname))

def create_rest():
    col1, col2 = st.columns(2)
    with col1:
        restaurant_id = st.number_input("Restaurant ID:",min_value=1,step=1)
        rname = st.text_input("Restaurant Name:")
        descrip = st.text_input("Description:")
    with col2: 
        phone= st.number_input("Phone number:",min_value=1000000000,step=1)
        street_name=st.text_input("Street Name:")
        city=st.text_input("City")

    if st.button("Add Restaurant"):
        add_data_rest(restaurant_id, rname, descrip, phone,street_name,city)
        st.success("Successfully added Restaurant: {}".format(rname))

def create_review():
    col1, col2 = st.columns(2)
    with col1:
        c_id = st.number_input("Customer ID:",min_value=1,step=1)
        restaurant_id = st.number_input("Restaurant ID:",min_value=1,step=1)
    with col2: 
        review=st.text_input("Review:")
        date=st.date_input("Date Recorded:")


    if st.button("Add Review"):
        add_data_rev(c_id,restaurant_id,review,date)
        st.success("Successfully added Review")

def create_rest_table():
    col1, col2 = st.columns(2)
    with col1:
        t_id = st.number_input("Table ID:",min_value=1,step=1)
        restaurant_id = st.number_input("Restaurant ID:",min_value=1,step=1)
        capacity = st.number_input("Capacity:",min_value=1,step=1)
    with col2: 
        vacancy= st.selectbox("Vacancy:", ["Yes","No"])
        reserved=st.selectbox("Reserved:",["Yes","No"])
    
    if st.button("Add Restaurant Table"):
        add_data_rest_table(t_id,restaurant_id,capacity,vacancy,reserved)
        st.success("Successfully added Restaurant table: {}".format(t_id))

def create_reservation():
    myobj = datetime.datetime.now()
    st.subheader("Procedure that filters reviews based on restaurant names:")
    procedure()

    st.subheader("View the number of vacant tables:")
    agg_cnt()

    st.subheader("Find the restaurants who have vacant tables and are present in Koramangala:")
    set_oper()
    
    st.subheader("Enter Reservation Details:")
    col1, col2 = st.columns(2)
    

    with col1:
        
        reservation_id=st.number_input("Reservation ID:",min_value=1,step=1)
        tid=st.number_input("Table ID:",min_value=1,step=1)
        cid=st.number_input("Customer ID:",min_value=1,step=1)
        
    
    with col2: 
        restaurant_id=st.number_input("Restaurant ID:",min_value=1,step=1)
        r_date=st.date_input("Reservation Date:")
        r_time = st.time_input('Reservation Time', datetime.time(myobj.hour, myobj.minute))


    if st.button("Reserve Table"):
        selected_result=get_details_rid_tid(restaurant_id,tid)
        if selected_result:
            vacancy = selected_result[0][0]
            reserved = selected_result[0][1]
        if selected_result:
            if(vacancy.strip()=="Yes" and reserved.strip()=="No"):
                add_data_reservation(reservation_id,tid,cid,restaurant_id,r_date,r_time)
                st.success("Successfully added Reservation: {}".format(reservation_id))
                edit_vacancy_table("No","Yes",restaurant_id,tid)
                
            else:
                st.error("Sorry, Table already reserved!")


