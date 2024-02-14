import streamlit

import pandas as pd
import numpy


def fetchRecords(records_password):
    try:
        if records_password[0] == 'ADMIN':  #for security purpose create a file to hold this password
        # if  password is in list proceed
            df_fetch = pd.read_csv('Reg.csv')
            streamlit.write(df_fetch)
            count = len(df_fetch)
            return f'all {count} records fetched'
        else:
            return 'wrong password'
    except:  # capture bug and error
        return 'error in Registration'

#delete registration record
#delet error in sales records
def deleteRecords(info_delete):
    try:
        if info_delete[0] == 'ADMIN':
            #proceed if password is admin
            if info_delete[1]: # admin entry found
                 #return f'{info_delete[1]}'
                #if entry for row to delete is not empty
                df_fetch2 = pd.read_csv('Reg.csv')
                if info_delete[1] < len(df_fetch2.index) :
                #drop the row df.index[-1]
                    df_update_reg = df_fetch2.drop(df_fetch2.index[info_delete[1]])
                    df_update_reg.to_csv('Reg.csv',index =False)
                    return f'Row {info_delete[1]} is succesfully deleted '
                else:
                    return 'Row of record doesnt exist. Enter proper row  '
            else:
                return ' you have not enter row to delete'
        else:
            return " wrong password"
    except:  # capture bug and error
        return ' code error'
    #deleteDuesRecords
def deleteDuesRecords(entrydues_delete):
    try:
        if entrydues_delete[0] == 'ADMIN':
            #proceed if password is admin
            if entrydues_delete[1]: # admin entry  for row is found

                #if entry for row to delete is not empty
                df_dues_fetch = pd.read_csv('Dues_2024.csv')
                if entrydues_delete[1] < len(df_dues_fetch.index) :
                #drop the row if it less than the length of row
                    #delete the row number entrydues_delete[1] from file CSV
                    df_update_dues = df_dues_fetch.drop(df_dues_fetch.index[entrydues_delete[1]])
                    df_update_dues.to_csv('Dues_2024.csv',index =False)
                    return f'Row {entrydues_delete[1]} is succesfully deleted '
                else:
                    return 'Row of record doesnt exist. Enter proper row  '
            else:
                return ' you have not enter row to delete'
        else:
            return " wrong password"
    except:  # capture bug and error
        return ' code error'

   # upload button for addding records
   #drop duplicate from csv when more than one entry
def upload(upload_details):
    try:

        if upload_details[0] == '':
            return 'Enter password '
        elif upload_details[1] == '':
            return 'Enter First name '
        elif upload_details[2] == '':
            return 'Enter last name '
        elif upload_details[3] == '':
            return 'Enter year '
        elif upload_details[4] == '':
            return 'Enter month '
        elif upload_details[5] == '':
            return 'Enter Dues '
        elif upload_details   :#if not empty list proceed
            #check for double entry
            if upload_details[0] == 'ADMIN':#proceed if password is admin
                del upload_details[0]  # do not enter password input upload_details[0] into csv
                Input_array = numpy.asarray(upload_details)
                Input_array_reshaped = Input_array.reshape(1, -1)
                df_add= pd.DataFrame(Input_array_reshaped)

                df_add.to_csv('Dues_2024.csv',mode='a',index= False,header=False) # add records
                df2_read = pd.read_csv('Dues_2024.csv')
                df_drop = df2_read.drop_duplicates(keep='first')  # remove multiple entries of same monthly dues
                df_drop.to_csv('Dues_2024.csv',index= False)  #update the record after remove duplcates
                return 'Successful payment'
            else:
                return 'wrong password'
        else: # if everrything failed
            return 'payment failed '
    # except:  # capture bug and error
    #     return 'error in Registration'
    except:  # capture bug and error
        return ' code error'


 #creating account
def Reg(user_details):
    try:
        if user_details[0] == '':
            return 'Enter First name '
        elif user_details[1] == '':
            return 'Enter last name '
        elif user_details[2] == '':
            return 'Enter user name '
        elif user_details[3] == '':
            return 'Enter password '
        elif user_details   :#if not empty list proceed
            #check for double registration
            df2 = pd.read_csv('Reg.csv')
            check_firstname = df2['Firstname'].values.tolist()  # if does work with pandas convert to list
            check_lastname = df2['LastName'].values.tolist()
            if user_details[0] in check_firstname and user_details[1] in check_lastname:
                return 'THIS ACCOUNT HAS BEEN REGISTERED!!!'

            else: #do for ist time registration
            #     #convert  list 1d[] to array 2d(row, col) [[]]
                Input_array = numpy.asarray(user_details)
                Input_array_reshaped = Input_array.reshape(1, -1)
                df= pd.DataFrame(Input_array_reshaped)
                df.to_csv('Reg.csv',mode='a',index= False,header=False)
                return 'Successful Registration'
        else: # if everrything failed
            return 'Registration failed '
    except:  # capture bug and error
        return ' code error'
