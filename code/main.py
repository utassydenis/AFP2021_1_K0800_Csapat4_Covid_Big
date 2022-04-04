from datetime import datetime
from kivy import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
import requests
import shutil
import os
import mysql.connector

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

#Config.set('graphics','resizeable',True)
my_window = Tk()
width_value = my_window.winfo_screenwidth()
height_value = my_window.winfo_screenheight()

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import csv


Builder.load_file("kv-files/covid.kv")
#Config.set("graphics", "width", "1050")
#Config.set("graphics", "height", "850")
#Config.set("graphics", "resizable", "0")

Config.set("graphics", "width", width_value)
Config.set("graphics", "height", height_value)

class Covid(FloatLayout):
    def __init__(self, **kwargs):
        super(Covid, self).__init__(**kwargs)

    #To-do eleje Milán
    def prediction_algorythm(self):
        region_spinner = self.ids.régió.text
        if self.ids.mire.text == 'Halálesetek':
            column = "deaths"
        else:
            column = "cases"

        mydb = mysql.connector.connect(host="localhost", user="root", database="covid_database")
        mycursor = mydb.cursor()
        if not(region_spinner =="World" or region_spinner == "AFRO" or region_spinner == "AMRO" or region_spinner == "EMRO" or region_spinner == "EURO" or region_spinner == "SEARO" or region_spinner == "WPRO"):
            fileWrite = open(region_spinner + ".csv", "w")
            fileWrite.write("day;month;year;cases;deaths;countriesAndTerritories\n")
            sql = "SELECT * FROM covid WHERE COUNTRY = '{0}';".format(region_spinner)
            mycursor.execute(sql)
            result = mycursor.fetchall();
            for x in result:
                dateDarabok = str(x[1]).split("-")
                newdate = dateDarabok[2] + ";" + dateDarabok[1] + ";" + dateDarabok[0]
                fileWrite.write(newdate +";" + str(x[4]) +";" +str(x[5]) + ";" + str(x[2]) + "\n")
            fileWrite.close()
            mycursor.close()
            mydb.close()
        reader = csv.reader(file)
        lines = int(len(list(reader))) - 1
        print('Number of rows: ', lines)

        data = pd.read_csv(self.ids.régió.text + '.csv', sep=';')
        #data = data[int(self.ids.napok.text), column]
        data = data[['day', column]]
        print('-' * 30);
        print('HEAD');
        print('-' * 30)
        print(data.head())

        print('-' * 30);
        print('PREPARE DATA');
        print('-' * 30)
        x = np.array(data['day']).reshape(-1, 1)
        y = np.array(data[column]).reshape(-1, 1)
        plt.plot(y, '-m')

        polyFeat = PolynomialFeatures(degree=4)
        x = polyFeat.fit_transform(x)

        print('-' * 30);
        print('TRAINING DATA');
        print('-' * 30)
        model = linear_model.LinearRegression()
        model.fit(x, y)
        accuracy = model.score(x, y)
        print(f'Accuracy:{round(accuracy * 100, 3)} %')
        y0 = model.predict(x)

        days = int(self.ids.napok.text)
        print('-' * 30);
        print('PREDICTION');
        print('-' * 30)
        print(f'Prediction - Cases after {days} days: ', end='')
        print(round(int(model.predict(polyFeat.fit_transform([[lines + days]])))), 'people')

        x1 = np.array(list(range(1, lines + days))).reshape(-1, 1)
        y1 = model.predict(polyFeat.fit_transform(x1))
    #To-do vége Milán
        
    # ----- update_db által meghívott fgvnyek -----

    def dir_exist(self):
        if not os.path.exists("database"):
            os.makedirs("database")

    def download_csv(self):
        print("Source file doesn't exist. Downloading...")
        url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'
        r = requests.get(url, allow_redirects=True)
        open('database/data.csv', 'wb').write(r.content)
        print("Source file downloaded.")

    def make_Trimmed_file(self):
        if not os.path.exists("database/dataTrim.csv"):
            print("Trim file doesn't exist. Making trim file.")
            open("database/dataTrim.csv", "x")
            print("Trim file created")
        else:
            print("Resetting trim file")
            open('database/dataTrim.csv', "w").close()
            print("Trim file reset success.")

    def trim_data(self):
        print("Trimming source file.")
        inF = open("database/data.csv")
        outF = open("database/dataTrim.csv", "w")
        next(inF)
        for line in inF:
            darabok = line.split(sep=",")
            if darabok[2] == '"occupied Palestinian territory':
                darabok[2] = 'occupied Palestinian territory including east Jerusalem'
                outF.write(darabok[0] + "," + darabok[2] + "," + darabok[4] + "," + darabok[5] + "," + darabok[7])
                outF.write("\n")
            else:
                outF.write(darabok[0] + "," + darabok[2] + "," + darabok[3] + "," + darabok[4] + "," + darabok[6])
                outF.write("\n")
        inF.close()
        outF.close()
        print("Trim done.")

    def check_if_db_exists(self):
        mydb = mysql.connector.connect(host="localhost", user="root")
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        database_exist = False
        for x in mycursor:
            if str(x) == "('covid_database',)":
                database_exist = True
        if database_exist == False:
            print("Database doesn't exist. Creating database.")
            mycursor.execute("CREATE DATABASE covid_database")
            print("Database created.")
        mydb.close()
        mycursor.close()

    def check_if_table_exists(self):
        print("Checking if table exists.")
        mydb = mysql.connector.connect(host="localhost", user="root", database="covid_database")
        mycursor = mydb.cursor()
        mycursor.execute("SHOW TABLES")
        for x in mycursor:
            if str(x) == "('covid',)":
                mycursor.close()
                mydb.close()
                print("Table exists.")
                return True
        mycursor.close()
        mydb.close()
        print("Table doesn't exist.")
        return False

    def create_table(self):
        mydb = mysql.connector.connect(host="localhost", user="root", database="covid_database")
        mycursor = mydb.cursor()
        print("Creating table.")
        mycursor.execute("CREATE TABLE covid (ID int NOT NULL AUTO_INCREMENT,  DATE date,COUNTRY varchar (255),REGION varchar(255), INFECTED_NEW int, DEATH_NEW int, PRIMARY KEY (ID));")
        print("Table created.")
        print("Populating table.")
        sql = "INSERT INTO Covid(DATE,COUNTRY,REGION,INFECTED_NEW,DEATH_NEW) VALUES (%s,%s,%s,%s,%s)"
        file = open("database/dataTrim.csv", "r")
        for line in file:
            darabok = line.split(sep=",")
            if(int(darabok[3]) < 0):
                darabok[3] = '0'
            if(int(darabok[4]) <  0):
                darabok[4] = '0'
            val = (darabok[0], darabok[1], darabok[2], darabok[3],darabok[4])
            mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()

    def reset_db(self):
        mydb = mysql.connector.connect(host="localhost", user="root", database="covid_database")
        mycursor = mydb.cursor()
        print("Resetting database")
        mycursor.execute("DELETE FROM covid;")
        mycursor.execute("TRUNCATE TABLE covid;")
        sql = "INSERT INTO Covid(DATE,COUNTRY,REGION,INFECTED_NEW,DEATH_NEW) VALUES (%s,%s,%s,%s,%s)"
        file = open("database/dataTrim.csv", "r")
        for line in file:
            darabok = line.split(sep=",")
            if(int(darabok[3]) < 0):
                darabok[3] = '0'
            if(int(darabok[4]) <  0):
                darabok[4] = '0'
            val = (darabok[0], darabok[1], darabok[2], darabok[3],darabok[4])
            mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()
    # ----- update_db által meghívott fgvnyek -----

    # ----- search_db által meghívott fgvnyek -----
    def check_separator(self,from_value,till_value):
        if (till_value.find("-") > 0 and from_value.find("-")):
            return True
        else:
            return False

    def check_if_date_correct(self,from_section,till_section):
        mydb = mysql.connector.connect(host="localhost", user="root", database="covid_database")
        mycursor = mydb.cursor()
        datemin_query = "SELECT MIN(DATE) FROM covid"
        datemax_query = "SELECT MAX(DATE) FROM covid"
        statements = [datemin_query, datemax_query]
        for statement in statements:
            mycursor.execute(statement)
            if statement.find("MIN") > 0:
                date_min_arr = re.sub('[^0-9,]','',str(mycursor.fetchall())).replace(",","-")[:-1]
            else:
                date_max_arr = re.sub('[^0-9,]','',str(mycursor.fetchall())).replace(",","-")[:-1]

        date_min = datetime.strptime(''.join(date_min_arr), '%Y-%m-%d')
        date_max = datetime.strptime(''.join(date_max_arr), '%Y-%m-%d')
        try:
            from_section_date = datetime.strptime(from_section, '%Y-%m-%d')
            till_section_date = datetime.strptime(till_section, '%Y-%m-%d')
            if date_min <= from_section_date <= till_section_date <= date_max:
                mydb.close()
                mycursor.close()
                return True
            else:
                mydb.close()
                mycursor.close()
                return False
        except ValueError:
            print("Nem dátumot adott meg.")

    def return_values(self,spinner_section,from_section,till_section):
        mydb = mysql.connector.connect(host="localhost", user="root", database="covid_database")
        mycursor = mydb.cursor()
        if spinner_section == "World":
            sql_death = "SELECT SUM(DEATH_NEW) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}';".format(from_section,till_section)
            sql_infected = "SELECT SUM(INFECTED_NEW) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}';".format(from_section, till_section)
        elif spinner_section == "AFRO" or spinner_section == "AMRO" or spinner_section == "EMRO" or spinner_section == "EURO" or spinner_section == "SEARO" or spinner_section == "WPRO":
            sql_death = "SELECT SUM(DEATH_NEW) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}' AND REGION = '{2}';".format(from_section, till_section, spinner_section)
            sql_infected = "SELECT SUM(INFECTED_NEW) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}' AND REGION = '{2}';".format(from_section, till_section, spinner_section)
        else:
            sql_death = "SELECT SUM(DEATH_NEW) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}' AND COUNTRY ='{2}';".format(from_section, till_section, spinner_section)
            sql_infected = "SELECT SUM(INFECTED_NEW) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}' AND COUNTRY ='{2}';".format(from_section, till_section, spinner_section)
        statements = [sql_death, sql_infected]
        for statement in statements:
            mycursor.execute(statement)
            if statement.find("DEATH_NEW") > 0:
                death_sum = mycursor.fetchall()
            else:
                infected_sum = mycursor.fetchall()
        self.ids.HalottPlaceHolder.text = re.sub("[^0-9]", "", str(death_sum))
        self.ids.FertőPlaceHolder.text = re.sub("[^0-9]", "", str(infected_sum))
        mycursor.close()
        mydb.close()
    # ----- search_db által meghívott fgvnyek -----

    def update_db(self):
        print("Update started!")
        self.dir_exist()
        if not os.path.exists("database/data.csv"):
            self.download_csv()
        self.make_Trimmed_file()
        self.trim_data()
        self.check_if_db_exists()
        self.check_if_table_exists()
        if not self.check_if_table_exists():
            self.create_table()
        else:
            self.reset_db()
        shutil.rmtree("database")
        print("Done updating")

    def search_db(self):
        if not self.check_separator(self.ids.tól.text, self.ids.ig.text):
            print("Hibás elválasztók! Kérem használjon '-'-t")
        else:
            if self.check_if_date_correct(self.ids.tól.text,self.ids.ig.text):
                self.return_values(self.ids.régió.text, self.ids.tól.text, self.ids.ig.text)
            else:
                print("Kérem adjon meg más dátumokat.")

    def error_report_press(self):
        root = Tk()
        frame_header = ttk.Frame(root)
        frame_header.pack()
        headerlabel = ttk.Label(frame_header, text='Hibabejelentés', foreground='Black',
                                font=('Times New Roman', 24))
        headerlabel.grid(row=0, column=1)
        messagelabel = ttk.Label(frame_header,
                                 text='Kérem írja le, mit gondol a programról!',
                                 foreground='purple', font=('Arial', 10))
        messagelabel.grid(row=1, column=1)

        frame_content = ttk.Frame(root)
        frame_content.pack()
        myvar = StringVar()
        var = StringVar()
        namelabel = ttk.Label(frame_content, text='Name')
        namelabel.grid(row=0, column=0, padx=5, sticky='sw')
        entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
        entry_name.grid(row=1, column=0)

        emaillabel = ttk.Label(frame_content, text='Email')
        emaillabel.grid(row=0, column=1, sticky='sw')
        entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
        entry_email.grid(row=1, column=1)

        commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 10))
        commentlabel.grid(row=2, column=0, sticky='sw')
        textcomment = Text(frame_content, width=55, height=10)
        textcomment.grid(row=3, column=0, columnspan=2)

        textcomment.config(wrap='word')

        def clear():
            messagebox.showinfo(title='clear', message='Ki szeretnéd törölni a megadottakat?')
            entry_name.delete(0, END)
            entry_email.delete(0, END)
            textcomment.delete(1.0, END)

        def submit():
            print('Name:{}'.format(myvar.get()))
            print('Email:{}'.format(var.get()))
            print('Comment:{}'.format(textcomment.get(1.0, END)))
            messagebox.showinfo(title='Elküldés', message='Köszönjük a visszajelzést, a véleményed mentésre került.')
            entry_name.delete(0, END)
            entry_email.delete(0, END)
            textcomment.delete(1.0, END)

            sender_email = "covidapptester@gmail.com"
            rec_email = "rkevin99@gmail.com" #Ide ird be a mailod, ha tesztelni akarod
            password = "Covidteszt!!11"
            message = textcomment.get(1.0, END)

            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = rec_email
            message['Subject'] = 'Hibabejelentés'
            message.attach(MIMEText(textcomment.get(1.0, END)))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = message.as_string()
            server.sendmail(sender_email, rec_email, text)
            server.quit()

        submitbutton = ttk.Button(frame_content, text='Elküldés', command=submit).grid(row=4, column=0, sticky='e')
        clearbutton = ttk.Button(frame_content, text='Törlés', command=clear).grid(row=4, column=1, sticky='w')

        mainloop()

class CovidApp(App):
    def build(self):
        return Covid()
if __name__ == '__main__':
    CovidApp().run()