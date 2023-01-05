import streamlit as st
import mysql.connector

from create import *
from database import create_table   
from delete import *
from read import read
from update import *
from procedure import procedure
from join import join
from agg_cnt import agg_cnt
from query import query
from set_oper import set_oper
#from query import query

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
#if()
#c = mydb.cursor()
#c.execute("CREATE DATABASE railways;")

def main():
    st.title("PES1UG20CS077 - Restaurant Table Booking System")
    menu = ["Add Data", "View Data", "Edit Data", "Remove Data","Join","Query"]#,"Query"
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add Data":
        table_choice = ["Customer", "Restaurant", "Restaurant Table", "Reservation","Review"]
        choice = st.selectbox("Choose Table", table_choice)
        
        if(choice=='Customer'):
            st.subheader("Enter {} Details:".format(choice))
            create_customer()
        elif(choice=='Restaurant'):
            st.subheader("Enter {} Details:".format(choice))
            create_rest()
        elif(choice=='Review'):
            st.subheader("Enter {} Details:".format(choice))
            create_review()
        elif(choice=='Restaurant Table'):
            st.subheader("Enter {} Details:".format(choice))
            create_rest_table()
        elif(choice=='Reservation'):
            create_reservation()
        else:
            st.subheader("About Data")

    elif choice == "View Data":

        st.subheader("View Data:")
        read()

    elif choice == "Edit Data":
        table_choice =["Customer", "Restaurant", "Restaurant Table", "Reservation","Review"]
        choice = st.selectbox("Choose Table", table_choice)
        st.subheader("Edit {} Details:".format(choice))
        if(choice=='Customer'):
            update_cust()
        elif(choice=='Restaurant'):
            update_rest()
        elif(choice=='Restaurant Table'):
            update_table()
        elif(choice=='Reservation'):
            update_reservation()
        elif(choice=="Review"):
            update_review()
        else:
            st.subheader("About Data")
        # elif(choice=='Review'):
            # update

    elif choice == "Remove Data":
        table_choice =["Customer", "Restaurant", "Restaurant Table", "Reservation","Review"]
        choice = st.selectbox("Choose Table", table_choice)
        st.subheader("Delete {}:".format(choice))
        if(choice=='Customer'):
            delete_cust()
        elif(choice=='Restaurant'):
            delete_rest()
        elif(choice=='Restaurant Table'):
            delete_table()
        elif(choice=='Reservation'):
            delete_reservation()
        elif(choice=="Review"):
            delete_review()
        else:
            st.subheader("About Data")
    
    # elif choice =="Procedure":
    #     st.subheader("Procedure that filters reviews based on restaurant names:")
    #     procedure()
    elif choice=="Join":
        st.subheader("Find the names of customers who have made atleast 1 reservation:")
        join()
    elif choice == "Query":
        st.subheader("Execute any query!")
        query()

    # elif choice=="Aggregate":
    #     st.subheader("Count the number of vacant tables:")
    #     agg_cnt()
    # elif choice=="Set operation":
    #     st.subheader("Find the restaurants who have vacant tables and are in present in kormangala:")
    #     set_oper()
    else:
        st.subheader("About Data")


if __name__ == '__main__':
    main()