#
##checking individual records
def login(user_login):
    try:
        if user_login[0] == '':
            return 'Enter first name  '
        elif user_login[1] == '':
            return 'Enter last name  '
        # elif user_login[2] == '':
        #     return 'Enter username '
        elif user_login[2] == '':
            return 'Enter password '
        elif user_login[3] == '':
            return 'Enter year '

        ######################################### admin
        elif user_login[2] == 'ADMIN':
            #if  password is in list proceed

            if user_login[3] == 2023:
                df_admin23 = pd.read_csv('ycp_2023.csv')
                streamlit.write(df_admin23)
            elif user_login[3] == 2024:
                df_admin24 = pd.read_csv('Dues_2024.csv')
                streamlit.write(df_admin24)
                count = len(df_admin24)
                # calculate the sum  to user
                total_due = df_admin24['Dues'].sum()
                return f'Your total due is {total_due} for  {count}  records'
            else:
                return ' no file for that year found'
            return ' RECORDS for Administrators'
        #################################################

        elif user_login : #if not empty list proceed
            #check for authencation
            df2 = pd.read_csv('Reg.csv')
            #user details fetching...
            passlist= df2['Password'].values.tolist() # if does work with pandas convert to list
            if user_login[2] in passlist: #check pasword in list
                if user_login[3] == 2023:  # if 2023 file selcted
                    df3 = pd.read_csv('ycp_2023.csv')
                    #if user_login[0] in df3['FirstName'].values.tolist():
                    # streamlit.text_area(label='result', key='3', value=df3['MembersID'].values.tolist())
                    my_fin_2023_details = df3.loc[(df3['LastName'] == user_login[1])&(df3['FirstName'] == user_login[0])  ]
                    # my_fin_2023_details = (df3.loc[(df3['LastName'] == user_login[1])& (df2.loc(df2[''LastName''] == user_login[1])

                    streamlit.write(my_fin_2023_details)
                    return f'Hello {user_login[0]} {user_login[1]} your finacial records for 2023  '

                elif user_login[3] == 2024:
                        df4 = pd.read_csv('Dues_2024.csv')
                        #Ensure capitalisation of user details matches the csv file
                        my_fin_2024_details = df4.loc[(df4['LastName'] == user_login[1]) &  (df4['FirstName'] == user_login[0])  ]

                        streamlit.write(my_fin_2024_details)
                        return f'Hello {user_login[0]} {user_login[1]} your finacial records for 2024  '
                else:
                        return ' no file for that year found'
            else:
                return ' wrong password'

        else: # if user login is empty
            return 'login failed '
    except:  # capture bug and error
        return ' code error'

##### build interface
def main():



    # Registration inteface
    # give a title
    streamlit.title(' YOUNG CATHOLIC PROFESSIONALs, OKEAFA - financial Records')

    streamlit.image('ycp.png', caption='young and catholic') #copy image to pain resize 100 pixel
    streamlit.title(' Create Account')
    Enter_firtname = streamlit.text_input('enter firstname', value="", key= 'fn')
    Enter_firtname_upper = Enter_firtname.upper().strip() # pass an upper to database

    Enter_lastname = streamlit.text_input('enter lastname', value="",key= 'ln')

    Enter_lastname_upper = Enter_lastname.upper().strip() # pass an upper

    Enter_username = streamlit.text_input('enter username', value="", key= 'us')

    Enter_username_upper = Enter_username.upper().strip()

    Enter_password = streamlit.text_input('enter password', value="",key= 'pw')

    Enter_password_upper = Enter_password.upper().strip()

    feedback = ""  # declare this variable to hold result like empty list

    if streamlit.button('click here for Registration',key = 'reg'):
        # Reg ...call the function to process input
        feedback = Reg([Enter_firtname_upper, Enter_lastname_upper,Enter_username_upper, Enter_password_upper])

    streamlit.success(feedback)
