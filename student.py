import mysql.connector
import streamlit as st
import datetime
import pandas as pd

#Establish a connection to Mysql Server

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Vamsi@0116",
      database="crud_new1",


 )
mycursor=mydb.cursor()
print("Connection Established")


def main():
    st.title("STUDENT REGISTRATION FORM ");
    option=st.sidebar.selectbox("Select an Operation ",("Create","Read","Update","Delete"))
    if option=="Create":
        st.subheader("Create a Record")
        Name=st.text_input("Enter Name")
        fathername=st.text_input("Enter fathername")
        dateofbirth = st.date_input(
    "Enter your date of birth",value=None,
    min_value=datetime.date(1800, 1, 1),
    max_value=datetime.date(9999,12,31)
)
        email=st.text_input("Enter email")
        contactnumber=st.text_input("Enter contactnumber")
    
    
   
        
        
        if st.button("Create"):
           sql="insert into users(Name,email,fathername,dateofbirth,contactnumber) values(%s,%s,%s,%s,%s)"
           val=(Name,email,fathername,dateofbirth,contactnumber)
           mycursor.execute(sql,val)
           mydb.commit()
           st.success("Record Created Successfully !!!")
           
    elif option == "Read":
        st.subheader("Read Records")
        query = "SELECT * FROM users"
        df = pd.read_sql(query, mydb)
        st.dataframe(df)
        
            
        
    elif option=="Update":
        st.subheader("Update a Record")
        id=st.number_input("Enter ID",min_value=1)
        name=st.text_input("Enter New Name")
        fathername=st.text_input("Enter fathername")
        
        dateofbirth=st.date_input("Enter your date of birth",value=None, min_value=datetime.date(1800, 1, 1),
    max_value=datetime.date(9999,12,31)
    )
        email=st.text_input("Enter New Email")
        contactnumber=st.text_input("Enter contactnumber")
        
        if st.button("Update"):
            sql="update users set name=%s, email=%s,fathername=%s,dateofbirth=%s,contactnumber=%s where id =%s"
            val=(name,email,fathername,dateofbirth,contactnumber,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully !!!")
            
    elif option=="Delete":
        st.subheader("Delete a Record")
        id=st.number_input("Enter ID",value=None)
        if st.button("Delete"):
            sql="delete from users where id =%s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")


        
    elif option=="Delete":
        st.subheader("Delete a record")
        
        



if __name__=="__main__":
      main()