import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="restaurant_table_booking_system"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Customer (C_ID int PRIMARY KEY,FirstName varchar(255),LastName varchar(255),Email_ID varchar(255),Phone_number bigint)')
    #c.execute('Use restaurant_table_booking_system')

def add_data_cust(c_id, firstname, lastname, email, phone):
    c.execute('INSERT INTO Customer (C_ID, FirstName, LastName, Email_ID, Phone_number) VALUES (%s,%s,%s,%s,%s)',
              (c_id, firstname, lastname, email, phone))
    mydb.commit()

def add_data_rest(restaurant_id, rname, descrip, phone,street_name,city):
    c.execute('INSERT INTO Restaurant (Restaurant_ID, Restaurant_Name, Description, Phone_number, Street_name, City) VALUES (%s,%s,%s,%s,%s,%s)',
              (restaurant_id, rname, descrip, phone,street_name,city))
    mydb.commit()

def add_data_rev(c_id,restaurant_id,review,date):
    c.execute('INSERT INTO Review (C_ID, Restaurant_ID, Review , Date_Recorded) VALUES (%s,%s,%s,%s)',
              (c_id, restaurant_id, review, date))
    mydb.commit()

def add_data_rest_table(t_id,restaurant_id,capacity,vacancy,reserved):
    c.execute('INSERT INTO Restaurant_Table (T_ID, Restaurant_ID, Capacity , Vacancy, Reserved) VALUES (%s,%s,%s,%s,%s)',
              (t_id,restaurant_id,capacity,vacancy,reserved))
    mydb.commit()

def add_data_reservation(reservation_id,tid,cid,restaurant_id,r_date,r_time):
    c.execute('INSERT INTO Reservation (Reservation_ID, T_ID, C_ID, Restaurant_ID, R_Date, R_Time) VALUES (%s,%s,%s,%s,%s,%s)',
              (reservation_id,tid,cid,restaurant_id,r_date,r_time))
    mydb.commit()

def view_all_data_cust():
    c.execute('SELECT * FROM Customer')
    data = c.fetchall()
    return data
def view_all_data_rest():
    c.execute('SELECT * FROM Restaurant')
    data = c.fetchall()
    return data
def view_all_data_review():
    c.execute('SELECT * FROM Review')
    data = c.fetchall()
    return data
def view_all_data_table():
    c.execute('SELECT * FROM Restaurant_table')
    data = c.fetchall()
    return data   

def view_all_data_reservation():
    c.execute('SELECT * FROM Reservation')
    data = c.fetchall()
    return data   

def view_only_customer_names():
    c.execute('SELECT C_ID FROM Customer')
    data = c.fetchall()
    return data

def view_only_restaurant_names():
    c.execute('SELECT Restaurant_ID FROM Restaurant')
    data = c.fetchall()
    return data

def view_only_restaurant_namess():
    c.execute('SELECT Restaurant_Name FROM Restaurant')
    data = c.fetchall()
    return data

def view_only_table_id():
    c.execute('SELECT T_ID FROM Restaurant_Table')
    data = c.fetchall()
    return data 

def view_only_reservation_id():
    c.execute('SELECT Reservation_ID FROM Reservation')
    data = c.fetchall()
    return data 

def view_only_cid():
    c.execute('SELECT C_ID FROM Review')
    data = c.fetchall()
    return data 

def view_only_rid():
    c.execute('SELECT Restaurant_ID FROM Review')
    data = c.fetchall()
    return data 


def get_details_cust(firstname):
    c.execute('SELECT * FROM Customer WHERE C_ID="{}"'.format(firstname))
    data = c.fetchall()
    return data

def get_details_rid_tid(rid,tid):
    c.execute('SELECT Vacancy,Reserved FROM Restaurant_Table WHERE T_ID="{}" and Restaurant_ID="{}"'.format(tid,rid))
    data=c.fetchall()
    return data

def get_details_rest(firstname):
    c.execute('SELECT * FROM Restaurant WHERE Restaurant_ID="{}"'.format(firstname))
    data = c.fetchall()
    return data

def get_details_table(firstname):
    c.execute('SELECT * FROM Restaurant_Table WHERE T_ID="{}"'.format(firstname))
    data = c.fetchall()
    return data

def get_details_reservation(firstname):
    c.execute('SELECT * FROM Reservation WHERE Reservation_ID="{}"'.format(firstname))
    data = c.fetchall()
    return data

def get_details_review(cid,rid):
    c.execute('SELECT * FROM Review WHERE C_ID="{}" and Restaurant_ID="{}"'.format(cid,rid))
    data = c.fetchall()
    return data

def get_details_rid_tid_for_delete(reservation_id):
    c.execute('SELECT Restaurant_ID, T_ID FROM Reservation WHERE Reservation_ID="{}"'.format(reservation_id))
    data = c.fetchall()
    return data