#####  fetch finacial records  interface
    # give a title

    streamlit.title('Check MY Financial status')
    login_firstname = streamlit.text_input('enter firstname', value="", key='Lfn')

    login_firstname_upper = login_firstname.upper().strip()

    login_lastname = streamlit.text_input('enter lastname', value="", key='Lln')

    login_lastname_upper = login_lastname.upper().strip()

    #login_username = streamlit.text_input('enter username', value="", key= 'user')

    # login_username_upper = login_username.upper()

    Login_password = streamlit.text_input('enter password', value="",key= 'pass')

    Login_password_upper = Login_password.upper().strip()

    df = pd.read_csv('yearly.csv')
    selected_items = streamlit.selectbox("Select year ", df['Year']  , key='year')
    year = selected_items
    # streamlit.text_area('')

    details = ""  # declare this variable to hold result like empty list

    if streamlit.button('MY Financial status', key = 'log'):
        # Reg ...call the function to process input login_username_upper,
        details = login([login_firstname_upper,login_lastname_upper,Login_password_upper,int(year)])

    streamlit.success(details)



#UPLOAD inteface
    # give a title
    streamlit.title(' Upload Dues  ')
    streamlit.subheader('Admins only')
    upload_password = streamlit.text_input('enter password', value="", key='uppass')
    upload_password_upper = upload_password.upper().strip()
    upload_firtname = streamlit.text_input('enter firstname', value="", key= 'uf')
    upload_firtname_upper = upload_firtname.upper().strip() # pass an upper to database

    upload_lastname = streamlit.text_input('enter lastname', value="",key= 'ul')
    upload_lastname_upper = upload_lastname.upper().strip() # pass an upper

    df_cal = pd.read_csv('CALENDAR.csv')
    selected_year = streamlit.selectbox("Select year ", df_cal['YEAR'], key='uyear')
    upload_year = selected_year
    df_cal = pd.read_csv('CALENDAR.csv')
    selected_month = streamlit.selectbox("Select month  ", df_cal['MONTH'], key='umonth')
    upload_month = selected_month
    df_cal = pd.read_csv('CALENDAR.csv')
    selected_amount = streamlit.selectbox("Select amount in Naira ", df_cal['AMOUNT'], key='uamount')
    upload_amount = selected_amount

    uploadholder = ""  # declare this variable to hold result like empty list

    if streamlit.button('upload dues',key = 'upload'):
        # Reg ...call the function to process input
        uploadholder = upload([upload_password_upper,upload_firtname_upper, upload_lastname_upper,int(upload_year), upload_month,int(upload_amount)])


########## delete due interface
    streamlit.success(uploadholder)
    streamlit.subheader(' Delete Dues  ')
    admindues_password = streamlit.text_input('enter password', value="", key='duepass')
    admindues_password_upper = admindues_password.upper().strip()

    Dues_admin_del = streamlit.number_input('enter row number of record to delete', min_value=0, max_value=10000, value=1000, step=1, key='Duesrows')
    #admin_del_upper = admin_del.upper().strip()
    delectedue = ""
    if streamlit.button('Delete Registration Record', key='deldues'):
        delectedue = deleteDuesRecords([admindues_password_upper,int(Dues_admin_del)])
    streamlit.success(delectedue)  # return the result

    # fetch all Registration records ----- fetch all sales records
    # give a title

    streamlit.header('Admins only')
    admin_password = streamlit.text_input('enter password', value="", key='regpass')
    admin_password_upper = admin_password.upper().strip()
    fectchreg = ""  # declare this variable to hold result like empty list

    if streamlit.button('See all Registration', key='fetchreg'):
        # fetchRecords ...call the function to process input
        fectchreg = fetchRecords([admin_password_upper])
    streamlit.success(fectchreg)
    # DELTING RECORDS

    admin_del = streamlit.number_input('enter row number of record to delete', min_value=0, max_value=10000, value=1000,
                                       step=1, key='regrows')
    # admin_del_upper = admin_del.upper().strip()
    delectereg = ""
    if streamlit.button('Delete Registration Record', key='delreg'):
        delectereg = deleteRecords([admin_password_upper, int(admin_del)])
    streamlit.success(delectereg)  # return the result


if __name__ == '__main__':
    main()

# web app  on your desktop local host
#run  on your pycharm terminal ' streamlit run ycp.py '
