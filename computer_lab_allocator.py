from datetime import datetime
import pandas as pd
import csv
import numpy as np
import os
import shutil
from os import path

PATH = './computer.csv' #Path to actual CSV file on disk
labels = ['Rollno', 'Name', 'Date', 'Time'] #2CSV labels
ADMIN_PASSWORD = 'p' #Default admin password

def add_data(data): #Pass dictionary of data created to enter into CSV
    df = pd.DataFrame(data)
    if os.path.exists(PATH):        #if path exists firstly
        df.to_csv(PATH, index=False, mode='a', header=0)
    else:
        df.to_csv(PATH, index=False, mode='w')

def delete_data(): #Queries for user input and deletes ALL records of user form CSV
    df = read_data()
    if df is None: return
    print("Enter the roll no whose data you want to be deleted:")
    newDf = df[~df.Rollno.isin([input()])]
    os.remove(PATH)
    newDf.to_csv(PATH, index=False)

def read_data(): #Reads and returns all data from CSV, handles subsequent exceptions
    try:
        df = pd.read_csv(PATH)
        return df
    except pd.errors.EmptyDataError:
        print("No data is present!")
        return None
    except FileNotFoundError:
        print('No CSV file exists!')
        return None

def update_data():
    df = read_data()
    if df is None: return
    #print("Enter the roll no whose data is to be updated:")
    #newDf = df[~df.Rollno.isin([input()])]
    print('Do you want to update name(1) or rollno(2) ?')
    c=int(input())
    if(c==1):
        print("Type the name which is to be changed:")
        sname=input()
        #df.loc[df['Name']==sname]
        #findL =stud
        print("Type the new name:")
        rname=input()
        #df['Name'].replace(sname,rname, inplace= True)
        #newDf = df[~df.Rollno.isin([input()])]
        #print(df)
        df.to_csv(PATH, index=False, mode='a')
        #df.loc[df['Name']==sname].replace(sname,rname)
        #df.loc[df['Name']==sname]=rname
        #print(df)
        #replaceL = rname
        col='Name'
        df[col].replace(sname, rname ,inplace=True)
        #if path.exists("computer.csv")
        #df = read_data()
        #computer.csv.close()
        #new_column = pd.Series([rname],name='Name' , index=[2])
        #df.update(new_column)
        df.to_csv('computer.csv', index=False) 
        print(df)
    elif(c==2):
        print("Type the roll no which is to be changed:")
        srollno=int(input())
        print("Type the new roll no:")
        rrollno=int(input())
        df.to_csv(PATH, index=False, mode='a')
        col='Rollno'
        df[col].replace(srollno, rrollno ,inplace=True)
        df.to_csv('computer.csv', index=False) 
        print(df) 



# delete_data('15CE1038')
print('WELCOME TO THE LAB')
print('IF YOU ARE A USER ENTER:- 1')
print('IF YOU ARE AN ADMIN ENTER:- 2')
x = int(input())
if(x == 1):
        #print('ENTER YOUR NAME AND ROLL NUMBER:-')
        #y=input()
        #z=int(input())
        #localtime = time.localtime(time.time())
        #print("Local current time :", localtime)
    # fields = ['Rollno', 'Name', 'Date', 'Time']
    # rows = []
    roll_no = []
    stud = []
    dates = []
    times = []
    num = int(input("How many students?: "))
    for i in range(num):
        number = input("Input roll no. of the student: ")
        roll_no.append(number)
        name = input("Input name of student: ")
        stud.append(name)
        date = datetime.now().strftime('%d/%m/%y')
        dates.append(date)
        time = datetime.now().strftime('%H:%M')
        times.append(time)

    # with open(PATH, 'a') as out:
    #     csvWriter = csv.writer(out, delimiter=' ')
    #     csvWriter.writerow(fields)

    # writing the data rows
        # csvWriter.writerows(rows)
    # for i in range(num):
    #     rollno = roll_no[i]
    #     b = stud[i]
    #     da = dates[i]
    #     ti = times[i]

    dict = {
        labels[0]: roll_no, 
        labels[1]: stud,
        labels[2]: dates,
        labels[3]: times
    }
    add_data(dict)

        # csvWriter.writerow(row)
        # add_data(row)

elif(x == 2):
        print('ENTER PASSWORD')
        adminPass = input()
        if(adminPass == ADMIN_PASSWORD):
            print('WELCOME ADMIN')
            while(True):
                print("\n1) Read\n2) Delete\n3) Update\n4) Exit")
                x = int(input("Enter your choice:"))
                if(x == 1):
                    print(read_data())
                    #with open(PATH,'r') as out:
                    #csv_reader = csv.reader(out)
                    #for line in csv_reader:
                    #print(line)
                elif(x == 2):
                    delete_data()
                        # df = pd.read_csv(PATH)
                        # df.drop(index=[1], axis=0, inplace=True)
                        # df.head()
                        # df = pd.read_csv(PATH)
                        # print(df)
                    #with open(PATH, 'rb') as inp, open(PATH, 'wb') as out:
                    #writer = csv.writer(out)
                    #for row in csv.reader(inp):
                    #if row[1] != y:
                    #writer.writerow(row)
                elif(x == 3):
                    print("Update") #TODO: Update function to be called!!
                    update_data()

                elif(x == 4):
                    break
                else:
                    print("Invalid input!")
        else:
            print('ENTER VALID PASSWORD')
