from datetime import datetime
from kivy import Config
from kivy.app import  App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
import requests
import os.path
import mysql.connector
import re

Builder.load_file("kv-files/covid.kv")
Config.set("graphics", "width", "1050")
Config.set("graphics", "height", "850")
Config.set("graphics", "resizable", "0")

class Covid(FloatLayout):
    def __init__(self, **kwargs):
        super(Covid, self).__init__(**kwargs)
    # ----- update_db által meghívott fgvnyek -----

    def dir_exist(self):
        if not os.path.exists("database"):
            os.makedirs("database")

    def download_cvs(self):
        print("Source file doesn't exist. Downloading...")
        url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv/data.csv'
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
            if darabok[6] == '"Bonaire':
                darabok[6] = "Bonaire_Saint_Eustatius_and_Saba"
                outF.write(darabok[0] + "," + darabok[4] + "," + darabok[5] + "," + darabok[6] + "," + darabok[11])
                outF.write("\n")
            else:
                outF.write(darabok[0] + "," + darabok[4] + "," + darabok[5] + "," + darabok[6] + "," + darabok[10])
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
        mycursor.execute("CREATE TABLE covid (ID int NOT NULL AUTO_INCREMENT,  DATE date, INFECTED_NUM int, DEATH_NUM int, COUNTRY varchar(255), CONTINENT varchar(255) , INFECTED_TOTAL_CASES int , DEATH_TOTAL_CASES int , PRIMARY KEY (ID));")
        print("Table created.")
        print("Populating table.")
        sql = "INSERT INTO Covid(DATE,INFECTED_NUM,DEATH_NUM,COUNTRY,CONTINENT) VALUES (%s, %s,%s,%s,%s)"
        file = open("database/dataTrim.csv", "r")
        for line in file:
            darabok = line.split(sep=",")
            convert = darabok[0].split(sep="/")
            date = convert[2] + "-" + convert[1] + "-" + convert[0]
            val = (date, darabok[1], darabok[2], darabok[3], darabok[4])
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
        sql = "INSERT INTO Covid(DATE,INFECTED_NUM,DEATH_NUM,COUNTRY,CONTINENT) VALUES (%s, %s,%s,%s,%s)"
        file = open("database/dataTrim.csv", "r")
        for line in file:
            darabok = line.split(sep=",")
            convert = darabok[0].split(sep="/")
            date = convert[2] + "-" + convert[1] + "-" + convert[0]
            val = (date, darabok[1], darabok[2], darabok[3], darabok[4])
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
        if spinner_section == "Világ":
            sql_death = "SELECT SUM(DEATH_NUM) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}';".format(from_section,till_section)
            sql_infected = "SELECT SUM(INFECTED_NUM) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}';".format(from_section, till_section)
        elif spinner_section == "Európa":
            sql_death = "SELECT SUM(DEATH_NUM) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}' AND CONTINENT = 'Europe\n';".format(from_section, till_section)
            sql_infected = "SELECT SUM(INFECTED_NUM) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}' AND CONTINENT = 'Europe\n';".format(from_section, till_section)
        else:
            sql_death = "SELECT SUM(DEATH_NUM) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}' AND COUNTRY ='{2}';".format(from_section, till_section, spinner_section)
            sql_infected = "SELECT SUM(INFECTED_NUM) FROM covid WHERE DATE >= '{0}' AND DATE <= '{1}' AND COUNTRY ='{2}';".format(from_section, till_section, spinner_section)
        statements = [sql_death, sql_infected]
        for statement in statements:
            mycursor.execute(statement)
            if statement.find("DEATH_NUM") > 0:
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
            self.download_cvs()
        self.make_Trimmed_file()
        self.trim_data()
        self.check_if_db_exists()
        self.check_if_table_exists()
        if not self.check_if_table_exists():
            self.create_table()
        else:
            self.reset_db()
        print("Done updating")

    def search_db(self):
        if not self.check_separator(self.ids.tól.text, self.ids.ig.text):
            print("Hibás elválasztók! Kérem használjon '-'-t")
        else:
            if self.check_if_date_correct(self.ids.tól.text,self.ids.ig.text):
                self.return_values(self.ids.régió.text, self.ids.tól.text, self.ids.ig.text)
            else:
                print("Kérem adjon meg más dátumokat.")

class CovidApp(App):
    def build(self):
        return Covid()
if __name__ == '__main__':
    CovidApp().run()