def edit_details_cust(new_cid, new_firstname, new_lastname, new_email, new_phone, c_id, firstname, lastname, email, phone):
    c.execute("UPDATE Customer SET C_ID=%s, FirstName=%s, LastName=%s, Email_ID=%s, Phone_number=%s WHERE "
              "C_ID=%s and FirstName=%s and LastName=%s and Email_ID=%s and Phone_number=%s", (new_cid, new_firstname, new_lastname, new_email, new_phone, c_id, firstname, lastname, email, phone))
    mydb.commit()


def edit_details_rev(new_c_id, new_restaurant_id, new_review, new_date, cid, rid, review, date_recorded):
    c.execute("UPDATE Review SET C_ID=%s, Restaurant_ID=%s, Review=%s, Date_Recorded=%s WHERE "
              "C_ID=%s and Restaurant_ID=%s and Review=%s and Date_Recorded=%s", (new_c_id, new_restaurant_id, new_review, new_date, cid, rid, review, date_recorded))
    mydb.commit()


def edit_details_rest(new_restaurant_id,new_rname,new_descrip,new_phone,new_street_name,new_city,rest_id,rest_name,descrip,phone,street_name,city):
    c.execute("UPDATE Restaurant SET Restaurant_ID=%s, Restaurant_Name=%s, Description=%s, Phone_number=%s, Street_name=%s,City=%s WHERE "
              "Restaurant_ID=%s and Restaurant_Name=%s and Description=%s and Phone_number=%s and Street_name=%s and City=%s", (new_restaurant_id,new_rname,new_descrip,new_phone,new_street_name,new_city,rest_id,rest_name,descrip,phone,street_name,city))
    mydb.commit()


def edit_details_table(new_t_id, new_restaurant_id, new_capacity, new_vacancy, new_reserved, t_id, restaurant_id, capacity, vacancy, reserved):
    c.execute("UPDATE Restaurant_Table SET T_ID=%s, Restaurant_ID=%s, Capacity=%s, Vacancy=%s, Reserved=%s WHERE "
              "T_ID=%s and Restaurant_ID=%s and Capacity=%s and Vacancy=%s and Reserved=%s", (new_t_id, new_restaurant_id, new_capacity, new_vacancy, new_reserved, t_id, restaurant_id, capacity, vacancy, reserved))
    mydb.commit()


def edit_details_reservation(new_reservation_id,new_tid,new_cid,new_restaurant_id,new_r_date,new_r_time,reservation_id,t_id,c_id,restaurant_id,r_date,r_time):
    c.execute("UPDATE Reservation SET Reservation_ID=%s, T_ID=%s, C_ID=%s, Restaurant_ID=%s, R_Date=%s,R_Time=%s WHERE "
              "Reservation_ID=%s and T_ID=%s and C_ID=%s and Restaurant_ID=%s and R_Date=%s and R_Time=%s", (new_reservation_id,new_tid,new_cid,new_restaurant_id,new_r_date,new_r_time,reservation_id,t_id,c_id,restaurant_id,r_date,r_time))
    mydb.commit()


def edit_vacancy_table(vacancy,reserved,rid,tid):
    c.execute("UPDATE Restaurant_Table SET Vacancy=%s, Reserved=%s WHERE "
            "Restaurant_ID=%s and T_ID=%s", (vacancy,reserved,rid,tid))
    mydb.commit()


def delete_data_cust(firstname):
    c.execute('DELETE FROM Customer WHERE C_ID="{}"'.format(firstname))
    mydb.commit()

def delete_data_rest(firstname):
    c.execute('DELETE FROM Restaurant WHERE Restaurant_ID="{}"'.format(firstname))
    mydb.commit()

def delete_data_table(firstname):
    c.execute('DELETE FROM Restaurant_Table WHERE T_ID="{}"'.format(firstname))
    mydb.commit()

def delete_data_review(cid,rid):
    c.execute('DELETE FROM Review WHERE C_ID="{}" and Restaurant_ID="{}"'.format(cid,rid))
    mydb.commit()

def delete_data_reservation(firstname):
    c.execute('DELETE FROM Reservation WHERE Reservation_ID="{}"'.format(firstname))
    mydb.commit()

def procedure2(rname):
    c.callproc('get_reviews',[rname])
    df=pd.DataFrame()
    for result in c.stored_results():
        temp_df=pd.DataFrame(result.fetchall())
        df=df.append(temp_df)
    return df

def join2():
    c.execute('SELECT C.C_ID,C.FirstName,C.LastName FROM Customer C INNER JOIN Reservation R ON C.C_ID=R.C_ID')
    data=c.fetchall()
    return data

def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    desc=c.description
    return data,desc

def agg_cnt2():
    c.execute('SELECT COUNT(T_ID) FROM Restaurant_table WHERE vacancy="Yes"')
    data=c.fetchall()
    return data

def query2(q):
    c.execute('{}'.format(q))
    data=c.fetchall()
    return data

def set_oper2():
    c.execute('SELECT * FROM Restaurant WHERE Restaurant_ID IN (SELECT Restaurant_ID from Restaurant WHERE Street_Name="Koramangala" INTERSECT SELECT Restaurant_ID from Restaurant_Table WHERE Vacancy="Yes")')
    data=c.fetchall()
    return data



