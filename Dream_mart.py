# IMPORTING MODULES 
 
import pandas as pd 
 
import numpy as np 
 
import random 
 
import time 
 
import os 
 
import sys 
 
from datetime import datetime, timedelta 
 
from IPython.core.display import display, HTML 
 
display(HTML("<style>.container { width:100%; }</style>")) 
 
#IMPORTING MODULE FOR CONNECTING MYSQL AND PYTHON 
 
import pymysql 
 
#IMPORTING MODULES FOR GRAPH 
 
import matplotlib.pyplot as plt 
 
import plotly.graph_objects as go 
 
#IMPORTING MODULE FOR NOTIFICATION 
 
from plyer import notification 
 
#IMPORTING MOGULE TO ADD IMAGE 
 
from IPython.display import Image 
 
#IMPORTING MODULE TO ADD COLORS 
 
from termcolor import colored 
 
#IMPORTING MODULE TO HIDE TEXT 
 
import getpass 
 
#IMPORTING MODULE TO SEND MAIL 
 
import smtplib 
 
#IMPORTING MODULE FOR VOICE ASSISSTANCE 
 
import win32com.client as mouth 
 
 
# CONNECTING MYSQL 
 
connection = pymysql.connect(host='localhost', 
                             user='root', 
                             password='junaidh0', 
                             db='dream_mart') 
 
cursor = connection.cursor() 
 
 
#VOICE ASSISTANT 
 
speaker_number=1 
 
voice=mouth.Dispatch("SAPI.SpVoice") 
 
v=voice.GetVoices() 
 
v.Item(speaker_number).GetAttribute("Name") 
 
voice.voice 
 
voice.SetVoice(v.Item(speaker_number)) 
 
#ADDING IMAGE 
 
print('\n') 
 
display(Image(r'C:\Users\Junaidh\Desktop\Ip project\dream1.png',width="950", 
height="400")) 
 
print('\n') 
 
#GETTING STARTED 
 
voice.Speak("hi  my name is lili") 
 
voice.Speak("I am your voice assistant") 
 
j="y" 
 
while j=="y" or j=="Y": 
     
    #ASKING FOR SIGN UP OR SIGN IN 
     
    voice.Speak("DO YOU WANT TO SIGN UP OR SIGN IN") 
 
    print(colored("DO YOU WANT TO SIGN UP OR SIGN 
IN".center(120,'*'),'green',attrs=['bold'])) 
     
    print('\n') 
     
    voice.Speak("IF YOUR NEW SIGN UP") 
 
    print(colored("IF YOUR NEW SIGN UP".center(200),'red')) 
 
    print('\n') 
     
    voice.Speak("FOR SIGN UP ENTER 1 and for SIGN IN enter 2") 
 
    print(colored("FOR SIGN UP ENTER 1".center(200),'yellow')) 
     
    print('\n') 
 
    print(colored("FOR SIGN IN ENTER 2".center(200),'yellow')) 
     
    print('\n') 
     
    voice.Speak('enter your choice') 
 
    print(colored('ENTER YOUR CHOICE:','red')) 
 
    log=int(input( )) 
 
    print('\n') 
 
    a='y' 
     
    while a=="y" or a=="Y": 
         
 
        #SINGINING UP 
         
        if log==1: 
             
 
            #GETTING INFORMATION FROM USER 
             
            voice.Speak("YOU HAD CHOSEN TO SIGN UP") 
 
            print(colored("YOU HAD CHOSEN TO SIGN 
UP".center(140),'green',attrs=['bold'])) 
             
            notification.notify( 
                title = 'DREAM MART', 
                message = 'WELCOME TO DREAM MART', 
                app_icon =r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico", 
                timeout = 60) 
 
            print('\n') 
 
            print('\n') 
             
            voice.Speak("Enter your first name") 
             
            print(colored(('ENTER YOUR FIRST NAME :'),'yellow')) 
 
            first_name=input( ) 
 
            print('\n') 
             
            voice.Speak("enter your last name") 
             
            print(colored(('ENTER YOUR LAST NAME :'),'yellow')) 
 
            last_name=input( ) 
 
            print('\n') 
             
            voice.Speak("enter your date of birth ") 
             
            print(colored(('ENTER YOUR DATE OF BIRTH (YYYY-MM-DD) :'),'yellow')) 
 
            dob=input( ) 
 
            print('\n') 
             
             
            #SENDING EMAIL  
 
            em="y" 
 
            while em=="y" or em=="Y": 
                 
                 
                #GETTING A RANDON OTP 
                 
                voice.Speak("enter your email i d ") 
                 
                print(colored("ENTER YOUR EMAIL ID :","yellow")) 
                 
                email_id=input( ) 
 
                print('\n') 
 
                con=random.randint(100000,999999) 
 
                cont=str(con) 
                 
                message = 'Subject: {}\n\n{}'.format('OTP FROM DREAM MART', 'ENTER THE OTP FOR VERIFICATION '+cont) 
 
                server=smtplib.SMTP('smtp.gmail.com',587) 
 
                server.ehlo() 
 
                server.starttls() 

 
 
                server.login('dreammart31@gmail.com','dream1331') 
 
                server.sendmail('dreammart31@gmail.com',email_id,message) 
 
                server.close() 
                 
                 
                #VERIFICATION OF EMAIL 
                 
                voice.Speak("enter the o t p sent to your email id ") 
                 
                print(colored(('ENTER THE OTP SENT TO YOUR EMAIL ID'),'yellow')) 
             
                otp=int(input( )) 
 
                print('\n') 
                     
                if otp==con: 
                     
                    voice.Speak("Your email id is verified") 
 
                    print(colored("YOUR EMAIL ID IS VERIFIED",'yellow')) 
 
                    print('\n') 
 
                    em="n" 
 
                elif otp != con: 
                     
                    voice.Speak("Incorrect O T P") 
 
                    print(colored("INCORRECT OTP",'red')) 
 
                    print('\n') 
                     
                    voice.Speak("Would you like to try again ") 
 
                    em=print(colored("WOULD YOU LIKE TO TRY AGAIN ?? (Y/N) : 
"),'yellow') 
                     
                    em=input() 
 
                    print('\n') 
                                
                else: 
                         
                    print('\n') 
                     
                    break 
                         
            h='y' 
                             
           #GETTING PHONE NUMBER     
 
            while h=='y' or h =='Y': 
                 
                voice.Speak("enter your phone number") 
                 
                print(colored("ENTER YOUR PHONE NUMBER :",'yellow')) 
 
                phone_no=input( ) 
 
                print('\n') 
                     
                if len(phone_no) == 10: 
                     
                    voice.Speak("Your phone number is correct") 
                     
                    print(colored("YOUR PHONE NUMBER IS CORRECT",'red')) 
 
                    print('\n') 
 
                    h='n' 
                     
                    em='n' 
                         
                    break 
                     
                else: 
                     
                    voice.Speak("Your phone number is inncorrect") 
 
                    print(colored("YOUR PHONE NUMBER IS INCORRECT",'red')) 
 
                    print('\n') 
                     
                    voice.Speak("would you like to try again") 
                     
                    print(colored('WOULD YOU LIKE TO TRY AGAIN ? (Y/N)','red')) 
 
                    h=input() 
 
                    print('\n') 
                     
            voice.Speak('Enter your username') 
             
            print(colored('ENTER YOUR USERNAME :','yellow')) 
                         
            uname=input( ) 
                     
            print('\n') 
             
            voice.Speak('enter your password') 
             
            voice.Speak('do you want to hide your password') 
             
            voice.Speak('if yes press Y') 
             
            print(colored('DO YOU WANT TO HIDE YOUR PASSWORD (Y/N) : ','yellow')) 
             
            pass1=input( ) 
             
            print('\n') 
             
            if pass1=='y' or pass1=='Y': 
                 
                #HIDING PASSWORD 
                 
                print(colored(('ENTER YOUR PASSWORD : '),'yellow')) 
                 
                pwd=getpass.getpass( ) 
 
                print('\n') 
                 
            else: 
                 
                print(colored(('ENTER YOUR PASSWORD : '),'yellow')) 
                 
                pwd=input( ) 
 
                 
                print('\n') 
                 
 
            #TO CHECK WHETHER THE USER IS HUMAN OR BOT 
     
            voice.Speak('you need to undergo recaptcha') 
 
            print(colored(("RECAPTCHA".center(200)),'cyan')) 
 
            print('\n') 
 
            display(Image(r'C:\Users\Junaidh\Desktop\Ip_project\recaptcha.png',width="350", height="100")) 
 
            print('\n') 
             
            voice.Speak("would you like to proceed") 
             
            print(colored("WOULD YOU LIKE TO PROCEED ?? (Y/N)  : ",'red')) 
 
            q=input() 
             
            print("\n") 
 
            if q=='y' or q=='Y': 
 
                display(Image(r'C:\Users\Junaidh\Desktop\Ip project\recaptcha 
car.jpg',width="250", height="200")) 
 
                print('\n') 
                 
                voice.Speak("Enter the number of cars in the image") 
                 
                print(colored("ENTER THE NUMBER OF CARS IN THE IMAGE  : 
",'yellow')) 
 
                t=int(input()) 
 
                print('\n') 
 
                if t==2 or t==3: 
                     
                    voice.Speak("RECAPTCHA SUCCESSFUL") 
 
                    print(colored(("RECAPTCHA SUCCESSFUL"),'cyan')) 
                     
                    print('\n') 
                     
                    print('\n') 
                     
                    display(Image(r'C:\Users\Junaidh\Desktop\Ip project\rep.png',width="500", height="400")) 
                         
                    print('\n') 
                     
                    voice.Speak("YOU HAVE SUCCESSFULLY CREATED AN ACCOUNT") 
 
                    print(colored(("YOU HAVE SUCCESSFULLY CREATED AN ACCOUNT ��".center(150)),'green')) 
                     
                    notification.notify(title = 'DREAM MART', 
                                        message = 'YOU HAVE SUCCESSFULLY CREATED AN ACCOUNT ��',   
                                        app_icon =r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                        timeout = 1000) 
 
                    print('\n') 
                     
 
                    #INSERTING USER INFO INTO MYSQL TABLE 
 
                    sql = "INSERT INTO `customer` (`fname`, `lname`, `dob`, `email`, 
                    `phone_no`,`uname`,`password`) VALUES (%s, %s, %s, %s, %s,%s,%s)" 
                     
                         
                    # EXECUTING THE QUERY 
                     
                    cursor.execute(sql, (first_name,last_name,dob,email_id,phone_no,uname,pwd)) 
 
                    connection.commit() 
                     
                    voice.Speak("nice to meet u") 
 
                    display(Image(r'C:\Users\Junaidh\Desktop\Ip_project\WELCOME.png',width="50000", height="40000")) 
 
                    print('\n') 
 
                    a="n" 
                     
                    j="n" 
                         
                    em="n" 
 
                else: 
                     
                    voice.Speak("RECAPTCHA UNSUCCESSFUL") 
 
                    print(colored(("RECAPTCHA UNSUCCESSFUL"),'red')) 
 
                    print('\n') 
 
                    display(Image(r'C:\Users\Junaidh\Desktop\Ip project\recaptcha backup.png',width="250", height="200")) 
 
                    print('\n') 
                     
                    voice.Speak("Enter the text in the image") 
 
                    print(colored("ENTER THE TEXT IN IMAGE  :  ",'yellow')) 
                     
                    voice.Speak("Note There should not be any space between the character") 
 
                    print(colored(("Note : There should not be any space between the character"),'cyan')) 
 
                    t2=input( ) 
 
                    print('\n') 
 
                    if t2 == 'td4eva' or t2 == 'TD4EVA': 
                         
                        voice.Speak("RECAPTCHA SUCCESSFUL") 
 
                        print(colored(("RECAPTCHA SUCCESSFUL"),'red')) 
                          
                        print('\n') 
                         
                        print('\n') 
                         
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip_project\rep.png',width="500", height="400")) 
 
                        print('\n') 
                         
                        voice.Speak("YOU HAVE SUCCESSFULLY CREATED AN ACCOUNT") 
 
                        print(colored(("YOU HAVE SUCCESSFULLY CREATED AN ACCOUNT".center(150)),'green')) 
                         
                        notification.notify(title = 'DREAM MART', 
                            message = 'YOU HAVE SUCCESSFULLY CREATED AN ACCOUNT ��',   
                            app_icon =r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                            timeout = 60) 
                         
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip project\WELCOME.png',width="500", height="400")) 
                          
                        print('\n') 
                         
                        #INSERTING USER INFO INTO MYSQL TABLE 
 
                        sql = "INSERT INTO `customer` (`fname`, `lname`, `dob`,`email`, 
                        `phone_no`,`uname`,`password`) VALUES (%s, %s, %s, %s, %s,%s,%s)" 
                         
                        # EXECUTING THE QUERY 
                         
                        cursor.execute(sql, (first_name,last_name,dob,email_id,phone_no,uname,pwd)) 
 
                        connection.commit() 
                         
                        voice.Speak("nice to meet u") 
 
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip_project\WELCOME.png',width="600", height="400")) 
 
                        print('\n') 
 
                        a="n" 
                         
                        j="n" 
                             
                        em="n" 
 
                        print('\n') 
 
                    else: 
                         
                        voice.Speak("RECAPTCHA UNSUCCESSFUL") 
 
                        print(colored(("RECAPTCHA UNSUCCESSFUL"),'red')) 
 
                        print('\n') 
                         
                        voice.Speak("Do you want to start from the begining ") 
                         
                        print(colored("DO YOU WANT TO START FROM THE BEGINNING (Y/N) :",'yellow')) 
 
                        j=input() 
                         
                        print('\n') 
     
            else: 
             
                voice.Speak("You have to undergo recaptcha") 
 
                print(colored("YOU HAVE TO UNDERGO RECAPTCHA",'red')) 
 
                print('\n')  
                 
                voice.Speak("Note Without recaptcha your not allowed to create an account") 
 
                print("NOTE: WITHOUT RECAPTCHA YOUR NOT ALLOWED TO CREATE AN ACCOUNT") 
 
                print('\n') 
                 
                voice.Speak("D   o you want to take recaptcha ") 
                 
                print(colored("DO YOU WANT TO TAKE RECAPTCHA (Y/N) ",'yellow')) 
 
                q=input() 
                 
                print('\n') 
 
 
        #SIGN IN         
 
        elif log ==2: 
             
            voice.Speak('YOU HAD CHOSEN TO SIGN IN') 
 
            print(colored(('YOU HAD CHOSEN TO SIGN IN'.center(200)),'green')) 
 
            print('\n') 
 
            print('\n') 
             
            voice.Speak('Enter your username') 
             
            print(colored("ENTER YOUR USERNAME : ",'yellow')) 
 
            uname2=input( ) 
 
            print('\n') 
             
            voice.Speak('DO YOU WANT TO HIDE YOUR PASSWORD') 
             
            print(colored('DO YOU WANT TO HIDE YOUR PASSWORD (Y/N)  : ','yellow')) 
             
            passwd=input() 
             
            print('\n') 
             
            if passwd=='y' or passwd=='Y': 
                 
                #HIDING PASSWORD 
                 
                voice.Speak('enter your password') 

                print(colored(('ENTER YOUR PASSWORD  : '),'yellow')) 
 
                pwd2=getpass.getpass( ) 
 
                print('\n') 
                 
            else: 
 
                voice.Speak('enter your password') 
             
                print(colored(('ENTER YOUR PASSWORD : '),'yellow')) 
 
                pwd2=input( ) 
 
                print('\n') 
                 
                 
            #CHECKING WHETHER THE USER EXISTS 
                                 
            cursor.execute("select*from customer where uname ='%s' ;"%(uname2)) 
             
            result=cursor.fetchall() 
 
            result_df=pd.DataFrame(result,columns=['fnameE','lname','dob','email_id', 
            'phone','uname','pwd']) 
 
            uname_df=result_df[['uname']] 
 
            un="`,`".join([str(i) for i in uname_df.uname.tolist()]) 
 
            pwd_df=result_df[['pwd']] 
 
            password="`,`".join([str(i) for i in pwd_df.pwd.tolist()]) 
 
            print('\n') 
 
            if uname2==un: 
 
                if pwd2==password: 
 
                    a="n" 
                     
                    j="n" 

                    voice.Speak('you have successfully logged in') 
 
                    print(colored("YOU HAVE SUCCESSFULLY LOGGED IN".center(200),'green')) 
                                                      
                    notification.notify( 
                        title = 'DREAM MART', 
                        message = 'YOU HAVE SUCCESSFULLY LOGGED IN ��',  
                        app_icon =r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                        timeout = 600) 
              
                    print('\n') 
                 
                    display(Image(r'C:\Users\Junaidh\Desktop\Ip project\sign in.png',width="650", height="400")) 
                     
                    print('\n') 
 
                    break 
 
                else: 
                 
                    voice.Speak("YOUR PASSWORD IS INCORRECT") 
 
                    print(colored("YOUR PASSWORD IS INCORRECT",'red')) 
                     
                    print('\n') 
                 
                    voice.Speak('WOULD YOU LIKE TO RETRY ') 
                     
                    print(colored("WOULD YOU LIKE TO RETRY ?? (Y/N)",'yellow')) 
 
                    a=input() 
                     
                    print('\n') 
 
                    if a=="n" or a=="N": 
                         
                        #RESETING PASSWORD 
                     
                        voice.Speak('WOULD YOU LIKE TO RESET YOUR PASSWORD') 
                         
                        print(colored("WOULD YOU LIKE TO RESET YOUR PASSWORD ?? (Y/N)",'yellow')) 
                               
                        w=input( ) 
                               
                        print('\n') 
 
                        if w=='y' or w=='Y': 
 
                            email2="y" 
 
                            while email2=="y" or email2=="Y": 
                               
                                voice.Speak('enter your email i d') 
                               
                                print(colored("ENTER YOUR EMAIL ID","yellow")) 
 
                                email_id2=input() 
 
                                print('\n') 
 
                                email_df=result_df[['email_id']] 
 
                                email="`,`".join([str(i) for i in email_df.email_id.tolist()]) 
                                 
                                #CHECKING WHETHER EMAIL ID EXIST 
 
                                if email_id2==email:         
                                     
                                    #GENERATING OTP 
 
                                    con=random.randint(100000,999999) 
 
                                    cont=str(con) 
                                     
                                    message = 'Subject: {}\n\n{}'.format('OTP FROM DREAM MART', 'ENTER THE OTP FOR VERIFICATION '+cont) 
 
                                    server=smtplib.SMTP('smtp.gmail.com',587) 
 
                                    server.ehlo() 
 
                                    server.starttls() 
 
                                    server.login('dreammart31@gmail.com','dream1331') 

                                    #SENDING OTP 
                                     
                                    server.sendmail('dreammart31@gmail.com',email_id2,message) 
 
                                    server.close() 
                               
                                    voice.Speak('Enter the OTP sent to your email') 
                               
                                    print(colored(('ENTER THE O T P SENT TO YOUR EMAIL' ),'yellow')) 
 
                                    otp=int(input()) 
 
                                    print('\n') 
 
                                    if otp == con: 
 
                                        f='y' 
                                         
                                        #CHANGNG PASSWORD 
 
                                        while f=='y' or f=='Y': 
                               
                                            voice.Speak('DO YOU WANT TO HIDE THE PASSWORD') 
                                             
                                            print(colored('DO YOU WANT TO HIDE THE PASSWORD ??','yellow')) 
                                                                                                                   
                                            password_hide=input( ) 
                                             
                                            print('\n') 
                                             
                                            if password_hide=='y' or password_hide=='Y': 
                                                 
                                                #HIDING PASSWORD 
                               
                                                voice.Speak('enter your new password') 
                                             
                                                print(colored('ENTER YOUR NEW PASSWORD  : ','yellow')) 
 
                                                pa=getpass.getpass( ) 

                                                print('\n') 
                               
                                                voice.Speak('ENTER YOUR NEW PASSWORD AGAIN ') 
                                                 
                                                print(colored('ENTER YOUR NEW PASSWORD AGAIN  : ','yellow')) 
 
                                                pa2=getpass.getpass( ) 
                                                 
                                                print('\n') 
                                                 
                                            else: 
                               
                                                voice.Speak('ENTER YOUR NEW PASSWORD ') 
                                                 
                                                print(colored('ENTER YOUR NEW PASSWORD  : ','yellow')) 
 
                                                pa=input( ) 
 
                                                print('\n') 
                               
                                                voice.Speak('ENTER YOUR NEW PASSWORD AGAIN ') 
                                                 
                                                print(colored('ENTER YOUR NEW PASSWORD AGAIN  : ','yellow')) 
                                                 
                                                pa2=input( ) 
 
                                                print('\n') 
 
                                            if pa==pa2: 
                               
                                                voice.Speak('YOU HAVE SUCCESSFULLY CHANGED YOUR PASSWORD') 
 
                                                print(colored("YOU HAVE SUCCESSFULLY CHANGED YOUR PASSWORD",'red')) 
                                                 
                                                print('\n') 
                               
                                                voice.Speak('YOU HAVE SUCCESSFULLY SIGNED IN') 
 
                                                print(colored("YOU HAVE SUCCESSFULLY SIGNED IN",'green')) 
                                                 
                                                print('\n') 
                                             
                                                display(Image(r'C:\Users\Junaidh\Desktop\Ip project\sign in.png',width="650", height="400")) 
                                                       
                                                print('\n') 
 
                                                val=(pa2,email_id2) 
                                                 
                                                #UPDATING PASSWORD IN DATABASE 
 
                                                cursor.execute("update customer set password=%s where email=%s;",val) 
                                                 
                                                email2='n' 
                                                 
                                                j='n' 
 
                                                break 
 
                                            elif pa != pa2: 
                               
                                                voice.Speak("INNCORRECT PASSWORD") 
 
                                                print("INNCORRECT PASSWORD") 
                                                 
                                                print('\n') 
                               
                                                voice.Speak('TRY AGAIN') 
 
                                                print("TRY AGAIN") 
                                                 
                                                print('\n') 
                               
                                                voice.Speak('would you like to try again') 
                                                 
                                                print(colored("WOULD YOU LIKE TO TRY AGAIN ?? (Y/N)  : " ,'yellow')) 
 
                                                f=input( ) 
 
                                            else: 
                                         
                                                print('\n') 
                                         
                                                break 
                                         
                                    elif otp != con: 
                                 
                                        print(colored("INCORRECT OTP",'red')) 
                                 
                                        print('\n') 
                                     
                                        email2=(input("WOULD YOU LIKE TO TRY AGAIN ?? (Y/N)")) 
                                 
                                        print() 
                            
                                elif email_id2==email: 
                               
                                    voice.Speak('EMAIL ID IS INCORRECT') 
                             
                                    print("EMAIL ID IS INCORRECT") 
                             
                                    print('\n') 
                               
                                    voice.Speak('PLEASE CHECK YOUR USERNAME AND EMAIL I D') 
                             
                                    print(colored("PLEASE CHECK YOUR USERNAME & EMAIL ID",'red')) 
                             
                                    print('\n') 
                               
                                    voice.Speak('would you like to try again') 
                               
                                    print(colored("WOULD YOU LIKE TO TRY AGAIN ?? (Y/N)",'yellow')) 
                             
                                    email=input() 
 
                                    print('\n') 
                             
                        elif w=='n' or w=='N': 
                               
                            voice.Speak('DO YOU WISH TO START FROM THE BEGINNING ') 
                               
                            print(colored("DO YOU WISH TO START FROM THE BEGINNING ?? (Y/N)",'yellow')) 
                         
                            j=input() 
                             
                            print('\n') 
                         
                            break 
                         
                        else: 
                         
                            break 
                         
                    elif uname2 != un: 
                               
                        voice.Speak("INCORRECT USER NAME") 
                     
                        print(colored("INCORRECT USER NAME",'red')) 
                     
                        print('\n') 
                               
                        voice.Speak("WOULD YOU LIKE TO START FROM THE BEGINNING ?? (Y/N)") 
                               
                        print("WOULD YOU LIKE TO START FROM THE BEGINNING ?? (Y/N)") 
                     
                        a=input() 
                               
                        print('\n') 
                     
                    else: 
                               
                        voice.Speak("SOMETHING WENT WRONG") 
                 
                        print(colored("SOMETHING WENT WRONG",'red')) 

                        print('\n') 
                               
                        voice.Speak("WOULD YOU LIKE TO START FROM BEGINNING ") 
                               
                        print(colored("WOULD YOU LIKE TO START FROM BEGINNING ?? (Y/N)")) 
                 
                        j=input() 
                               
                        print('\n')                      
                                                       
# MAIN MENU 
                                                 
 
# CREATING A LOADING APPLICATION 
         
animation = ["LOADING [■□□□□□□□□□]","LOADING [■■□□□□□□□□]", 
"LOADING [■■■□□□□□□□]",  
             "LOADING [■■■■□□□□□□]", "LOADING [■■■■■□□□□□]", "LOADING 
[■■■■■■□□□□]", 
             "LOADING [■■■■■■■□□□]", "LOADING [■■■■■■■■□□]", "LOADING 
[■■■■■■■■■□]",  
             "LOADING [■■■■■■■■■■]"] 
         
for i in range(len(animation)): 
     
    time.sleep(1) 
     
    sys.stdout.write("\r" + animation[i % len(animation)]) 
     
    sys.stdout.flush() 
 
sys.stdout.write('\rDone!                          ') 
         
print('\n') 
 
notification.notify(title = 'DREAM MART', 
                    message = 'ENJOY SHOPPING ��',  
                    app_icon =r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                    timeout = 60) 
     
menu='y' 
 
while menu=='y' or menu=='Y': 
     
    #DISPLAYING THE MAIN MENU 
     
    print(colored('MENU'.center(200),'red')) 
     
    print('\n') 
     
    voice.Speak(' press 1 to know about us ') 
     
    print(colored('1. KNOW ABOUT US'.center(200),'yellow')) 
     
    voice.Speak('press 2 to play mini games') 
     
    print(colored('2. GAME CORNER'.center(200),'yellow')) 
     
    voice.Speak('press 3 to shop') 
     
    print(colored('3. SHOPPING CENTER'.center(200),'yellow')) 
     
    voice.Speak('press 4 to know about the datas of dream mart ') 
     
    print(colored('4. DATA VISUALISATION OF DREAM 
MART'.center(180),'yellow')) 
     
    voice.Speak('press 5 to leave dream mart ') 
     
    print(colored('5. EXIT FROM DREAM MART'.center(200),'yellow')) 
     
    print('\n') 
     
    voice.Speak("ENTER YOUR CHOICE FROM THE MENU ") 
     
    print(colored("ENTER YOUR CHOICE FROM THE MENU  : ",'yellow')) 
     
    menu_choice=int(input( )) 
     
    print('\n') 
     
#ABOUT US 
     
    if menu_choice == 1: 
         
        animation = ["LOADING [■□□□□□□□□□]","LOADING [■■□□□□□□□□]", 
"LOADING [■■■□□□□□□□]",  
             "LOADING [■■■■□□□□□□]", "LOADING [■■■■■□□□□□]", "LOADING 
[■■■■■■□□□□]", 
             "LOADING [■■■■■■■□□□]", "LOADING [■■■■■■■■□□]", "LOADING 
[■■■■■■■■■□]",  
             "LOADING [■■■■■■■■■■]"] 
         
        for i in range(len(animation)): 
     
            time.sleep(1) 
     
            sys.stdout.write("\r" + animation[i % len(animation)]) 
     
            sys.stdout.flush() 
 
        sys.stdout.write('\rDone!                          ') 
         
        print('\n') 
         
        voice.Speak('drem mart makes your grocery shopping even simpler') 
         
        display(Image(r'C:\Users\Junaidh\Desktop\Ip project\about us.png',width="1000", height="500")) 
         
        voice.Speak('our aim is to move shopping into the next stage') 
         
        menu='y' 
          
#GAME CORNER 
     
    elif menu_choice == 2: 
         
        animation = ["LOADING [■□□□□□□□□□]","LOADING [■■□□□□□□□□]", "LOADING [■■■□□□□□□□]",  
             "LOADING [■■■■□□□□□□]", "LOADING [■■■■■□□□□□]", "LOADING [■■■■■■□□□□]", 
             "LOADING [■■■■■■■□□□]", "LOADING [■■■■■■■■□□]", "LOADING [■■■■■■■■■□]",  "LOADING [■■■■■■■■■■]"] 
         
        for i in range(len(animation)): 
     
            time.sleep(1) 
     
            sys.stdout.write("\r" + animation[i % len(animation)]) 
     
            sys.stdout.flush() 
 
        sys.stdout.write('\rDone!                          ') 
         
        print('\n') 
         
         
        #INTRODUCING A VOICE ASSISTANCE FOR GAME CORNER 
                 
        speaker_number=0 
 
        vol=mouth.Dispatch("SAPI.SpVoice") 
 
        v=vol.GetVoices() 
 
        v.Item(speaker_number).GetAttribute("Name") 
 
        vol.voice 
 
        vol.SetVoice(v.Item(speaker_number)) 
         
         
         
        vol.Speak('welcome to game corner') 
         
        display(Image(r'C:\Users\Junaidh\Desktop\Ip project\game 
corner.png',width="1000", height="500")) 
                
        print(colored("WELCOME TO GAME CORNER".center(200),'green')) 
         
        print('\n') 
         
        vol.Speak('i am dweam') 
         
        vol.Speak('i will be guiding you throughout the game corner and play against 
you') 
#34 
 
         
        game='y' 
         
        count=0 
         
        while game=='y' or game=='Y': 
             
            vol.Speak("DO YOU WANT TO VISIT GAME CORNER") 
             
            print(colored("DO YOU WANT TO VISIT GAME CORNER  (Y/N)  : 
",'yellow')) 
             
            gg=input( ) 
             
            print('\n') 
             
            if gg=='y' or gg=='Y': 
                 
                #GAME CORNER MENU 
                 
                print(colored('MENU'.center(150),'red')) 
                 
                print('\n') 
                 
                vol.Speak('press 1 to check your dream coins') 
                 
                print(colored('1. CHECK YOUR DREAM COINS'.center(150),'yellow')) 
                 
                vol.Speak('press 2 to play number guessing') 
                 
                print(colored('2. NUMBER GUESSING'.center(150),'yellow')) 
                 
                vol.Speak('press 3 to play tik tak toe') 
             
                print(colored('3.TIK TAK TOE'.center(150),'yellow')) 
                 
                vol.Speak('press 4 to play rock paper scissors') 
             
                print(colored('4. ROCK,PAPER & SCISSORS'.center(150),'yellow')) 
                 
                vol.Speak('press 5 to toss') 
             
                print(colored('5. HEADS OR TAILS'.center(150),'yellow')) 
                 
#35 
 
                vol.Speak('press 6 to play dice rolling') 
             
                print(colored('6. DICE ROLLING'.center(150),'yellow')) 
                 
                vol.Speak('press 7 to play hangman') 
                 
                print(colored('7. HANGMAN'.center(150),'yellow')) 
                 
                vol.Speak('press 8 to play hand cricket') 
                 
                print(colored('8. HAND CRICKET'.center(150),'yellow')) 
                 
                print('\n') 
                 
                vol.Speak('ENTER THE GAME YOU WANT TO PLAY ') 
             
                print(colored("ENTER THE GAME YOU WANT TO PLAY  : ",'yellow')) 
                 
                game_choice=int(input( )) 
                 
                print('\n') 
                 
                                     
#CHECKING DREAM COINS 
                 
                if game_choice==1: 
                     
                    vol.Speak('your dream coins') 
                     
                    print(colored("YOUR DREAM COINS :",'yellow')) 
                     
                    print(count) 
                     
                    print('\n') 
                     
                    vol.Speak('do you want to withdraw your dream coins') 
                     
                    print(colored("DO YOU WANT TO WITHDRAW YOUR DREAM 
COINS",'green')) 
                     
                    vol.Speak('note if you exit from game corner your dream coins reset') 
                     
                    print(colored("NOTE : IF YOU EXIT FROM GAME CORNER YOUR 
DREAM COINS RESET",'cyan'))    
#36 
 
                     
                    coin=input() 
                     
                    print('\n') 
                     
                    if coin=='y' or coin=='Y': 
                         
                        if count==0: 
                             
                            vol.Speak('YOU HAVE NOT EARNED ANY DREAM COIN') 
                             
                            print(colored('YOU HAVE NOT EARNED ANY DREAM 
COIN','red')) 
                             
                            print('\n') 
                             
                            vol.Speak('PLAY GAMES TO EARN DREAM COIN') 
                             
                            print('\n') 
                             
                            print(colored('PLAY GAMES TO EARN DREAM COIN','red')) 
                             
                            print('\n') 
                             
                            gg='y' 
                             
                        #CONVERTING DREAM COINS INTO DISCOUNT COUPON 
                             
                        elif count>0 and count<501: 
                             
                            #10% DISCOUNT COUPON 
                             
                            print(colored("YOU HAVE ",'red'),count,colored(" DREAM 
COINS",'red')) 
                             
                            print('\n') 
                             
                            vol.Speak('congratulation you got 10 percent off') 
                             
                            print(colored('YOU GOT 10% OFF ���','yellow')) 
                             
                            notification.notify(title = 'DREAM MART', 
                                                message = 'YOU GOT 10% OFF  ��',    
#37 
 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",   
                                                timeout = 1000) 
                             
                            print('\n') 
                             
                            print(colored('ENTER YOUR MAIL ID','yellow')) 
                             
                            email=input() 
                             
                            print('\n') 
                             
                            message = 'Subject: {}\n\n{}'.format('A GIFT FROM DREAM 
MART','ENTER DC10 TO GET 10% OFF IN YOUR FINAL BILL' ) 
                             
                            server=smtplib.SMTP('smtp.gmail.com',587) 
                             
                            server.ehlo() 
                             
                            server.starttls() 
                             
                            server.login('dreammart31@gmail.com','dream1331') 
                             
                            server.sendmail('dreammart31@gmail.com',email,message) 
                             
                            server.close() 
                             
                            vol.Speak('enter the code sent to your mail to get 10 percent off') 
                               
                            print("✨",colored('ENTER THE CODE SENT TO YOUR MAIL 
TO GET 10% OFF','red'),"✨") 
                             
                            print('\n') 
                             
                            notification.notify(title = 'DREAM MART', 
                                                message = 'CHECK YOUR MAIL��',    
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",   
                                                timeout = 1000) 
                             
                            vol.Speak('check you mail') 
                             
                            print(colored('CHECK YOU MAIL','red')) 
                             
#38 
 
                            print('\n') 
                             
                        elif count>501 and count<1001: 
                             
                            #15% DICOUNT COUPON 
                             
                            print("YOU HAVE ",count," DREAM COINS") 
                             
                            print('\n') 
                             
                            vol.Speak('you got 15 percent off') 
                             
                            print('YOU GOT 15% OFF ���') 
                             
                            notification.notify(title = 'DREAM MART', 
                                                message = 'YOU GOT 15% OFF ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 1000) 
                             
                            print('\n') 
                             
                            print(colored('ENTER YOUR MAIL ID','yellow')) 
                             
                            email=input() 
                             
                            print('\n') 
                             
                            message = 'Subject: {}\n\n{}'.format('A GIFT FROM DREAM 
MART','ENTER DC10 TO GET 15% OFF IN YOUR FINAL BILL' ) 
                             
                            server=smtplib.SMTP('smtp.gmail.com',587) 
                             
                            server.ehlo() 
                             
                            server.starttls() 
                             
                            server.login('dreammart31@gmail.com','dream1331') 
                             
                            server.sendmail('dreammart31@gmail.com',email,message) 
                             
                            server.close() 
                             
                            vol.Speak('enter the code sent to your mail to get 15 percent off') 
#39 
 
                               
                            print("✨",colored('ENTER THE CODE SENT TO YOUR MAIL 
TO GET 15% OFF','red'),"✨") 
                             
                            print('\n') 
                             
                            notification.notify(title = 'DREAM MART', 
                                                message = 'CHECK YOUR MAIL��',    
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",   
                                                timeout = 1000) 
                             
                            vol.Speak('check you mail') 
                             
                            print(colored('CHECK YOU MAIL','red')) 
                             
                            print('\n') 
                                                         
                        elif count>1001: 
                             
                            #25% DISCOUNT COUPON 
                             
                            print("YOU HAVE ",count," DREAM COINS") 
                             
                            print('\n') 
                             
                            vol.Speak('you got 25 percent off') 
                             
                            print('YOU GOT 25% OFF ���') 
                             
                            notification.notify(title = 'DREAM MART', 
                                                message = 'YOU GOT 25% OFF��',   
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",   
                                                timeout = 1000) 
                             
                            print('\n') 
                                                         
                            print(colored('ENTER YOUR MAIL ID','yellow')) 
                             
                            email=input() 
                             
                            print('\n') 
                             
#40 
 
                            message = 'Subject: {}\n\n{}'.format('A GIFT FROM DREAM 
MART','ENTER DC10 TO GET 25% OFF IN YOUR FINAL BILL' ) 
                             
                            server=smtplib.SMTP('smtp.gmail.com',587) 
                             
                            server.ehlo() 
                             
                            server.starttls() 
                             
                            server.login('dreammart31@gmail.com','dream1331') 
                             
                            server.sendmail('dreammart31@gmail.com',email,message) 
                             
                            server.close() 
                             
                            vol.Speak('enter the code sent to your mail to get 25 percent off') 
                               
                            print("✨",colored('ENTER THE CODE SENT TO YOUR MAIL 
TO GET 25% OFF','red'),"✨") 
                             
                            print('\n') 
                             
                            notification.notify(title = 'DREAM MART', 
                                                message = 'CHECK YOUR MAIL��',    
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",   
                                                timeout = 1000) 
                             
                            vol.Speak('check you mail') 
                             
                            print(colored('CHECK YOU MAIL','red')) 
                             
                            print('\n') 
                               
                elif game_choice==2: 
                     
                 
#NUMBER GUESSING GAME 
                     
                 
                    c='y' 
 
                    while c=='y': 
                         
#41 
 
                        vol.Speak("Enter a number between 1 to 10") 
                     
                        print(colored("ENTER A NUMBER BETWEEN (1-10) : ",'yellow')) 
     
                        n=int(input()) 
         
                        print('\n') 
         
                        z=random.randint(1,10) 
     
                        print(z) 
     
                        print('\n') 
     
                        if n==z: 
             
                            vol.Speak('you won') 
             
                            print(colored("YOU WON!!",'red')) 
                 
                            print("���") 
                     
                            print('\n') 
                         
                            vol.Speak('check your dream coins') 
                               
                            print(colored("CHECK YOUR DREAM COINS",'red')) 
                             
                            notification.notify(title = 'DREAM MART', 
                                                message = 'CHECK YOUR DREAM COINS ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 600) 
                 
                            count+=1000 
         
                            break 
     
                        elif n>10: 
             
                            vol.Speak("enter a number between 1 to 10") 
         
                            print(colored("ENTER A NUMBER BETWEEN 1-10...",'red')) 
             
#42 
 
                            print('\n') 
         
                            c='y' 
     
                        else: 
             
                            vol.Speak("oops you lost better luck next time") 
         
                            print(colored("YOU LOST BETTER LUCK NEXT TIME",'red')) 
             
                            print('\n') 
                 
                            print(colored("DO YOU WANT TO CONTINE ?? (Y/N) 
",'yellow')) 
     
                            c=input() 
         
                            print('\n') 
             
             
         
                elif game_choice==3: 
                 
             
#TIK TAK TOE 
                 
                    board = [' ' for x in range(10)] 
                 
                    def insertLetter(letter, pos): 
                     
                        board[pos] = letter 
 
                    def spaceIsFree(pos): 
                     
                        return board[pos] == ' ' 
                     
                    #PRINTING BOARD 
 
                    def printBoard(board): 
                     
                        print('   ' + board[1] + ' | ' + board[2] + ' | ' + board[3]) 
                     
                        print('__  __ __ ') 
                     
#43 
 
                        print('   ' + board[4] + ' | ' + board[5] + ' | ' + board[6]) 
                     
                        print('__  __ __ ') 
                     
                        print('   ' + board[7] + ' | ' + board[8] + ' | ' + board[9]) 
                     
                    def isWinner(bo, le): 
                     
                        return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le 
and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == 
le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] 
== le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) 
or(bo[3] == le and bo[5] == le and bo[7] == le) 
 
                    def playerMove(): 
                     
                        run = True 
                     
                        while run: 
                             
                            vol.Speak('Please select a position to place X : ') 
                             
                            print(colored("PLEASE SELECT A POSITION TO PLACE X (1
9)",'yellow')) 
                         
                            move = input( ) 
                             
                            print('\n') 
                         
                            try: 
                             
                                move = int(move) 
                             
                                if move > 0 and move < 10: 
                                 
                                    if spaceIsFree(move): 
                                     
                                        run = False 
                                     
                                        insertLetter('X', move) 
                                     
                                    else: 
                                         
                                        vol.Speak('Sorry, this space is occupied') 
#44 
 
                                         
                                        print(colored('SORRY, THIS SPACE IS OCCUPIED 
!','red')) 
                                         
                                        print('\n') 
                             
                                else: 
                                     
                                    vol.Speak('Please type a number within the range') 
                                 
                                    print(colored('PLEASE TYPE A NUMBER WITHIN THE 
RANGE !','red')) 
                                     
                                    print('\n') 
                                 
                            except: 
                                 
                                vol.Speak('please type a number') 
                             
                                print(colored('PLEASE TYPE A NUMBER !','red')) 
                                 
                                print('\n') 
                 
                    def compMove(): 
                     
                        possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and 
x != 0] 
                     
                        move = 0 
 
                        for let in ['O', 'X']: 
                         
                            for i in possibleMoves: 
                             
                                boardCopy = board[:] 
                             
                                boardCopy[i] = let 
                             
                                if isWinner(boardCopy, let): 
                 
                                    move = i 
                                 
                                    return move 
 
#45 
 
                        cornersOpen = [] 
                     
                        for i in possibleMoves: 
                         
                            if i in [1,3,7,9]: 
             
                                cornersOpen.append(i) 
             
                        if len(cornersOpen) > 0: 
         
                            move = selectRandom(cornersOpen) 
         
                            return move 
 
                        if 5 in possibleMoves: 
                 
                            move = 5 
         
                            return move 
 
                        edgesOpen = [] 
     
                        for i in possibleMoves: 
         
                            if i in [2,4,6,8]: 
             
                                edgesOpen.append(i) 
             
                        if len(edgesOpen) > 0: 
                         
                            move = selectRandom(edgesOpen) 
         
                        return move 
 
                    def selectRandom(li): 
                 
                        ln = len(li) 
     
                        r = random.randrange(0,ln) 
     
                        return li[r] 
     
                    def isBoardFull(board): 
     
#46 
 
                        if board.count(' ') > 1: 
         
                            return False 
     
                        else: 
         
                            return True 
 
                    def main(): 
     
                        print(colored('WELCOME TO TIK TAK TOE!','cyan')) 
         
                        print('\n') 
     
                        printBoard(board) 
 
                        while not(isBoardFull(board)): 
         
                            if not(isWinner(board, 'O')): 
             
                                playerMove() 
             
                                printBoard(board) 
         
                            else: 
                 
                                vol.Speak('sorry O won this time') 
             
                                print(colored('SORRY O WON THIS TIME !','red')) 
                 
                                print('\n') 
             
                                break 
 
                            if not(isWinner(board, 'X')): 
             
                                move = compMove() 
             
                                if move == 0: 
                     
                                    vol.Speak('game tied') 
                 
                                    print(colored('TIE GAME !','red')) 
                     
#47 
 
                                    print('\n') 
             
                                else: 
                 
                                    insertLetter('O', move) 
                     
                                    vol.Speak("computer placed O") 
                 
                                    print(colored('COMPUTER PLACED AN \'O\' IN 
POSITION','yellow') 
                                          , move , ' : ') 
                     
                                    print('\n') 
                 
                                    printBoard(board) 
         
                            else: 
                 
                                vol.Speak('congratulation you won ') 
                                print(colored('X\'s WON THIS TIME ! GOOD JOB ! ��� 
','red')) 
                 
                                print('\n') 
                             
                                break 
 
                        if isBoardFull(board): 
                             
                            vol.Speak('game tied') 
         
                            print(colored('TIE GAME','red')) 
             
                            print('\n') 
 
                    while True: 
                         
                        vol.Speak('Do you want to play tik tac toe') 
                         
                        print(colored('DO YOU WANT TO PLAY TIK TAK TOE ?? (Y/N) 
','yellow')) 
                     
                        answer = input() 
                         
                        print('\n') 
#48 
 
     
                        if answer.lower() == 'y': 
         
                            board = [' ' for x in range(10)] 
         
                            print('-----------------------------------') 
         
                            main() 
                     
                        else: 
         
                            break 
                 
 
                elif game_choice==4: 
                     
                 
#ROCK,PAPER & SCISSORS 
                 
                    rps='y' 
 
                    while rps=='y' or rps=='Y': 
                         
                        vol.Speak("enter r for rock p for paper and s for scissors") 
     
                        print(colored("ENTER ROCK(R) , PAPER(P) OR 
SCISSORS(S)",'yellow')) 
     
                        rps1 = input( ) 
     
                        possible_actions = ["r", "p", "s"] 
     
                        computer_action = random.choice(possible_actions) 
     
                        if rps1=='r' or rps1=='R': 
         
                            if computer_action=='s': 
             
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\rp3.png',width="550", height="400")) 
                 
                                print('\n') 
                 
                                vol.Speak('you won') 
#49 
 
            
                                print(colored("YOU WON",'red')," ���") 
                 
                                print('\n') 
                 
                                count+=300 
                     
                                vol.Speak('check your dream coins') 
                     
                                print(colored("CHECK YOUR DREAM COINS",'red')) 
                         
                                notification.notify(title = 'DREAM MART', 
                                                message = 'CHECK YOUR DREAM COINS ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 600)                         
                                 
                                print('\n') 
                           
                                break 
             
                            elif computer_action=='r': 
                           
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\rps2.png',width="550", height="400")) 
                             
                                vol.Speak("THE MATCH DRAWED") 
                           
                                print(colored("THE MATCH DRAWED",'red')) 
                             
                                print('\n') 
                             
                                vol.Speak('DO YOU WANT TO PLAY AGAIN') 
                           
                                print(colored("DO YOU WANT TO PLAY AGAIN (Y/N)  : 
",'yellow')) 
                           
                                rps=input() 
                             
                                print('\n') 
             
                            else: 
             
#50 
 
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\rps5.png',width="550", height="400")) 
                 
                                vol.Speak('you lost') 
             
                                print(colored("YOU LOST",'red')) 
                 
                                print('\n') 
                     
                                vol.Speak('DO YOU WANT TO PLAY AGAIN') 
                           
                                print(colored("DO YOU WANT TO PLAY AGAIN (Y/N)  : 
",'yellow')) 
                           
                                rps=input() 
                             
                                print('\n') 
     
                        elif rps1=='s' or rps1=='S': 
                           
                            if computer_action=='s': 
                           
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\rps8.png',width="550", height="400")) 
                           
                                vol.Speak("THE MATCH DRAWED") 
                         
                                print(colored("THE MATCH DRAWED",'red')) 
                             
                                print('\n') 
                             
                                vol.Speak("DO YOU WANT TO PLAY AGAIN") 
                           
                                print(colored("DO YOU WANT TO PLAY AGAIN (Y/N)  : 
",'yellow')) 
             
                                rps=input()  
                 
                                print('\n') 
                           
                            elif computer_action=='r': 
                           
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\rps4.png',width="550", height="400")) 
#51 
 
                           
                                vol.Speak('you lost') 
                             
                                print(colored("YOU LOST",'red')) 
                                 
                                print('\n') 
                                 
                                vol.Speak("do you want to play again") 
                           
                                print(colored("DO YOU WANT TO PLAY AGAIN (Y/N)  : 
",'yellow')) 
                           
                                rps=input() 
                           
                                print('\n') 
                             
                             
                            else: 
             
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\rps9.png',width="550", height="400")) 
                 
                                vol.Speak('you won') 
                           
                                print(colored("YOU WON",'red')," ���") 
                             
                                print('\n') 
                             
                                vol.Speak('check your dream coins') 
                     
                                print(colored("CHECK YOUR DREAM COINS",'red')) 
                         
                                notification.notify(title = 'DREAM MART', 
                                                message = 'CHECK YOUR DREAM COINS ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 600) 
                                         
                         
                                print('\n') 
                         
                                count+=300 
                           
                                break 
#52 
 
                             
                           
                        else: 
         
                            if computer_action=='s': 
             
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\rps1.png',width="550", height="400")) 
                           
                                print(colored("YOU LOST",'red')) 
                         
                                print('\n') 
                           
                                print(colored("DO YOU WANT TO PLAY AGAIN (Y/N)  : 
",'yellow')) 
                           
                                rps=input() 
                                       
                                print('\n') 
                                       
                            elif computer_action=='r': 
                           
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\rps7.png',width="550", height="400")) 
                             
                                vol.Speak('you won') 
                           
                                print(colored("YOU WON",'red')," ���") 
                                       
                                print('\n')  
                             
                                vol.Speak('check your dream coins') 
                     
                                print(colored("CHECK YOUR DREAM COINS",'red')) 
                         
                                notification.notify(title = 'DREAM MART', 
                                                message = 'CHECK YOUR DREAM COINS ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 600) 
                 
                        
                                print('\n') 
                             
#53 
 
                                count+=300 
                           
                                break 
                                       
                           
                            else: 
             
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\rps6.png',width="550", height="400")) 
                 
                                vol.Speak("THE MATCH DRAWED") 
                           
                                print(colored("THE MATCH DRAWED",'red')) 
                             
                                print('\n') 
                             
                                vol.Speak("DO YOU WANT TO PLAY AGAIN") 
                           
                                print(colored("DO YOU WANT TO PLAY AGAIN (Y/N)  : 
",'yellow')) 
                           
                                rps=input() 
                             
                                print('\n') 
                                       
                     
                elif game_choice==5:  
                     
                 
#HEADS OR TAILS 
                 
                    ht4='y' 
 
                    while ht4=='y' or ht4=='Y': 
                                       
                        vol.Speak('enter h for heads ') 
                                       
                        vol.Speak('enter t for tails') 
                                       
                        print(colored("ENTER HEADS(H) OR TAILS(T)  : ",'yellow')) 
                         
                        ht=input() 
                                       
                        print('\n') 
#54 
 
 
                        ht2=['h','t'] 
 
                        ht1=random.choice(ht2) 
                         
                        if ht=='h' or ht=='H': 
     
                            if ht1=='h': 
         
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\heads.png',width="650", height="400")) 
                                       
                                vol.Speak("You won") 
         
                                print(colored("YOU WON",'red'),"���") 
             
                                notification.notify(title = 'DREAM MART', 
                                            message = 'CHECK YOUR DREAM COINS ��', 
                                            app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                            timeout = 600) 
                 
                                       
                                print('\n') 
             
                                count+=100 
                                       
                                vol.Speak("Do u wanna continue") 
                                       
                                print(colored("DO YOU WANT TO CONTINUE  : ",'yellow')) 
             
                                ht4=input() 
                                       
                                print('\n') 
         
                            else: 
         
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\tail.png',width="650", height="400")) 
                                       
                                vol.Speak("You lost") 
                                       
                                print(colored("YOU LOST",'red')) 
                                       
#55 
 
                                print('\n') 
                                       
                                vol.Speak("Do u wanna continue") 
                                       
                                print(colored("DO YOU WANT TO CONTINUE  : ",'yellow')) 
             
                                ht4=input() 
                                       
                                print('\n') 
         
                        elif ht=='t' or ht=='T': 
     
                            if ht1=='h': 
         
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\heads.png',width="650", height="400")) 
         
                                vol.Speak("You lost") 
                                       
                                print(colored("YOU LOST",'red')) 
                                       
                                print('\n') 
                                       
                                vol.Speak("Do u wanna continue") 
                                       
                                print(colored("DO YOU WANT TO CONTINUE  : ",'yellow')) 
             
                                ht4=input() 
                                       
                                print('\n') 
         
                            else: 
         
                                display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\tail.png',width="650", height="400")) 
         
                                vol.Speak("You won") 
         
                                print(colored("YOU WON",'red'),"���") 
             
                                notification.notify(title = 'DREAM MART', 
                                                message = 'CHECK YOUR DREAM COINS ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
#56 
 
                                                timeout = 600) 
                 
                                       
                                print('\n') 
             
                                count+=100 
                                       
                                vol.Speak("Do u wanna continue") 
                                       
                                print(colored("DO YOU WANT TO CONTINUE  : ",'yellow')) 
             
                                ht4=input() 
                                       
                                print('\n') 
 
     
                elif game_choice==6: 
             
             
#DICE ROLLING 
                                       
                    player1_score = 0 
 
                    player2_score = 0 
 
                    for i in range(5): 
     
                        player1_value = random.randint(1, 6) 
     
                        player2_value = random.randint(1, 6) 
                                       
                        vol.Speak('Computer rolled') 
     
                        print(colored(" COMPUTER ROLLED  : ",'yellow')) 
                                       
                        print( player1_value) 
                                       
                        print('\n') 
                                       
                        vol.Speak("You rolled ") 
                                       
                        print(colored("YOU ROLLED  : ",'yellow')) 
     
                        print(player2_value) 
#57 
 
                                       
                        print('\n') 
     
                        if player1_value > player2_value: 
                                       
                            vol.Speak("Computer won") 
         
                            print(colored("COMPUTER WON ",'red')) 
                                       
                            print('\n') 
         
                            player1_score = player1_score + 1   
     
                        elif player2_value > player1_value: 
         
                            vol.Speak("You won") 
                                       
                            print(colored("YOU WON",'red')) 
                                       
                            print('\n') 
         
                            player2_score = player2_score + 1 
     
                        else: 
                                                                             
                            vol.Speak("It's a draw") 
                                       
                            print(colored("IT'S A DRAW",'red')) 
                                       
                            print('\n') 
                                       
                        vol.Speak("Press enter to continue.")     
 
                        input("PRESS ENTER TO CONTINUE")   
                                       
                        print('\n') 
                                       
                    vol.Speak('game over') 
 
                    print(colored("### Game Over ###".center(200),'red')) 
                                       
                    vol.Speak("Computer's score") 
 
                    print(colored("COMPUTER'S SCORE",'red'), player1_score) 
#58 
 
                                       
                    print('\n') 
                                       
                    vol.Speak("Your score") 
 
                    print(colored("YOUR SCORE ",'red'), player2_score) 
                                       
                    print('\n') 
                     
                    if player1_score < player2_score: 
                                       
                        vol.Speak('you won') 
                         
                        print(colored("YOU WON ",'red')) 
                             
                        print("���") 
                         
                        notification.notify(title = 'DREAM MART', 
                                                message = 'CHECK YOUR DREAM COINS ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 600) 
                 
                                       
                        print('\n') 
                         
                        count+=200 
                         
                    else: 
                     
                        vol.Speak('you lost') 
                         
                        print("YOU LOST :(  ") 
                                       
                        print('\n') 
                         
                                                   
                if game_choice==7: 
                     
                     
#HANGMAN 
                                       
                    vol.Speak('press 1 to find marvel characters') 
                                       
#59 
 
                    print(colored("1. MARVEL CHARACTERS",'yellow')) 
                                       
                    vol.Speak('press 2 to find indian cricketers name') 
                     
                    print('\n') 
                                       
                    print(colored("2. INDIAN CRICKETERS ",'yellow')) 
                                       
                    print('\n') 
                                       
                    print(colored("ENTER YOUR CHOICE  : ",'yellow')) 
                                       
                    hang=int(input()) 
                                       
                    print('\n') 
                                       
                    if hang==1: 
                                       
                        def hangman(): 
                         
                            word = random.choice(["ironman" ,  
                                                  "hulk" , 
                                                  "thor" , 
                                                  "captainamerica" , 
                                                  "clint" , "loki" , 
                                                  "blackwidow", 
                                                  "spiderman","vision", 
                                                  "captianmarvel"]) 
                         
                            validLetters = 'abcdefghijklmnopqrstuvwxyz' 
                     
                            turns = 10 
                         
                            guessmade = '' 
 
                            while len(word) > 0: 
                             
                                main = "" 
                             
                                missed = 0 
 
                                for letter in word: 
                                 
                                    if letter in guessmade: 
#60 
 
                                     
                                        main = main + letter 
                                 
                                    else: 
                                     
                                        main = main + "_" + " " 
                             
                                if main == word: 
                                 
                                    print(main) 
                                       
                                    vol.Speak('you won') 
                                 
                                    print(colored("YOU WON",'red')) 
                                       
                                    print('\n') 
                                 
                                    break 
                                       
                                vol.Speak('guess the word') 
 
                                print(colored("GUESS THE WORD : ",'yellow') , main) 
                             
                                guess = input() 
                                       
                                print('\n') 
 
                                if guess in validLetters: 
                                 
                                    guessmade = guessmade + guess 
                             
                                else: 
                                       
                                    vol.Speak("Enter a valid character") 
                                 
                                    print(colored("ENTER A VALID CHARACTER",'red')) 
                                       
                                    print('\n') 
                                       
                                    vol.Speak("capital letters are invalid") 
                                       
                                    print(colored("CAPITAL LETTERS ARE INVALID",'red')) 
                                 
                                    guess = input() 
#61 
 
                                       
                                    print('\n') 
 
                                if guess not in word: 
                                 
                                    turns = turns - 1 
                                 
                                    if turns == 9: 
                                       
                                        vol.Speak("9 turns left") 
                                     
                                        print(colored("9 TURNS LEFT",'red')) 
                                       
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 8: 
                                       
                                        vol.Speak("8 turns left") 
                                     
                                        print(colored("8 TURNS LEFT",'red')) 
                                       
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("     O      ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 7: 
                                       
                                        vol.Speak("7 turns left") 
                                     
                                        print(colored("7 TURNS LEFT",'red')) 
                                       
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("     O      ") 
#62 
 
                                     
                                        print("     |      ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 6: 
                                     
                                        vol.Speak("6 turns left") 
                                     
                                        print(colored("6 TURNS LEFT",'red')) 
                                       
                                        print('\n') 
                                         
                                        print("  --------  ") 
                                     
                                        print("     O      ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    /       ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 5: 
                                     
                                        vol.Speak("5 turns left") 
                                     
                                        print(colored("5 TURNS LEFT",'red')) 
                                     
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("     O      ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 4: 
                                     
                                        vol.Speak("4 turns left") 
#63 
 
                                     
                                        print(colored("4 TURNS LEFT",'red')) 
                                     
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("   \ O      ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 3: 
                                     
                                        vol.Speak("3 turns left") 
                                     
                                        print(colored("3 TURNS LEFT",'red')) 
                                     
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("   \ O /    ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 2: 
                                     
                                        vol.Speak("2 turns left") 
                                     
                                        print(colored("2 TURNS LEFT",'red')) 
                                     
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("   \ O /|   ") 
#64 
 
                                     
                                        print("     |      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 1: 
                                     
                                        vol.Speak("1 turns left") 
                                     
                                        print(colored("1 TURNS LEFT",'red')) 
                                     
                                        print('\n') 
                                     
                                        vol.Speak("Last breaths counting Take care") 
                                       
                                        print(colored("LAST BREATHS COUNTING. TAKE 
CARE ! ",'red')) 
                                       
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("   \ O_|/   ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 0: 
                                     
                                        vol.Speak("You lost") 
                                       
                                        print(colored("YOU LOST",'red')) 
                                       
                                        print('\n') 
                                     
                                        vol.Speak("You let a kind and poor man die") 
                                       
                                        print(colored("YOU LET A KIND AND POOR MAN 
DIE"),'cyan') 
#65 
 
                                       
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("     O_|    ") 
                                     
                                        print("    /|\      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                     
                                        break 
                                       
                        vol.Speak("WELCOME TO HANGMAN") 
                                     
                        print(colored("*",'red')*150) 
 
                        print(colored("WELCOME TO HANGMAN".center(200),'yellow')) 
                     
                        print(colored("*",'red')*150) 
                                       
                        print('\n') 
                                       
                        vol.Speak("try to guess the word in less than 10 attempts") 
                     
                        print(colored("TRY TO GUESS THE WORD IN LESS THAN 10 
ATTEMPTS",'red')) 
                     
                        print('\n')   
                                       
                        vol.Speak("type the letters in small case") 
                                       
                        print(colored("TYPE THE LETTERS IN SMALL CASE",'yellow')) 
                                       
                        print('\n') 
                                       
                        hangman() 
 
                    elif hang==2: 
                                       
                        def hangman(): 
                         
#66 
 
                            word = random.choice(["viratkholi" ,  
                                                  "rohitsharma" , 
                                                  "msdhoni" , 
                                                  "klrahul" , 
                                                  "rishabhpant" ,  
                                                  "jaspritbumrah" , 
                                                  "jadeja", 
                                                  "ashwin","hardik"]) 
                         
                            validLetters = 'abcdefghijklmnopqrstuvwxyz' 
                     
                            turns = 10 
                         
                            guessmade = '' 
 
                            while len(word) > 0: 
                             
                                main = "" 
                             
                                missed = 0 
 
                                for letter in word: 
                                 
                                    if letter in guessmade: 
                                     
                                        main = main + letter 
                                 
                                    else: 
                                     
                                        main = main + "_" + " " 
                             
                                if main == word: 
                                 
                                    print(main) 
                                       
                                    vol.Speak('you won') 
                                 
                                    print(colored("YOU WON",'red')) 
                                       
                                    print('\n') 
                                 
                                    break 
                                       
                                vol.Speak('guess the word') 
#67 
 
 
                                print(colored("GUESS THE WORD : ",'yellow') , main) 
                             
                                guess = input() 
                                       
                                print('\n') 
 
                                if guess in validLetters: 
                                 
                                    guessmade = guessmade + guess 
                             
                                else: 
                                       
                                    vol.Speak("Enter a valid character") 
                                 
                                    print(colored("ENTER A VALID CHARACTER",'red')) 
                                       
                                    print('\n') 
                                       
                                    vol.Speak("capital letters are invalid") 
                                       
                                    print(colored("CAPITAL LETTERS ARE INVALID",'red')) 
                                 
                                    guess = input() 
                                       
                                    print('\n') 
 
                                if guess not in word: 
                                 
                                    turns = turns - 1 
                                 
                                    if turns == 9: 
                                       
                                        vol.Speak("9 turns left") 
                                     
                                        print(colored("9 TURNS LEFT",'red')) 
                                       
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 8: 
#68 
 
                                       
                                        vol.Speak("8 turns left") 
                                     
                                        print(colored("8 TURNS LEFT",'red')) 
                                       
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("     O      ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 7: 
                                       
                                        vol.Speak("7 turns left") 
                                     
                                        print(colored("7 TURNS LEFT",'red')) 
                                       
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("     O      ") 
                                     
                                        print("     |      ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 6: 
                                     
                                        vol.Speak("6 turns left") 
                                     
                                        print(colored("6 TURNS LEFT",'red')) 
                                       
                                        print('\n') 
                                         
                                        print("  --------  ") 
                                     
                                        print("     O      ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    /       ") 
#69 
 
                                       
                                        print('\n') 
                                 
                                    if turns == 5: 
                                     
                                        vol.Speak("5 turns left") 
                                     
                                        print(colored("5 TURNS LEFT",'red')) 
                                     
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("     O      ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 4: 
                                     
                                        vol.Speak("4 turns left") 
                                     
                                        print(colored("4 TURNS LEFT",'red')) 
                                     
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("   \ O      ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 3: 
                                     
                                        vol.Speak("3 turns left") 
                                     
                                        print(colored("3 TURNS LEFT",'red')) 
#70 
 
                                     
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("   \ O /    ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 2: 
                                     
                                        vol.Speak("2 turns left") 
                                     
                                        print(colored("2 TURNS LEFT",'red')) 
                                     
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("   \ O /|   ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 1: 
                                     
                                        vol.Speak("1 turns left") 
                                     
                                        print(colored("1 TURNS LEFT",'red')) 
                                     
                                        print('\n') 
                                     
                                        vol.Speak("Last breaths counting Take care") 
                                       
                                        print(colored("LAST BREATHS COUNTING. TAKE 
CARE ! ",'red')) 
                                       
#71 
 
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("   \ O_|/   ") 
                                     
                                        print("     |      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                 
                                    if turns == 0: 
                                     
                                        vol.Speak("You lost") 
                                       
                                        print(colored("YOU LOST",'red')) 
                                       
                                        print('\n') 
                                     
                                        vol.Speak("You let a kind and poor man die") 
                                       
                                        print(colored("YOU LET A KIND AND POOR MAN 
DIE"),'cyan') 
                                       
                                        print('\n') 
                                     
                                        print("  --------  ") 
                                     
                                        print("     O_|    ") 
                                     
                                        print("    /|\      ") 
                                     
                                        print("    / \     ") 
                                       
                                        print('\n') 
                                     
                                        break 
                                       
                        vol.Speak("WELCOME TO HANGMAN") 
                                     
                        print(colored("*",'red')*150) 
 
                        print(colored("WELCOME TO HANGMAN".center(200),'yellow')) 
#72 
 
                     
                        print(colored("*",'red')*150) 
                                       
                        print('\n') 
                                       
                        vol.Speak("try to guess the word in less than 10 attempts") 
                     
                        print(colored("TRY TO GUESS THE WORD IN LESS THAN 10 
ATTEMPTS"),'red') 
                     
                        print('\n')   
                                       
                        vol.Speak("type the letters in small case") 
                                       
                        print(colored("TYPE THE LETTERS IN SMALL CASE",'yellow')) 
                                       
                        print('\n') 
                                       
                        hangman() 
 
                if game_choice==8:  
                     
                     
#HAND-CRICKET 
                     
                    lst1= [1,2,3,4,5,6] 
 
                    chances_1= 18 
 
                    no_of_chances_1= 0 
 
                    your_runs= 0 
                     
                    print(colored('*','blue')*150) 
                     
                    vol.Speak("YOUR BATTING") 
  
                    print(colored("YOUR BATTING".center(200),'cyan')) 
 
                    print(colored('*','blue')*150)     
     
                    print('\n') 
 
                    while no_of_chances_1 < chances_1: 
#73 
 
                 
                        vol.Speak("Enter Runs for Your Batting Turn") 
                 
                        print(colored("ENTER RUNS FOR YOUR BATTING TURN  : 
",'yellow')) 
     
                        runs= int(input()) 
         
                        print('\n') 
     
                        comp_bowl= random.choice(lst1) 
 
                        if runs==comp_bowl: 
                 
                            vol.Speak('your guess') 
                 
                            print(colored("YOUR GUESS :",'yellow')) 
         
                            print (runs) 
             
                            print('\n') 
                 
                            vol.Speak('computer guess') 
                 
                            print(colored("COMPUTER GUESS :",'yellow')) 
                     
                            print(comp_bowl) 
                         
                            print('\n') 
                             
                            vol.Speak('you are out') 
                             
                            print(colored("YOU ARE OUT",'red')) 
                             
                            print('\n') 
                             
                            vol.Speak('your total runs') 
                             
                            print(colored("YOUR TOTAL RUNS",'red')) 
                             
                            print(your_runs) 
                             
                            print ("\n") 
         
#74 
 
                            break 
     
                        elif runs>6: 
             
                            vol.Speak('enter a number between 1 to 6') 
         
                            print(colored("ALERT!! ENTER A NUMBER BETWEEN 1
6",'red')) 
         
                            continue 
     
                        else: 
                             
                            your_runs= your_runs+runs 
                     
                            vol.Speak("your guess") 
                         
                            print(colored("YOUR GUESS",'yellow')) 
                             
                            print(runs) 
                             
                            print('\n') 
                             
                            vol.Speak('computer guess') 
                             
                            print(colored("COMPUTER GUESS",'yellow')) 
                             
                            print(comp_bowl) 
                             
                            print('\n') 
                             
                            vol.Speak("Your runs Now are") 
                             
                            print(colored("YOUR RUNS NOW ARE :",'yellow')) 
         
                            print (your_runs) 
             
                            print('\n') 
 
                        no_of_chances_1= no_of_chances_1 + 1   
 
                    lst2= [1,2,3,4,5,6] 
 
                    chances_2= 18 
#75 
 
 
                    no_of_chances_2= 0 
 
                    comp_runs= 0 
                     
                    print(colored('*','blue')*150) 
                     
                    vol.Speak("COMPUTER BATTING") 
  
                    print(colored("COMPUTER BATTING".center(200),'cyan')) 
 
                    print(colored('*','blue')*150)     
     
                    print('\n') 
 
                    while no_of_chances_2 < chances_2: 
                 
                        vol.Speak("Enter Runs for Your Bowling Turn ") 
                     
                        print(colored("ENTER THE RUNS FOR YOUR BOWLING TURN : 
",'yellow')) 
 
                        bowl= int(input()) 
                         
                        print('\n') 
     
                        comp_bat= random.choice(lst2) 
 
                        if comp_bat==bowl: 
                 
                            vol.Speak("Computer Guess") 
                     
                            print(colored("COMPUTER GUESS : ",'yellow')) 
                         
                            print(comp_bat) 
                             
                            print('\n') 
                             
                            vol.Speak("your guess") 
                             
                            print(colored("YOUR GUESS : ",'yellow')) 
         
                            print (bowl) 
             
#76 
 
                            print('\n') 
                 
                            vol.Speak('the computer is out') 
                     
                            print(colored("THE COMPUTER IS OUT ",'red')) 
                         
                            print('\n') 
                             
                            vol.Speak('computer runs') 
                             
                            print(colored("COMPUTER RUNS : ",'yellow')) 
                             
                            print(comp_runs) 
         
                            print('\n') 
         
                            break 
     
                        else: 
         
                            comp_runs= comp_runs+comp_bat 
                                         
                            vol.Speak('computer guess') 
                             
                            print(colored("COMPUTER GUESS",'yellow')) 
                             
                            print(comp_bat) 
                             
                            print('\n') 
                             
                            vol.Speak("your guess") 
                         
                            print(colored("YOUR GUESS",'yellow')) 
                             
                            print(bowl) 
                             
                            print('\n') 
                             
                            vol.Speak("computer runs Now are") 
                             
                            print(colored("COMPUTER RUNS NOW ARE :",'yellow')) 
         
                            print (comp_runs) 
             
#77 
 
                            print('\n') 
 
 
                            if comp_runs > your_runs: 
             
                                break 
         
                        no_of_chances_2= no_of_chances_2+1 
             
                    vol.Speak('results') 
 
                    print(colored("*",'red')*100) 
     
                    print (colored("RESULTS ".center(200),'yellow')) 
 
                    print(colored("*",'red')*100)    
             
                    print('\n') 
         
                    if comp_runs < your_runs: 
                 
                        vol.Speak('your total runs') 
     
                        print(colored("YOUR TOTAL RUNS : ",'yellow')) 
     
                        print(your_runs) 
     
                        print('\n') 
         
                        vol.Speak('BOWLS TAKEN OUT OF 18') 
     
                        print(colored("BOWLS TAKEN (OUT OF 18) : ",'yellow')) 
     
                        print(no_of_chances_1+1) 
     
                        print('\n') 
         
                        vol.Speak("COMPUTER TOTAL RUNS ") 
     
                        print(colored("COMPUTER TOTAL RUNS :",'yellow')) 
     
                        print(comp_runs) 
     
                        print('\n') 
#78 
 
         
                        vol.Speak("BOWLS TAKEN OUT OF 18") 
     
                        print(colored("BOWLS TAKEN (OUT OF 18) : ",'yellow')) 
     
                        print(no_of_chances_2+1) 
         
                        voice.Speak('you won') 
     
                        print(colored('YOU WON','red')) 
         
                        print('\n') 
             
                        voice.Speak('check your dream coins') 
                 
                        print(colored('CHECK YOUR DREAM COINS','red')) 
                     
                        notification.notify(title = 'DREAM MART', 
                                                message = 'CHECK YOUR DREAM COINS ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 600) 
                 
     
                        print('\n') 
         
                        count+=200 
     
                    elif comp_runs == your_runs: 
     
                        vol.Speak("THE GAME TIED FOR A SUPEROVER") 
         
                        print(colored("THE GAME TIED FOR A SUPEROVER",'red')) 
             
                        lst1= [1,2,3,4,5,6] 
 
                        chances_1= 6 
 
                        no_of_chances_1= 0 
 
                        your_runs= 0 
                     
                        print(colored('*','blue')*150) 

 
                        vol.Speak("YOUR BATTING") 
  
                        print(colored("YOUR BATTING".center(200),'cyan')) 
 
                        print(colored('*','blue')*150)     
     
                        print('\n') 
 
                        while no_of_chances_1 < chances_1: 
                 
                            vol.Speak("Enter Runs for Your Batting Turn") 
                 
                            print(colored("ENTER RUNS FOR YOUR BATTING TURN  : 
",'yellow')) 
     
                            runs= int(input()) 
         
                            print('\n') 
     
                            comp_bowl= random.choice(lst1) 
 
                            if runs==comp_bowl: 
                 
                                vol.Speak('your guess') 
                 
                                print(colored("YOUR GUESS :",'yellow')) 
         
                                print (runs) 
             
                                print('\n') 
                 
                                vol.Speak('computer guess') 
                 
                                print(colored("COMPUTER GUESS :",'yellow')) 
                     
                                print(comp_bowl) 
                         
                                print('\n') 
                             
                                vol.Speak('you are out') 
                             
                                print(colored("YOU ARE OUT",'red')) 
                             
                                print('\n') 

 
                             
                                vol.Speak('your total runs') 
                             
                                print(colored("YOUR TOTAL RUNS",'red')) 
                             
                                print(your_runs) 
                             
                                print ("\n") 
         
                                break 
     
                            elif runs>6: 
             
                                vol.Speak('enter a number between 1 to 6') 
         
                                print(colored("ALERT!! ENTER A NUMBER BETWEEN 1
6",'red')) 
         
                                continue 
     
                            else: 
                             
                                your_runs= your_runs+runs 
                     
                                vol.Speak("your guess") 
                         
                                print(colored("YOUR GUESS",'yellow')) 
                             
                                print(runs) 
                             
                                print('\n') 
                             
                                vol.Speak('computer guess') 
                             
                                print(colored("COMPUTER GUESS",'yellow')) 
                             
                                print(comp_bowl) 
                             
                                print('\n') 
                             
                                vol.Speak("Your runs Now are") 
                             
                                print(colored("YOUR RUNS NOW ARE :",'yellow')) 
         
#81 
 
                                print (your_runs) 
             
                                print('\n') 
 
                            no_of_chances_1= no_of_chances_1 + 1   
 
                        lst2= [1,2,3,4,5,6] 
 
                        chances_2= 6 
 
                        no_of_chances_2= 0 
 
                        comp_runs= 0 
                     
                        print(colored('*','blue')*150) 
                     
                        vol.Speak("COMPUTER BATTING") 
  
                        print(colored("COMPUTER BATTING".center(200),'cyan')) 
 
                        print(colored('*','blue')*150)     
     
                        print('\n') 
 
                        while no_of_chances_2 < chances_2: 
                 
                            vol.Speak("Enter Runs for Your Bowling Turn ") 
                     
                            print(colored("ENTER THE RUNS FOR YOUR BOWLING TURN 
: ",'yellow')) 
 
                            bowl= int(input()) 
                         
                            print('\n') 
     
                            comp_bat= random.choice(lst2) 
 
                            if comp_bat==bowl: 
                 
                                vol.Speak("Computer Guess") 
                     
                                print(colored("COMPUTER GUESS : ",'yellow')) 
                         
                                print(comp_bat) 
#82 
 
                             
                                print('\n') 
                             
                                vol.Speak("your guess") 
                             
                                print(colored("YOUR GUESS : ",'yellow')) 
         
                                print (bowl) 
             
                                print('\n') 
                 
                                vol.Speak('the computer is out') 
                     
                                print(colored("THE COMPUTER IS OUT ",'red')) 
                         
                                print('\n') 
                             
                                vol.Speak('computer runs') 
                             
                                print(colored("COMPUTER RUNS : ",'yellow')) 
                             
                                print(comp_runs) 
         
                                print('\n') 
         
                                break 
     
                            else: 
         
                                comp_runs= comp_runs+comp_bat 
                                         
                                vol.Speak('computer guess') 
                             
                                print(colored("COMPUTER GUESS",'yellow')) 
                             
                                print(comp_bat) 
                             
                                print('\n') 
                             
                                vol.Speak("your guess") 
                         
                                print(colored("YOUR GUESS",'yellow')) 
                             
                                print(bowl) 
 print('\n') 
                             
                                vol.Speak("computer runs Now are") 
                             
                                print(colored("COMPUTER RUNS NOW ARE :",'yellow')) 
         
                                print (comp_runs) 
             
                                print('\n') 
 
 
                                if comp_runs > your_runs: 
             
                                    break 
         
                            no_of_chances_2= no_of_chances_2+1 
             
                        vol.Speak('results') 
 
                        print(colored("*",'red')*120) 
     
                        print (colored("RESULTS ".center(200),'yellow')) 
 
                        print(coolored("*",'red')*120)    
             
                        print('\n') 
         
                        if comp_runs < your_runs: 
                 
                            vol.Speak('your total runs') 
     
                            print(colored("YOUR TOTAL RUNS : ",'yellow')) 
     
                            print(your_runs) 
     
                            print('\n') 
         
                            vol.Speak('BOWLS TAKEN OUT OF 6') 
     
                            print(colored("BOWLS TAKEN (OUT OF 6) : ",'yellow')) 
     
                            print(no_of_chances_1+1) 
     
#84 
 
                            print('\n') 
         
                            vol.Speak("COMPUTER TOTAL RUNS ") 
     
                            print(colored("COMPUTER TOTAL RUNS :",'yellow')) 
     
                            print(comp_runs) 
     
                            print('\n') 
         
                            vol.Speak("BOWLS TAKEN OUT OF 6  ") 
     
                            print(colored("BOWLS TAKEN (OUT OF 6) : ",'yellow')) 
     
                            print(no_of_chances_2+1) 
     
                            print('\n') 
         
                            voice.Speak('you won') 
             
                            print(colored('YOU WON',red)) 
                 
                            print('\n') 
                     
                            voice.Speak('check your dream coins') 
                     
                            print(colored('CHECK YOUR DREAM COINS','red')) 
                         
                            print('\n') 
         
                            count+=200 
 
 
                    else: 
                     
                        vol.Speak('computer total runs') 
     
                        print(colored("COMPUTER TOTAL RUNS :",'yellow')) 
     
                        print(comp_runs) 
     
                        print('\n') 
         
                        vol.Speak('bowls taken out of 6') 
#85 
 
             
                        print(colored("BOWLS TAKEN (OUT OF 6) : ",'yellow')) 
     
                        print(no_of_chances_2+1) 
     
                        print('\n') 
         
                        vol.Speak('your total runs') 
     
                        print(colored("YOUR TOTAL RUNS :",'yellow')) 
     
                        print(your_runs) 
     
                        print('\n') 
         
                        vol.Speak('bowls taken out of 6') 
     
                        print(colored("BOWLS TAKEN (OUT OF 6) : ",'yellow')) 
     
                        print(no_of_chances_1+1) 
     
                        print('\n') 
         
                         
            else: 
                 
                break 
                 
                 
#SHOPPING 
                 
    if menu_choice==3: 
         
        animation = ["LOADING [■□□□□□□□□□]","LOADING [■■□□□□□□□□]", 
"LOADING [■■■□□□□□□□]",  
             "LOADING [■■■■□□□□□□]", "LOADING [■■■■■□□□□□]", "LOADING 
[■■■■■■□□□□]", 
             "LOADING [■■■■■■■□□□]", "LOADING [■■■■■■■■□□]", "LOADING 
[■■■■■■■■■□]",  
             "LOADING [■■■■■■■■■■]"] 
         
        for i in range(len(animation)): 
     
            time.sleep(1) 
#86 
 
     
            sys.stdout.write("\r" + animation[i % len(animation)]) 
     
            sys.stdout.flush() 
 
        sys.stdout.write('\rDone!                          ') 
         
        print('\n')         
         
        shop='y' 
         
        while shop=='y' or shop=='Y': 
             
            #SHOPPING CENTER 
             
            print(colored('MENU'.center(200),'red')) 
             
            print('\n') 
             
            voice.Speak('press 1 to view the cart') 
         
            print(colored('1. TO VIEW THE CART'.center(200),'yellow')) 
             
            voice.Speak('press 2 to shop') 
                 
            print(colored('2. TO SHOP'.center(200),'yellow')) 
     
            voice.Speak('press 3 to exit') 
         
            print(colored('3. TO EXIT'.center(200),'yellow')) 
             
            print('\n') 
             
            voice.Speak('enter your choice') 
                 
            print(colored('ENTER YOUR CHOICE  : ','yellow')) 
             
            shop_choice=int(input()) 
             
            print('\n') 
             
            #TO VIEW CART 
             
            if shop_choice==1: 
#87 
 
                 
                sc='y' 
                 
                while sc=='y' or sc=='Y': 
                     
                    pdf=pd.read_sql('select*from customers',connection) 
                 
                    
print(colored(pdf.to_string(index=False).center(160),'green',attrs=['bold','dark','concealed'])) 
                 
                    print('\n') 
                     
                    voice.Speak('press 1 to add more items to cart') 
                 
                    print(colored('1. TO ADD MORE ITEMS TO 
CART'.center(200),'yellow')) 
                     
                    voice.Speak('press 2 to delete items from cart') 
                 
                    print(colored('2. TO DELETE ITEMS FROM 
CART'.center(200),'yellow')) 
                     
                    voice.Speak('press  3 to place order') 
                 
                    print(colored('3. TO PLACE THE ORDER'.center(200),'yellow')) 
                     
                    print('\n') 
                     
                    voice.Speak('enter your choice') 
                 
                    print(colored('ENTER YOUR CHOICE : ','yellow')) 
                 
                    ca=int(input()) 
                     
                    print('\n') 
                 
                    if ca==1: 
                     
                        sc='n' 
                         
                    #DELETING ITEMS 
                 
                    elif ca==2: 
                     
#88 
 
                        o='y' 
                     
                        while o=='y' or o=='Y': 
                             
                            voice.Speak('enter the code of the item to be deleted') 
                             
                            print(colored("ENTER THE CODE OF THE ITEM TO BE 
DELETED",'red')) 
                         
                            item_code=input( ) 
                             
                            print('\n') 
                         
                            cart_df=pd.read_sql("select*from customers where p_code='%s' 
;"%(item_code),connection) 
                         
                            item_code=cart_df[['p_code']] 
                         
                            cols="`,`".join([str(i) for i in item_code.p_code.tolist()]) 
                         
                            sql=("delete from customers where p_code='%s';"%(cols)) 
                         
                            cursor.execute(sql) 
                                                         
                            connection.commit() 
                         
                            o="n" 
                             
                            voice.Speak('would you like to delete more items from your cart') 
                             
                            print(colored("WOULD YOU LIKE TO DELETE MORE ITEMS 
FROM YOUR CART ? (Y/N) ",'yellow')) 
                         
                            o=input() 
                             
                            print('\n') 
                         
                    elif ca==3:                  
                         
                        fn='y' 
                         
                        while fn=='y' or fn=='Y': 
                             
                            #VIEWING THE FINAL CART 
#89 
 
                             
                            if ca==3: 
                                 
                                voice.Speak('here is your final cart') 
                                 
                                print(colored("HERE IS YOUR FINAL CART :",'red')) 
                                 
                                print('\n') 
                                 
                                cart_df=pd.read_sql("select*from customers;",connection) 
                                 
                                
print(colored(cart_df.to_string(index=False),'red',attrs=['bold','dark','concealed'])) 
                                 
                                print('\n') 
                                 
                                voice.Speak("would you like to view your bill") 
                                 
                                print(colored("WOULD YOU LIKE TO VIEW YOUR BILL 
?",'red')) 
                                 
                                bl=input() 
                                 
                                print('\n') 
                                 
                                #BILLING       
                                 
                                if bl=='y' or bl=='Y': 
                                     
                                    total=cart_df[['total_price']] 
                                     
                                    print('\n') 
                                     
                                    amount=total.sum() 
                                     
                                    voice.Speak('do you have a coupon') 
                                     
                                    print(colored('DO YOU HAVE A COUPON (Y/N)','green')) 
                                     
                                    c=input() 
                                     
                                    print('\n') 
                                     
                                    #DISCOUNTING 
#90 
 
                                     
                                    if c=='y' or c== 'Y': 
                                         
                                        voice.Speak('enter your coupon code') 
                                         
                                        print(colored("ENTER YOUR COUPON CODE",'red')) 
                                         
                                        co=input() 
                                         
                                        print('\n') 
                                         
                                        if co=='dc10' or co== 'DC10': 
                                             
                                            amount1=amount-(amount*10)/100   
                                             
                                            voice.Speak('YOU GOT 10 PERCENT OFF') 
                                             
                                            print(colored('YOU GOT 10% OFF','red')) 
                                             
                                            notification.notify(title = 'DREAM MART', 
                                                message = 'YOU GOT 10% OFF ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 600) 
                                                             
                                            print('\n') 
                                             
                                            
print(colored(cart_df.to_string(index=False),'green',attrs=['bold','dark','concealed'])) 
                                             
                                            print('\n') 
                                             
                                            voice.Speak('TOTAL AMOUNT TO BE PAID IS') 
                                             
                                            print(colored("TOTAL AMOUNT TO BE PAID IS : 
",'red'),amount1) 
                                             
                                            print('\n') 
                                             
                                            voice.Speak('ARE YOU SURE AND PROCEED YOUR 
ORDER') 
                                             
                                            print(colored('ARE YOU SURE AND PROCEED YOUR 
ORDER','yellow')) 
#91 
 
 
                                            ff=input() 
                                             
                                            print('\n') 
                                             
                                            if ff != 'y' or ff !='Y': 
                                                 
                                                sc='y' 
                                             
                                        elif co=='dc15' or co== 'DC15': 
                                             
                                            amount1=amount-(amount*15)/100   
                                             
                                            voice.Speak('YOU GOT 15 PERCENT OFF') 
                                             
                                            print(colored('YOU GOT 15% OFF','red')) 
                                             
                                            notification.notify(title = 'DREAM MART', 
                                                message = 'YOU GOT 15% OFF ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 600) 
                                                          
                                            print('\n') 
                                             
                                            
print(colored(cart_df.to_string(index=False),'green',attrs=['bold','dark','concealed'])) 
                                             
                                            print('\n') 
                                             
                                            voice.Speak('TOTAL AMOUNT TO BE PAID IS') 
                                             
                                            print(colored("TOTAL AMOUNT TO BE PAID IS 
:",'red'),amount1) 
                                             
                                            print('\n') 
                                             
                                            voice.Speak('ARE YOU SURE AND PROCEED YOUR 
ORDER') 
                                             
                                            print(colored('ARE YOU SURE AND PROCEED YOUR 
ORDER','yellow')) 
 
                                            ff=input() 
#92 
 
                                             
                                            print('\n') 
                                             
                                            if ff != 'y' or ff !='Y': 
                                                 
                                                sc='y' 
                                                                                        
                                        elif co=='dc25' or co== 'DC25': 
                                             
                                            amount1=amount-(amount*25)/100   
                                             
                                            voice.Speak('YOU GOT 25 PERCENT OFF') 
                                             
                                            print(colored('YOU GOT 25% OFF','red')) 
 
                                            notification.notify(title = 'DREAM MART', 
                                                message = 'YOU GOT 25% OFF ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 600)                                             
                                             
                                            print('\n') 
                                             
                                            
print(colored(cart_df.to_string(index=False),'green',attrs=['bold','dark','concealed'])) 
                                             
                                            print('\n') 
                                             
                                            voice.Speak('TOTAL AMOUNT TO BE PAID IS') 
                                             
                                            print(colored("TOTAL AMOUNT TO BE PAID IS : 
",'red') , amount1) 
                                             
                                            print('\n') 
                                             
                                            voice.Speak('ARE YOU SURE AND PROCEED YOUR 
ORDER') 
                                             
                                            print(colored('ARE YOU SURE AND PROCEED YOUR 
ORDER','yellow')) 
 
                                            ff=input() 
                                             
                                            print('\n') 
#93 
 
                                             
                                            if ff != 'y' or ff !='Y': 
                                                 
                                                sc='y' 
                                             
                                        else: 
                                             
                                            voice.Speak("INVALID COUPON") 
                                             
                                            print(colored("INVALID COUPON",'red')) 
                                             
                                            print('\n') 
                                             
                                            voice.Speak('WOULD YOU LIKE TO TRY AGAIN') 
                                             
                                            print(colored("WOULD YOU LIKE TO TRY AGAIN 
(Y/N) ",'yellow')) 
                                             
                                            coup=input() 
                                             
                                            print('\n') 
                                             
                                            if coup =='y' or coup=='Y': 
                                                 
                                                fn='y' 
                                                 
                                            else: 
                                                 
                                                sc='y' 
                                                 
                                                 
                                else: 
                                     
                                    sc='y' 
                                     
                                ad='y' 
                                     
                                while ad=='y' or ad=='Y': 
                     
                     
                                    #GETTING ADDRESS 
                         
                                    voice.Speak('ENTER YOUR DOOR OR FLAT NUMBER') 
                                     
#94 
 
                                    print(colored('ENTER YOUR DOOR/FLAT NO.','yellow')) 
                                 
                                    a1=input() 
                                     
                                    print('\n') 
                                     
                                    voice.Speak('ENTER YOUR FLAT NAME AND STREET 
NAME') 
                                 
                                    print(colored('ENTER YOUR FLAT NAME & STREET 
NAME','yellow')) 
                                 
                                    a2=input() 
                                     
                                    print('\n') 
                                     
                                    voice.Speak('ENTER YOUR AREA') 
                                 
                                    print(colored('ENTER YOUR AREA','yellow')) 
                                 
                                    a3=input() 
                                     
                                    print('\n') 
                                     
                                    voice.Speak('ENTER YOUR PINCODE') 
                                 
                                    print(colored('ENTER YOUR PINCODE','yellow')) 
                                 
                                    a4=input() 
                                     
                                    print('\n') 
                                                                         
                                    voice.Speak('YOUR ADDRESS') 
                                 
                                    print(colored('YOUR ADDRESS :','red')) 
                                 
                                    print(a1, ',' , a2 ,',' ) 
                                     
                                    print(a3,',') 
                                     
                                    print('PINCODE : ', a4 , '.') 
                                     
                                    print('\n') 
                                     
#95 
 
                                    voice.Speak('DO YOU WANT TO CHANGE YOUR 
ADDRESS') 
                                 
                                    print(colored('DO YOU WANT TO CHANGE YOUR 
ADDRESS','red')) 
                                 
                                    a5=input() 
                                     
                                    print('\n') 
                                 
                                    if a5=='y' or a5=='Y': 
                                         
                                        ad='y' 
                                         
                                    else: 
                                         
                                        break 
                                         
                                 
                                notification.notify(title = 'DREAM MART', 
                                                message = 'YOUR ORDER HAS BEEN 
SUCCESSFULLY PLACED ��', 
                                                app_icon 
=r"C:\Users\Junaidh\Downloads\Dream_icon.svg (2).ico",  
                                                timeout = 600) 
                                 
                                voice.Speak('YOUR ORDER HAS BEEN SUCCESSFULLY 
PLACED') 
                                 
                                print(colored('YOUR ORDER HAS BEEN SUCCESSFULLY 
PLACED ','red')) 
                                 
                                print('\n') 
                                                 
                                voice.Speak('THANK YOU FOR PLACING YOUR ORDER')     
                             
                                print(colored('THANK YOU FOR PLACING YOUR 
ORDER','red')) 
                                 
                                print('\n') 
                     
                                sql=("delete from customers ;") 
                     
                                cursor.execute(sql) 
#96 
 
                     
                                connection.commit() 
                         
                                voice.Speak('WE WILL DELIVER YOUR ORDER 
INSTANTLY') 
                     
                                print(colored('WE WILL DELIVER YOUR ORDER 
INSTANTLY','red')) 
                         
                                print('\n') 
                             
                             
                                #RATING 
                                 
                                voice.Speak('DROP YOUR RATING') 
                     
                                print(colored('DROP YOUR RATING','yellow')) 
                         
                                print('\n') 
                             
                                voice.Speak('HOW MUCH STAR WOULD YOU GIVE us') 
                             
                                print(colored('HOW MUCH STAR WOULD YOU GIVE 
US','yellow')) 
                     
                                star=int(input()) 
                         
                                print('\n') 
                             
                                st='y' 
                                 
                                while st=='y': 
                     
                                    if star==1: 
                             
                                        animation = ['����� ',"⭐���� "] 
                                                      
                                        for i in range(len(animation)): 
     
                                            time.sleep(1) 
     
                                            sys.stdout.write("\r" + animation[i % len(animation)]) 
                                        
                                            sys.stdout.flush() 
#97 
 
                 
                                        sys.stdout.write('\r⭐����             ')    
             
                                        print('\n') 
                         
                                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\1.jpg',width="200", height="200")) 
                             
                                        print('\n') 
                                 
                                        voice.Speak('THANK YOU FOR YOUR RATING') 
                                 
                                        print(colored('THANK YOU FOR YOUR RATING','cyan')) 
                                     
                                        print('\n') 
                                         
                                        st='n' 
                         
                                    elif star==2: 
                                 
                                        animation = ['����� ',"⭐���� ","⭐⭐��� "] 
                                                      
                                        for i in range(len(animation)): 
     
                                            time.sleep(1) 
     
                                            sys.stdout.write("\r" + animation[i % len(animation)]) 
                                        
                                            sys.stdout.flush() 
                 
                                        sys.stdout.write('\r⭐⭐���             ')    
                                 
                                        print('\n') 
                         
                                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\2.png',width="200", height="200")) 
                             
                                        print('\n') 
                                 
                                        voice.Speak('THANK YOU FOR YOUR RATING') 
                                 
                                        print(colored('THANK YOU FOR YOUR RATING','cyan')) 
                                     
                                        print('\n') 
#98 
 
                                         
                                        st='n' 
                         
                                    elif star==3: 
                                 
                                        animation = ['����� ',"⭐���� ","⭐⭐��� 
","⭐⭐⭐�� "] 
                                                      
                                        for i in range(len(animation)): 
     
                                            time.sleep(1) 
     
                                            sys.stdout.write("\r" + animation[i % len(animation)]) 
                                        
                                            sys.stdout.flush() 
                                                       
                                        sys.stdout.write('\r⭐⭐⭐��             ')                     
   
                                        print('\n') 
                         
                                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\3.png',width="200", height="200")) 
                             
                                        print('\n') 
                                 
                                        voice.Speak('THANK YOU FOR YOUR RATING') 
                                 
                                        print(colored('THANK YOU FOR YOUR RATING','cyan')) 
                                     
                                        print('\n') 
                                         
                                        st='n' 
                         
                                    elif star==4: 
                                 
                                        animation = ['�����  ',"⭐����  ","⭐⭐���  
","⭐⭐⭐��   ","⭐⭐⭐⭐�  "] 
                                                      
                                        for i in range(len(animation)): 
     
                                            time.sleep(1) 
     
                                            sys.stdout.write("\r" + animation[i % len(animation)]) 
                                        
#99 
 
                                            sys.stdout.flush() 
 
                                        sys.stdout.write('\r⭐⭐⭐⭐�             ')     
     
                                        print('\n') 
                         
                                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\4.jpg',width="200", height="200")) 
                             
                                        print('\n') 
                                 
                                        voice.Speak('THANK YOU FOR YOUR RATING') 
                                 
                                        print(colored('THANK YOU FOR YOUR RATING','cyan')) 
                                     
                                        print('\n') 
                                         
                                        st='n' 
                         
                                    elif star==5: 
                                 
                                        animation = ['����� ',"⭐���� ","⭐⭐��� 
","⭐⭐⭐�� ","⭐⭐⭐⭐� " 
                                                     ,"⭐⭐⭐⭐⭐ "] 
                                                      
                                        for i in range(len(animation)): 
     
                                            time.sleep(1) 
     
                                            sys.stdout.write("\r" + animation[i % len(animation)]) 
                                        
                                            sys.stdout.flush() 
                 
                                        sys.stdout.write('\r⭐⭐⭐⭐⭐             ')     
 
                                        print('\n') 
                         
                                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\5.jpg',width="200", height="200")) 
                             
                                        print('\n') 
                                 
                                        voice.Speak('THANK YOU FOR YOUR RATING') 
                                 
#100 
 
                                        print(colored('THANK YOU FOR YOUR RATING','cyan')) 
                                     
                                        print('\n') 
                                         
                                        st='n' 
                         
                                    else: 
                                 
                                        voice.Speak('ENTER A NUMBER BETWEEN 1 to 5') 
                         
                                        print(colored('ENTER A NUMBER BETWEEN 1-5','red')) 
                             
                                        print('\n') 
                             
                                        st='y' 
                                 
                                 
                                #FEEDBACK 
                                 
                                voice.Speak('DROP YOUR FEEDBACK HERE') 
                     
                                print(colored('DROP YOUR FEEDBACK HERE','yellow')) 
                     
                                feed=input() 
                         
                                print('\n') 
                             
                                voice.Speak('THANKS FOR YOUR REVIEW') 
                     
                                print(colored('THANKS FOR YOUR REVIEW','red')) 
                         
                                print('\n') 
                             
                                voice.Speak('DO YOU WANT TO CHECK THE STATUS OF 
YOUR PRODUCT') 
                         
                                print(colored('DO YOU WANT TO CHECK THE STATUS OF 
YOUR PRODUCT (Y/N) ','red')) 
                             
                                qw=input() 
                                 
                                print('\n') 
                                 
                                 
#101 
 
                                #DELIVERY DETAILS 
                                 
                                if qw =='y' or qw=='Y': 
                                     
                                    dt = datetime.now() + timedelta(hours=5) 
                                     
                                    dt1=format(dt, '%H:%M:%S') 
                                     
                                    voice.Speak("YOUR ORDER WILL BE DELIVERED BY ") 
                                     
                                    print(colored("YOUR ORDER WILL BE DELIVERED BY 
",'red'),dt1) 
                                     
                                    print('\n') 
                                     
                                    voice.Speak("FOR ANY QUERIES CONTACT US ON + 9 1 
9 1 2 3 4 5 6 7 8 0 ") 
                                     
                                    print(colored("FOR ANY QUERIES CONTACT US ON +91 
91234 56780 ",'yellow')) 
                                     
                                    print('\n') 
                                     
                                    fn='n'   
                                     
                                    sc='n' 
                                     
                                     
                                else: 
                                     
                                    voice.Speak("FOR ANY QUERIES CONTACT US ON + 9 1 
9 1 2 3 4 5 6 7 8 0 ") 
                                     
                                    print(colored("FOR ANY QUERIES CONTACT US ON +91 
91234 56780 ",'yellow')) 
                                     
                                    print('\n')                                     
                                     
                                    fn='n' 
                                     
                                     
            #DISPLAYING ITEMS FOR PURCHASE                                            
                 
            elif shop_choice==2: 
#102 
 
                 
                shopping='y' 
                 
                while shopping=='y' or shopping=='Y': 
                     
                    voice.Speak('press 1 for foodgrains oils and masalas') 
                     
                    print(colored('1. FOODGRAINS,OILS & 
MASALAS'.center(200),'yellow')) 
                     
                    voice.Speak('press 2 for fruits and vegetables') 
                     
                    print(colored('2. FRUITS & VEGETABLES'.center(200),'yellow')) 
                     
                    voice.Speak('press 3 for snacks station') 
                     
                    print(colored('3. SNACKS STATION'.center(200),'yellow')) 
                     
                    voice.Speak('press 4 for diary and bakery') 
                     
                    print(colored('4. DIARY & BAKERY'.center(200),'yellow')) 
                     
                    voice.Speak('press 5 for beverage corner') 
                     
                    print(colored('5. BEVERAGE CORNER'.center(200),'yellow')) 
                     
                    voice.Speak('press 6 for instant food ') 
                     
                    print(colored('6. INSTANT FOODS'.center(200),'yellow')) 
                     
                    voice.Speak('press 7 for beauty and personal care products') 
                     
                    print(colored('7. BEAUTY & PERSONAL CARE'.center(200),'yellow')) 
                     
                    voice.Speak('press 8 for home hygiene and care') 
                     
                    print(colored('8. HOME HYGIENE & CARE'.center(200),'yellow')) 
                     
                    voice.Speak('press 9 for mom and baby products') 
                     
                    print(colored('9. MOM & BABY'.center(200),'yellow')) 
                     
                    voice.Speak('enter your choice') 
                     
#103 
 
                    print('\n') 
                     
                    print(colored('ENTER YOUR CHOICE  : ','yellow')) 
                     
                    sh=int(input()) 
                     
                    print('\n') 
                     
                    #DISPLAYING FOODGRAINS,OILS AND MASALA ITEMS  
                     
                    if sh==1: 
                         
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\food1.png',width="950", height="400")) 
                         
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\food2.png',width="950", height="400")) 
                         
                        print('\n') 
                             
                        pfdf=pd.read_sql('select*from product',connection) 
                         
                        
print(colored(pfdf.to_string(index=False).center(160),'green',attrs=['bold','dark','concealed'])) 
                         
                        print('\n') 
                         
                        voice.Speak('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ') 
                             
                        print(colored('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ','red')) 
                             
                        shop1=input() 
                         
                        print('\n') 
                             
                        if shop1=='y' or shop1=='Y' : 
                                 
                            total=pd.DataFrame=({'price':0}) 
                                 
                            cart1='y' 
                                 
                            while cart1=='y' or cart1=='Y': 
#104 
 
                                 
                                voice.Speak('enter the product code') 
                                     
                                print(colored("ENTER THE PRODUCT CODE",'yellow')) 
                                     
                                pf=input( ) 
                                     
                                print('\n') 
                                 
                                voice.Speak('enter the quantity') 
                                 
                                print(colored("ENTER THE QUANTITY",'yellow')) 
                                 
                                pfq=int(input( )) 
                                 
                                print('\n') 
                                     
                                pf_df=pd.read_sql("select*from product where pf_code='%s' 
;"%(pf),connection) 
             
                                pf_code=pf_df[['pf_code']]  
                                     
                                pf_name=pf_df[['pf_name']] 
                                     
                                pfq_series=pd.Series([pfq]) 
                                     
                                pf_price=pf_df[['price']] 
                                     
                                pf_total=pf_price.mul(pfq) 
                                     
                                col="`,`".join([str(i) for i in pf_code.pf_code.tolist()]) 
                                     
                                col1="`,`".join([str(i) for i in pf_name.pf_name.tolist()]) 
                                     
                                col2="`,`".join([str(i) for i in pfq_series.tolist()]) 
                                     
                                col3="`,`".join([str(i) for i in pf_price.price.tolist()]) 
                                     
                                col4="`,`".join([str(i) for i in pf_total.price.tolist()]) 
                                     
                                for i,row in pf_code.iterrows(): 
                                         
                                    for i,row in pf_name.iterrows(): 
                                             
#105 
 
                                        for i,row in pf_price.iterrows(): 
                                                 
                                            for i,row in pf_total.iterrows(): 
                                                     
                                                sql2="INSERT INTO `customers` 
(`p_code`,`p_name`,`price`,`quantity`,`total_price`)  VALUES (%s, %s, %s, %s, %s)" 
                                                     
                                                cursor.execute(sql2,(col, col1,col2,col3,col4) ) 
                                                     
                                                connection.commit() 
                                                     
                                connection.commit() 
                                 
                                voice.Speak("WOULD YOU LIKE TO ADD MORE 
FOODGRAIN,OIL & MASALA ITEMS TO YOUR CART ") 
                                     
                                print(colored("WOULD YOU LIKE TO ADD MORE 
FOODGRAIN,OIL & MASALA ITEMS TO YOUR CART ?? (Y/N) ",'yellow')) 
                                     
                                cart1=input() 
                                 
                                print('\n') 
 
                        else: 
                             
                            break 
                             
                    #DISPLAYING VEGETABLES AND FRUITS        
                                     
                    elif sh==2: 
                         
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\vegge.png',width="950", height="400")) 
                         
                        print('\n') 
                             
                        pvdf=pd.read_sql('select*from product2',connection) 
                         
                        
print(colored(pvdf.to_string(index=False).center(160),'green',attrs=['bold','dark','concealed'])) 
                         
                        print('\n') 
                         
#106 
 
                        voice.Speak('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ') 
                             
                        print(colored('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ','red')) 
                             
                        shop1=input() 
                         
                        print('\n') 
                             
                        if shop1=='y' or shop1=='Y' : 
                                 
                            total=pd.DataFrame=({'price':0}) 
                                 
                            cart1='y' 
                                 
                            while cart1=='y' or cart1=='Y': 
                                 
                                voice.Speak("ENTER THE PRODUCT CODE") 
                                     
                                print(colored("ENTER THE PRODUCT CODE",'yellow')) 
                                     
                                pv=input( ) 
                                     
                                print('\n') 
                                 
                                voice.Speak("ENTER THE QUANTITY") 
                                 
                                print(colored("ENTER THE QUANTITY",'yellow')) 
                                     
                                pvq=int(input( )) 
                                 
                                print('\n') 
                                     
                                pv_df=pd.read_sql("select*from product2 where pv_code='%s' 
;"%(pv),connection) 
             
                                pv_code=pv_df[['pv_code']]  
                                     
                                pv_name=pv_df[['pv_name']] 
                                     
                                pvq_series=pd.Series([pvq]) 
                                 
                                pv_price=pv_df[['price']] 
#107 
 
                                     
                                pv_total=pv_price.mul(pvq) 
                                     
                                col="`,`".join([str(i) for i in pv_code.pv_code.tolist()]) 
                                     
                                col1="`,`".join([str(i) for i in pv_name.pv_name.tolist()]) 
                                     
                                col2="`,`".join([str(i) for i in pvq_series.tolist()]) 
                                     
                                col3="`,`".join([str(i) for i in pv_price.price.tolist()]) 
                                     
                                col4="`,`".join([str(i) for i in pv_total.price.tolist()]) 
                                     
                                for i,row in pv_code.iterrows(): 
                                         
                                    for i,row in pv_name.iterrows(): 
                                             
                                        for i,row in pv_price.iterrows(): 
                                                 
                                            for i,row in pv_total.iterrows(): 
                                                     
                                                sql2="INSERT INTO `customers` 
(`p_code`,`p_name`,`price`,`quantity`,`total_price`)  VALUES (%s, %s, %s, %s, %s)" 
                                                     
                                                cursor.execute(sql2,(col, col1,col2,col3,col4) ) 
                                                     
                                                connection.commit() 
                                                     
                                connection.commit() 
                                 
                                voice.Speak("WOULD YOU LIKE TO ADD MORE FRUITS & 
VEGETABLES TO YOUR CART ") 
                                     
                                print(colored("WOULD YOU LIKE TO ADD MORE FRUITS & 
VEGETABLES TO YOUR CART ?? (Y/N) ",'yellow')) 
                                     
                                cart1=input() 
                                 
                                print('\n') 
 
                        else: 
                             
                            break 
                             
#108 
 
                    #DISPLAYING SNACKS ITEMS 
                                 
                    elif sh==3: 
                         
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\snacks.png',width="950", height="400")) 
                         
                        print('\n') 
                             
                        psdf=pd.read_sql('select*from product3',connection) 
                         
                        
print(colored(psdf.to_string(index=False).center(160),'green',attrs=['bold','dark','concealed'])) 
                         
                        print('\n') 
                         
                        voice.Speak('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ') 
                             
                        print(colored('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ','red')) 
                             
                        shop1=input() 
                         
                        print('\n') 
                             
                        if shop1=='y' or shop1=='Y' : 
                                 
                            total=pd.DataFrame=({'price':0}) 
                                 
                            cart1='y' 
                                 
                            while cart1=='y' or cart1=='Y': 
                                 
                                voice.Speak('enter the product code') 
                                     
                                print(colored("ENTER THE PRODUCT CODE",'yellow')) 
                                     
                                ps=input( ) 
                                     
                                print('\n') 
                                 
                                voice.Speak('enter the quantity') 
                                 
#109 
 
                                print(colored("ENTER THE QUANTITY",'yellow')) 
                                     
                                psq=int(input( )) 
                                 
                                print('\n') 
                                     
                                ps_df=pd.read_sql("select*from product3 where ps_code='%s' 
;"%(ps),connection) 
             
                                ps_code=ps_df[['ps_code']]  
                                     
                                ps_name=ps_df[['ps_name']] 
                                     
                                psq_series=pd.Series([psq]) 
                                     
                                ps_price=ps_df[['price']] 
                                     
                                ps_total=ps_price.mul(psq) 
                                     
                                col="`,`".join([str(i) for i in ps_code.ps_code.tolist()]) 
                                     
                                col1="`,`".join([str(i) for i in ps_name.ps_name.tolist()]) 
                                     
                                col2="`,`".join([str(i) for i in psq_series.tolist()]) 
                                     
                                col3="`,`".join([str(i) for i in ps_price.price.tolist()]) 
                                     
                                col4="`,`".join([str(i) for i in ps_total.price.tolist()]) 
                                     
                                for i,row in ps_code.iterrows(): 
                                         
                                    for i,row in ps_name.iterrows(): 
                                             
                                        for i,row in ps_price.iterrows(): 
                                                 
                                            for i,row in ps_total.iterrows(): 
                                                     
                                                sql2="INSERT INTO `customers` 
(`p_code`,`p_name`,`price`,`quantity`,`total_price`)  VALUES (%s, %s, %s, %s, %s)" 
                                                     
                                                cursor.execute(sql2,(col, col1,col2,col3,col4) ) 
                                                     
                                                connection.commit() 
                                                     
#110 
 
                                connection.commit() 
                                 
                                voice.Speak('WOULD YOU LIKE TO ADD MORE SNACKS 
ITEMS TO YOUR CART') 
                                     
                                print(colored("WOULD YOU LIKE TO ADD MORE SNACKS 
ITEMS TO YOUR CART ?? (Y/N) ",'yellow')) 
                                     
                                cart1=input() 
                                 
                                print('\n') 
 
                        else: 
                             
                            break 
                             
                    #DISPLAYING DIARY AND BAKERY ITEMS 
                                 
                    elif sh==4: 
 
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\dairy.png',width="950", height="400")) 
                         
                        print('\n') 
                             
                        pdadf=pd.read_sql('select*from product4',connection) 
                         
                        
print(colored(pdadf.to_string(index=False).center(160),'green',attrs=['bold','dark','concealed'])
 ) 
                         
                        print('\n') 
                         
                        voice.Speak('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ') 
                             
                        print(colored('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ','red')) 
                             
                        shop1=input() 
                         
                        print('\n') 
                             
                        if shop1=='y' or shop1=='Y' : 
#111 
 
                                 
                            total=pd.DataFrame=({'price':0}) 
                                 
                            cart1='y' 
                                 
                            while cart1=='y' or cart1=='Y': 
                                 
                                voice.Speak('enter the product code') 
                                     
                                print(colored("ENTER THE PRODUCT CODE",'yellow')) 
                                     
                                pda=input( ) 
                                     
                                print('\n') 
                                 
                                voice.Speak('enter the quantity') 
                                 
                                print(colored("ENTER THE QUANTITY",'yellow')) 
                                     
                                pdaq=int(input( )) 
                                 
                                print('\n') 
                                     
                                pda_df=pd.read_sql("select*from product4 where pda_code='%s' 
;"%(pda),connection) 
             
                                pda_code=pda_df[['pda_code']] 
                                     
                                pda_name=pda_df[['pda_name']] 
                                     
                                pdaq_series=pd.Series([pdaq]) 
                                     
                                pda_price=pda_df[['price']] 
                                     
                                pda_total=pda_price.mul(pdaq) 
                                     
                                col="`,`".join([str(i) for i in pda_code.pda_code.tolist()]) 
                                     
                                col1="`,`".join([str(i) for i in pda_name.pda_name.tolist()]) 
                                     
                                col2="`,`".join([str(i) for i in pdaq_series.tolist()]) 
                                     
                                col3="`,`".join([str(i) for i in pda_price.price.tolist()]) 
                                     
#112 
 
                                col4="`,`".join([str(i) for i in pda_total.price.tolist()]) 
                                     
                                for i,row in pda_code.iterrows(): 
                                         
                                    for i,row in pda_name.iterrows(): 
                                             
                                        for i,row in pda_price.iterrows(): 
                                                 
                                            for i,row in pda_total.iterrows(): 
                                                     
                                                sql2="INSERT INTO `customers` 
(`p_code`,`p_name`,`price`,`quantity`,`total_price`)  VALUES (%s, %s, %s, %s, %s)" 
                                                     
                                                cursor.execute(sql2,(col, col1,col2,col3,col4) ) 
                                                     
                                                connection.commit() 
                                                     
                                connection.commit() 
                                 
                                voice.Speak('WOULD YOU LIKE TO ADD MORE DIARY & 
BAKERY ITEMS TO YOUR CART') 
                                     
                                print(colored("WOULD YOU LIKE TO ADD MORE DIARY & 
BAKERY ITEMS TO YOUR CART ?? (Y/N) ",'yellow')) 
                                     
                                cart1=input() 
                                 
                                print('\n') 
                                 
                    #DISPLAYING BEVERAGE ITEMS 
                     
                    elif sh==5: 
                         
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\beverage.png',width="950", height="400")) 
                         
                        print('\n') 
                             
                        pbdf=pd.read_sql('select*from product5',connection) 
                         
                        
print(colored(pbdf.to_string(index=False).center(160),'green',attrs=['bold','dark','concealed'])) 
                         
                        print('\n') 
#113 
 
                         
                        voice.Speak('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ') 
                             
                        print(colored('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ','red')) 
                             
                        shop1=input() 
                         
                        print('\n') 
                             
                        if shop1=='y' or shop1=='Y' : 
                                 
                            total=pd.DataFrame=({'price':0}) 
                                 
                            cart1='y' 
                                 
                            while cart1=='y' or cart1=='Y': 
                                 
                                voice.Speak('enter the product code') 
                                     
                                print(colored("ENTER THE PRODUCT CODE",'yellow')) 
                                     
                                pb=input( ) 
                                     
                                print('\n') 
                                 
                                voice.Speak('enter the quantity') 
                                 
                                print(colored("ENTER THE QUANTITY",'yellow')) 
                                     
                                pbq=int(input( )) 
                                 
                                print('\n') 
                                     
                                pb_df=pd.read_sql("select*from product5 where pb_code='%s' 
;"%(pb),connection) 
             
                                pb_code=pb_df[['pb_code']]  
                                     
                                pb_name=pb_df[['pb_name']] 
                                     
                                pbq_series=pd.Series([pbq]) 
                                     
#114 
 
                                pb_price=pb_df[['price']] 
                                     
                                pb_total=pb_price.mul(pbq) 
                                     
                                col="`,`".join([str(i) for i in pb_code.pb_code.tolist()]) 
                                     
                                col1="`,`".join([str(i) for i in pb_name.pb_name.tolist()]) 
                                     
                                col2="`,`".join([str(i) for i in pbq_series.tolist()]) 
                                     
                                col3="`,`".join([str(i) for i in pb_price.price.tolist()]) 
                                     
                                col4="`,`".join([str(i) for i in pb_total.price.tolist()]) 
                                     
                                for i,row in pb_code.iterrows(): 
                                         
                                    for i,row in pb_name.iterrows(): 
                                             
                                        for i,row in pb_price.iterrows(): 
                                                 
                                            for i,row in pb_total.iterrows(): 
                                                     
                                                sql2="INSERT INTO `customers` 
(`p_code`,`p_name`,`price`,`quantity`,`total_price`)  VALUES (%s, %s, %s, %s, %s)" 
                                                     
                                                cursor.execute(sql2,(col, col1,col2,col3,col4) ) 
                                                     
                                                connection.commit() 
                                                     
                                connection.commit() 
                                 
                                voice.Speak('WOULD YOU LIKE TO ADD MORE 
BEVERAGE ITEMS TO YOUR CART') 
                                     
                                print(colored("WOULD YOU LIKE TO ADD MORE 
BEVERAGE ITEMS TO YOUR CART ?? (Y/N) ",'yellow')) 
                                     
                                cart1=input() 
                                 
                                print('\n') 
                                 
                    #DISPLAYING INSTANT FOOD ITEMS 
                     
                    elif sh==6: 
#115 
 
                             
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\instant.png',width="950", height="400")) 
                         
                        print('\n') 
                             
                        pidf=pd.read_sql('select*from product6',connection) 
                         
                        
print(colored(pidf.to_string(index=False).center(160),'green',attrs=['bold','dark','concealed'])) 
                         
                        print('\n') 
                         
                        voice.Speak('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART') 
                             
                        print(colored('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ','red')) 
                             
                        shop1=input() 
                         
                        print('\n') 
                             
                        if shop1=='y' or shop1=='Y' : 
                                 
                            total=pd.DataFrame=({'price':0}) 
                                 
                            cart1='y' 
                                 
                            while cart1=='y' or cart1=='Y': 
                                 
                                voice.Speak('enter the product code') 
                                     
                                print(colored("ENTER THE PRODUCT CODE",'yellow')) 
                                     
                                pi=input( ) 
                                     
                                print('\n') 
                                 
                                voice.Speak('enter the quantity') 
                                 
                                print(colored("ENTER THE QUANTITY",'yellow')) 
                                     
                                piq=int(input( )) 
#116 
 
                                 
                                print('\n') 
                                     
                                pi_df=pd.read_sql("select*from product6 where pi_code='%s' 
;"%(pi),connection) 
             
                                pi_code=pi_df[['pi_code']] 
                                     
                                pi_name=pi_df[['pi_name']] 
                                     
                                piq_series=pd.Series([piq]) 
                                     
                                pi_price=pi_df[['price']] 
                                     
                                pi_total=pi_price.mul(piq) 
                                     
                                col="`,`".join([str(i) for i in pi_code.pi_code.tolist()]) 
                                     
                                col1="`,`".join([str(i) for i in pi_name.pi_name.tolist()]) 
                                     
                                col2="`,`".join([str(i) for i in piq_series.tolist()]) 
                                     
                                col3="`,`".join([str(i) for i in pi_price.price.tolist()]) 
                                     
                                col4="`,`".join([str(i) for i in pi_total.price.tolist()]) 
                                     
                                for i,row in pi_code.iterrows(): 
                                         
                                    for i,row in pi_name.iterrows(): 
                                             
                                        for i,row in pi_price.iterrows(): 
                                                 
                                            for i,row in pi_total.iterrows(): 
                                                     
                                                sql2="INSERT INTO `customers` 
(`p_code`,`p_name`,`price`,`quantity`,`total_price`)  VALUES (%s, %s, %s, %s, %s)" 
                                                     
                                                cursor.execute(sql2,(col, col1,col2,col3,col4) ) 
                                                     
                                                connection.commit() 
                                                     
                                connection.commit() 
                                 
#117 
 
                                voice.Speak('WOULD YOU LIKE TO ADD MORE INSTANT 
FOOD ITEMS TO YOUR CART') 
                                     
                                print(colored("WOULD YOU LIKE TO ADD MORE INSTANT 
FOOD ITEMS TO YOUR CART ?? (Y/N) ",'yellow')) 
                                     
                                cart1=input() 
                                 
                                print('\n') 
                                 
                    #DISPLAYING BEAUTY AND PERSONAL CARE ITEMS   
                             
                    elif sh==7: 
                         
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\cosmatic.png',width="950", height="400")) 
                         
                        print('\n') 
                             
                        pedf=pd.read_sql('select*from product7',connection) 
                         
                        
print(colored(pedf.to_string(index=False).center(160),'green',attrs=['bold','dark','concealed'])) 
                         
                        print('\n') 
                         
                        voice.Speak('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ') 
                             
                        print(colored('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ','red')) 
                             
                        shop1=input() 
                         
                        print('\n') 
                             
                        if shop1=='y' or shop1=='Y' : 
                                 
                            total=pd.DataFrame=({'price':0}) 
                                 
                            cart1='y' 
                                 
                            while cart1=='y' or cart1=='Y': 
                                 
#118 
 
                                voice.Speak('enter the product code') 
                                     
                                print(colored("ENTER THE PRODUCT CODE",'yellow')) 
                                     
                                pe=input( ) 
                                     
                                print('\n') 
                                 
                                voice.Speak('enter the quantity') 
                                 
                                print(colored("ENTER THE QUANTITY",'yellow')) 
                                     
                                peq=int(input( )) 
                                 
                                print('\n') 
                                     
                                pe_df=pd.read_sql("select*from product7 where pe_code='%s' 
;"%(pe),connection) 
             
                                pe_code=pe_df[['pe_code']]  
                                     
                                pe_name=pe_df[['pe_name']] 
                                     
                                peq_series=pd.Series([peq]) 
                                     
                                pe_price=pe_df[['price']] 
                                     
                                pe_total=pe_price.mul(peq) 
                                     
                                col="`,`".join([str(i) for i in pe_code.pe_code.tolist()]) 
                                     
                                col1="`,`".join([str(i) for i in pe_name.pe_name.tolist()]) 
                                     
                                col2="`,`".join([str(i) for i in peq_series.tolist()]) 
                                     
                                col3="`,`".join([str(i) for i in pe_price.price.tolist()]) 
                                     
                                col4="`,`".join([str(i) for i in pe_total.price.tolist()]) 
                                     
                                for i,row in pe_code.iterrows(): 
                                         
                                    for i,row in pe_name.iterrows(): 
                                             
                                        for i,row in pe_price.iterrows(): 
#119 
 
                                                 
                                            for i,row in pe_total.iterrows(): 
                                                     
                                                sql2="INSERT INTO `customers` 
(`p_code`,`p_name`,`price`,`quantity`,`total_price`)  VALUES (%s, %s, %s, %s, %s)" 
                                                     
                                                cursor.execute(sql2,(col, col1,col2,col3,col4) ) 
                                                     
                                                connection.commit() 
                                                     
                                connection.commit() 
                                 
                                voice.Speak('WOULD YOU LIKE TO ADD MORE  BEAUTY 
& PERSONAL CARE ITEMS TO YOUR CART ') 
                                     
                                print(colored("WOULD YOU LIKE TO ADD MORE  BEAUTY 
& PERSONAL CARE ITEMS TO YOUR CART ?? (Y/N) ",'yellow')) 
                                     
                                cart1=input() 
                                 
                                print('\n') 
                                 
                    #DISPLAYING HOME HYGIENE PRODUCTS 
                                     
                    elif sh==8: 
                         
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\home.png',width="950", height="400")) 
                         
                        print('\n') 
                             
                        phdf=pd.read_sql('select*from product8',connection) 
                         
                        
print(colored(phdf.to_string(index=False).center(160),'green',attrs=['bold','dark','concealed'])) 
                         
                        print('\n') 
                         
                        voice.Speak('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ') 
                             
                        print(colored('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ','red')) 
                             
#120 
 
                        shop1=input() 
                         
                        print('\n') 
                             
                        if shop1=='y' or shop1=='Y' : 
                                 
                            total=pd.DataFrame=({'price':0}) 
                                 
                            cart1='y' 
                                 
                            while cart1=='y' or cart1=='Y': 
                                 
                                voice.Speak("enter the product code") 
                                     
                                print(colored("ENTER THE PRODUCT CODE",'yellow')) 
                                     
                                ph=input( ) 
                                     
                                print('\n') 
                                 
                                print(colored("ENTER THE QUANTITY",'yellow')) 
                                     
                                phq=int(input( )) 
                                 
                                print('\n') 
                                     
                                ph_df=pd.read_sql("select*from product8 where ph_code='%s' 
;"%(ph),connection) 
             
                                ph_code=ph_df[['ph_code']]  
                                     
                                ph_name=ph_df[['ph_name']] 
                                     
                                phq_series=pd.Series([phq]) 
                                     
                                ph_price=ph_df[['price']] 
                                     
                                ph_total=ph_price.mul(phq) 
                                     
                                col="`,`".join([str(i) for i in ph_code.ph_code.tolist()]) 
                                     
                                col1="`,`".join([str(i) for i in ph_name.ph_name.tolist()]) 
                                     
                                col2="`,`".join([str(i) for i in phq_series.tolist()]) 
#121 
 
                                     
                                col3="`,`".join([str(i) for i in ph_price.price.tolist()]) 
                                     
                                col4="`,`".join([str(i) for i in ph_total.price.tolist()]) 
                                     
                                for i,row in ph_code.iterrows(): 
                                         
                                    for i,row in ph_name.iterrows(): 
                                             
                                        for i,row in ph_price.iterrows(): 
                                                 
                                            for i,row in ph_total.iterrows(): 
                                                     
                                                sql2="INSERT INTO `customers` 
(`p_code`,`p_name`,`price`,`quantity`,`total_price`)  VALUES (%s, %s, %s, %s, %s)" 
                                                     
                                                cursor.execute(sql2,(col, col1,col2,col3,col4) ) 
                                                     
                                                connection.commit() 
                                                     
                                connection.commit() 
                                 
                                voice.Speak('WOULD YOU LIKE TO ADD MORE HOME 
HYGIENE & CARE ITEMS TO YOUR CART') 
                                     
                                print(colored("WOULD YOU LIKE TO ADD MORE HOME 
HYGIENE & CARE ITEMS TO YOUR CART ?? (Y/N) ",'yellow')) 
                                     
                                cart1=input() 
                                 
                                print('\n') 
                                 
                    #DISPLAYING MOM AND BABY PRODUCTS 
                     
                    elif sh==9: 
                         
                        display(Image(r'C:\Users\Junaidh\Desktop\Ip 
project\baby.png',width="950", height="400")) 
                         
                        print('\n') 
                             
                        pmdf=pd.read_sql('select*from product9',connection) 
                         
#122 
 
                        
print(colored(pmdf.to_string(index=False).center(160),'green',attrs=['bold','dark','concealed'])
 ) 
                         
                        print('\n') 
                         
                        voice.Speak('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ') 
                             
                        print(colored('DO YOU WANT TO ADD SOMETHING TO YOUR 
CART ','yellow')) 
                             
                        shop1=input() 
                         
                        print('\n') 
                             
                        if shop1=='y' or shop1=='Y' : 
                                 
                            total=pd.DataFrame=({'price':0}) 
                                 
                            cart1='y' 
                                 
                            while cart1=='y' or cart1=='Y': 
                                 
                                voice.Speak('enter the product code') 
                                     
                                print(colored("ENTER THE PRODUCT CODE",'yellow')) 
                                     
                                pm=input( ) 
                                     
                                print('\n') 
                                 
                                voice.Speak('enter the quantity') 
                                 
                                print(colored("ENTER THE QUANTITY",'yellow')) 
                                     
                                pmq=int(input( )) 
                                 
                                print('\n') 
                                     
                                pm_df=pd.read_sql("select*from product9 where pm_code='%s' 
;"%(pm),connection) 
             
                                pm_code=pm_df[['pm_code']]  
#123 
 
                                     
                                pm_name=pm_df[['pm_name']] 
                                     
                                pmq_series=pd.Series([pmq]) 
                                     
                                pm_price=pm_df[['price']] 
                                     
                                pm_total=pm_price.mul(pmq) 
                                     
                                col="`,`".join([str(i) for i in pm_code.pm_code.tolist()]) 
                                     
                                col1="`,`".join([str(i) for i in pm_name.pm_name.tolist()]) 
                                     
                                col2="`,`".join([str(i) for i in pmq_series.tolist()]) 
                                     
                                col3="`,`".join([str(i) for i in pm_price.price.tolist()]) 
                                     
                                col4="`,`".join([str(i) for i in pm_total.price.tolist()]) 
                                     
                                for i,row in pm_code.iterrows(): 
                                         
                                    for i,row in pm_name.iterrows(): 
                                             
                                        for i,row in pm_price.iterrows(): 
                                                 
                                            for i,row in pm_total.iterrows(): 
                                                     
                                                sql2="INSERT INTO `customers` 
(`p_code`,`p_name`,`price`,`quantity`,`total_price`)  VALUES (%s, %s, %s, %s, %s)" 
                                                     
                                                cursor.execute(sql2,(col, col1,col2,col3,col4) ) 
                                                     
                                                connection.commit() 
                                                     
                                connection.commit() 
                                 
                                voice.Speak('WOULD YOU LIKE TO ADD MORE BABY 
ITEMS TO YOUR CART') 
                                     
                                print(colored("WOULD YOU LIKE TO ADD MORE BABY 
ITEMS TO YOUR CART ?? (Y/N) ",'yellow')) 
                                     
                                cart1=input() 
                                 
#124 
 
                                print('\n') 
                   
                            else: 
                                 
                                print('\n') 
                                 
                                break 
                                 
                    voice.Speak('WOULD YOU LIKE TO VISIT OTHER PRODUCTS') 
                                     
                    print(colored("WOULD YOU LIKE TO VISIT OTHER PRODUCTS  ?? 
(Y/N) ",'yellow')) 
                                     
                    shopping=input()    
                     
                    print('\n') 
                     
            elif shop_choice==3: 
                 
                shop='n' 
                                     
 
#DATA VISUALIZATION 
                 
    elif menu_choice == 4: 
         
        animation = ["LOADING [■□□□□□□□□□]","LOADING [■■□□□□□□□□]", 
"LOADING [■■■□□□□□□□]",  
             "LOADING [■■■■□□□□□□]", "LOADING [■■■■■□□□□□]", "LOADING 
[■■■■■■□□□□]", 
             "LOADING [■■■■■■■□□□]", "LOADING [■■■■■■■■□□]", "LOADING 
[■■■■■■■■■□]",  
             "LOADING [■■■■■■■■■■]"] 
         
        for i in range(len(animation)): 
     
            time.sleep(1) 
     
            sys.stdout.write("\r" + animation[i % len(animation)]) 
     
            sys.stdout.flush() 
 
        sys.stdout.write('\rDone!                          ') 
         
#125 
 
        print('\n')    
         
        graph='y' 
         
        while graph=='y' or graph=='Y': 
             
            voice.Speak('do you want to see our statistics') 
             
            print(colored("DO YOU WANT TO SEE OUR STATISTICS (Y/N) 
",'yellow')) 
             
            gh=input() 
             
            print('\n') 
             
            if gh=='y' or gh=='Y': 
                 
                voice.Speak('press 1 to know data about game corner') 
                 
                print(colored('1. DATA ABOUT GAME CORNER'.center(200),'yellow')) 
                 
                voice.Speak('press 2 to know data about shopping center') 
                 
                print(colored('2. DATA ABOUT SHOPPING 
CENTER'.center(200),'yellow')) 
                 
                print('\n') 
                 
                voice.Speak('ENTER YOUR CHOICE  : ') 
                 
                print(colored("ENTER YOUR CHOICE  : ",'red')) 
             
                gh1=int(input()) 
                 
                print('\n') 
                 
                 
                #DATA ABOUT GAME CORNER 
             
                if gh1==1: 
                     
                    #RADAR CHART 
                     
                    voice.Speak('here is the data about game corner') 
#126 
 
                     
                    print(colored("RADAR CHART OF GAME 
CORNER".center(200),'red')) 
                     
                    print('\n') 
                          
                    categories = ['NUMBER GUESSING','TIK TAK TOE', 
                                  'ROCK,PAPER & SCISSORS', 
                                  'TOSS', 'DICE ROLLING','HANGMAN','HAND-CRICKET'] 
                     
                    fig = go.Figure() 
 
                    fig.add_trace(go.Scatterpolar( 
                        r=[4, 5, 3, 4, 3,2,4], 
                        theta=categories, 
                        fill='toself', 
                        name='NO. OF PLAYER PLAYED' 
                    )) 
                     
                    fig.add_trace(go.Scatterpolar( 
                        r=[2, 3, 2.5, 2, 2,1,3.5], 
                        theta=categories, 
                        fill='toself', 
                        name='NO. OF PLAYER WON' 
                    )) 
                     
                    fig.update_layout( 
                        polar=dict( 
                            radialaxis=dict( 
                                visible=True, 
                                range=[0, 6] 
                            )), 
                        showlegend=True 
                    ) 
                     
                    fig.show() 
                     
                    print('\n') 
                     
                    voice.Speak('DO YOU WANT TO CONTINUE') 
                     
                    print(colored('DO YOU WANT TO CONTINUE (Y/N) :','yellow')) 
                             
                    graph2=input() 
#127 
 
                     
                    print('\n') 
                     
                #DATA ABOUT SHOPPING CENTER 
                     
                elif gh1==2: 
                     
                    graph2='y' 
         
                    while graph2=='y' or graph2=='Y': 
                 
                        voice.Speak('PRESS 1 TO SEE PIE CHART OF PRODUCTS ') 
                     
                        print(colored('1. PIE CHART OF PRODUCTS '.center(200),'yellow')) 
                         
                        voice.Speak('PRESS 2 TO SEE A LINE CHART about GROWTH OF 
DREAM MART') 
                         
                        print(colored('2. LINE CHART (GROWTH OF DREAM 
MART)'.center(200),'yellow' )) 
                         
                        voice.Speak('press 3 to see bar graph about products sold') 
                         
                        print(colored('3. BAR GRAPH ABOUT PRODUCTS 
SOLD'.center(200),'yellow')) 
                         
                        print('\n') 
                         
                        voice.Speak('enter your choice') 
                         
                        print(colored("ENTER YOUR CHOICE  :",'yellow')) 
                         
                        g_choice=int(input( )) 
                         
                        print('\n') 
                         
                        if g_choice==1: 
                             
                            #PIE CHART 
                             
                            voice.Speak('here is the pie chart of products') 
                             
                            products = ['FOODGRAINS,OILS & MASALAS',  
                                        'FRUITS & VEGETABLES', 'DAIRY & BAKERY', 
#128 
 
                                        'SNACKS STATION','BEVARAGES CORNER', 
                                        'INSTANT FOODS','BEAUTY & PERSONAL CARE', 
                                        'HOME HYGIENE & CARE','MOM & BABY'] 
                             
                            sizes = [20,27,14,11,9,7,5.5,3.5,3] 
                             
                            colors = ['gold', 'yellowgreen', 'lightcoral', 
'lightskyblue','cyan','yellow','pink','m','orange'] 
                             
                            explode = (0, 0.1, 0,0,0,0,0,0,0)   
                         
                            wp = { 'linewidth' : 1, 'edgecolor' : "white" } 
                             
                            plt.figure(figsize=(8,10)) 
                             
                            plt.title("PIE CHART OF PRODEUCTS",fontsize=22,color='red') 
                             
                            plt.pie(sizes,labels=products, explode=explode, 
                                    colors=colors,wedgeprops = wp, textprops = dict(color 
="black"), 
                                    autopct='%1.1f%%', shadow=True, startangle=120)  
 
                            plt.legend(products,title='PRODUCTS',loc='lower right') 
 
                            plt.axis('equal') 
 
                            plt.show() 
                             
                            print('\n') 
                             
                            voice.Speak('DO YOU WANT TO CONTINUE ') 
                             
                            print(colored('DO YOU WANT TO CONTINUE  :','yellow')) 
                             
                            graph2=input() 
                             
                            print('\n') 
                             
                        #;INE CHART 
 
                        elif g_choice==2: 
                             
                            voice.Speak('here is a line chart of growth of dream mart') 
                             
#129 
 
                            x = [2014,2015,2016,2017,2018,2019,2020,2021] 
                             
                            y = [25000,15000,40000,37000,51000,48000,55000,71000] 
                             
                            plt.plot(x, y,'cyan',linestyle='dashed') 
                             
                            plt.xlabel("YEARS") 
                             
                            plt.ylabel("PRODUCTS SOLD") 
                             
                            plt.title('GROWTH OF DREAM MART',fontsize=22,color='red') 
                             
                            plt.show() 
                             
                            print('\n') 
                                                         
                            voice.Speak('do you want to continue') 
                             
                            print(colored('DO YOU WANT TO CONTINUE  :','yellow')) 
                             
                            graph2=input()            
                             
                            print('\n') 
                             
                        #BAR GRAPH 
                     
                        elif g_choice==3: 
                             
                            voice.Speak('bar graph of foodgrains oil and masalas') 
                             
                            foodgrain=["DALS & PULSES","ATTA & FLOURS", 
                                       "SUGAR & SALT","RICE PRODUCTS", 
                                       "SOYA & GRAINS","DRY FRUITS & NUTS", 
                                       "EDIBLE OILS","SPICES & MASALAS"] 
 
                            production1=[6500,7500,7000,8000,6000,5500,7500,7000] 
 
                            plt.figure(figsize = (15, 5)) 
 
                            c=['gold', 'yellowgreen', 'lightcoral', 
'lightskyblue','cyan','yellow','pink','red'] 
 
                            plt.bar(foodgrain,production1,color=c) 
 
#130 
 
                            plt.title("FOODGRAINS, OIL & 
MASALAS",fontsize=22,color='red') 
                             
                            plt.xlabel("PRODUCTS") 
 
                            plt.ylabel("NO. OF PRODUCTS SOLD SO FAR ") 
 
                            plt.show() 
                             
                            print('\n') 
                             
                            voice.Speak('bar graph of snacks station') 
                             
                            snacks=["CHIPS","CHOCOLATES & SWEETS" 
                                    ,"FROZEN SNACKS","BISCUITS & COOKIES", 
                                    "CAKES & RUSK","NAMKEEN & SAVOURIES"] 
 
                            production2=[5000,4000,2500,6000,2000,3000] 
 
                            plt.figure(figsize = (13, 5)) 
 
                            c=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','cyan','yellow'] 
 
                            plt.bar(snacks,production2,color=c) 
 
                            plt.title("SNACKS STATION",fontsize=22,color='red') 
                             
                            plt.xlabel("PRODUCTS") 
 
                            plt.ylabel("NO. OF PRODUCTS SOLD SO FAR ") 
 
                            plt.show() 
                             
                            print('\n') 
                             
                            voice.Speak('bar graph of diary and bakery') 
                             
                            diary=["MILK & MILK POWDER","CAKES & RUSK", 
                                   "BREADS & BUNS","BUTTER, CHEESE & CREAM", 
                                   "CURD & PANNER","SHAKES & BUTTERMILK"] 
                             
                            production3=[5000,2000,3000,4000,3500,2500] 
                             
                            plt.figure(figsize = (13, 5)) 
#131 
 
 
                            c=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','cyan','yellow'] 
 
                            plt.bar(diary,production3,color=c) 
 
                            plt.title("DIARY & BAKERY",fontsize=22,color='red') 
                             
                            plt.xlabel("PRODUCTS") 
 
                            plt.ylabel("NO. OF PRODUCTS SOLD SO FAR ") 
 
                            plt.show() 
                             
                            print('\n') 
                             
                            voice.Speak('bar graph of beverage corner') 
                             
                            BEVERAGE=["WATER & SODA","SHAKES & BUTTERMILK", 
                                      "TEA & COFFEE","HEALTH DRINKS","COLD DRINKS", 
                                      "JUICE & SQUASHES"] 
                             
                            production4=[1000,2000,3500,3500,3000,2500] 
 
                            plt.figure(figsize = (13, 5)) 
 
                            c=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','cyan','yellow'] 
 
                            plt.bar(BEVERAGE,production4,color=c) 
 
                            plt.title("BEVERAGE CORNER",fontsize=22,color='red') 
                             
                            plt.xlabel("PRODUCTS") 
 
                            plt.ylabel("NO. OF PRODUCTS SOLD SO FAR ") 
 
                            plt.show() 
                             
                            print('\n') 
                             
                            voice.Speak('bar graph of instant foods') 
                     
                            instant=["NOODLES,SOUPS & PASTA","JAM & HONEY", 
                                     "BREAKFAST CEREALS","  DESSERT ", 
                                     "SAUCES & PICKELS","PAPPAD & FRYUMS"] 
#132 
 
 
                            production5=[5000,2000,3000,4000,3500,2500] 
 
                            plt.figure(figsize = (13, 5)) 
 
                            c=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','cyan','yellow'] 
 
                            plt.bar(instant,production5,color=c) 
 
                            plt.title("INSTANT FOODS",fontsize=22,color='red') 
                             
                            plt.xlabel("PRODUCTS") 
 
                            plt.ylabel("NO. OF PRODUCTS SOLD SO FAR ") 
 
                            plt.show() 
                             
                            print('\n') 
                             
                            voice.Speak('bar graph of beauty and personal care') 
 
                            cosmatics=["MAKE UP","CREAM & LOTIONS","   SOAP & 
BODY WASH", 
                                       "  HAIR OIL & GELS","FACE WASH","DEO & 
PERFUME", 
                                       "SHAMPOO","TOOTHPASTE "] 
 
                            production6=[1000,1500,2500,1000,1500,1500,2000,1000] 
 
                            plt.figure(figsize = (15, 5)) 
 
                            c=['gold', 'yellowgreen', 'lightcoral', 
'lightskyblue','cyan','yellow','pink','red'] 
 
                            plt.bar(cosmatics,production6,color=c) 
 
                            plt.title("BEAUTY & PERSONAL CARE",fontsize=22,color='red') 
                             
                            plt.xlabel("PRODUCTS") 
 
                            plt.ylabel("NO. OF PRODUCTS SOLD SO FAR ") 
 
                            plt.show() 
                             
#133 
 
                            print('\n') 
                             
                            voice.Speak('bar graph of home hygiene and care') 
    
                            home=["DETERGENTS","HOUSEHOLD CLEANERS", 
                                  "  OTHER HOME NEEDS","UTENSIL CLEANERS"] 
 
                            production7=[2000,1000,500,1500] 
 
                            plt.figure(figsize = (10, 5)) 
 
                            c=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'] 
 
                            plt.bar(home,production7,color=c) 
 
                            plt.title("HOME HYGIENE & CARE",fontsize=22,color='red') 
                         
                            plt.xlabel("PRODUCTS") 
 
                            plt.ylabel("NO. OF PRODUCTS SOLD SO FAR ") 
 
                            plt.show() 
                             
                            print('\n') 
                             
                            voice.Speak('mom and baby') 
 
                            baby=["BABY FOOD","DIAPER & WIPES", 
                                  "BODY SOAP & SHAMPOO","BABY OIL & POWDER"] 
 
                            production8=[250,1250,1000,500] 
 
                            plt.figure(figsize = (10, 5)) 
 
                            c=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'] 
 
                            plt.bar(baby,production8,color=c) 
 
                            plt.title("MOM & BABY",fontsize=22,color='red') 
                             
                            plt.xlabel("PRODUCTS") 
 
                            plt.ylabel("NO. OF PRODUCTS SOLD SO FAR ") 
 
#134 
 
                            plt.show() 
                             
                            print('\n') 
                             
                            voice.Speak('DO YOU WANT TO CONTINUE') 
                             
                            print(colored('DO YOU WANT TO CONTINUE  :','yellow')) 
                             
                            graph2=input() 
                             
                            print('\n') 
     
 
            else : 
                 
                break 
                 
    elif menu_choice==5: 
         
        voice.Speak('THANK YOU FOR VISITING DREAM MART') 
         
        print(colored('THANK YOU FOR VISITING DREAM 
MART'.center(180),'red')) 
         
        break 
