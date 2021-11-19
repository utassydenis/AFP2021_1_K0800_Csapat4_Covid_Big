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

    def dir_exist(self):
        if not os.path.exists("database"):
            os.makedirs("database")

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

class CovidApp(App):
    def build(self):
        return Covid()
if __name__ == '__main__':
    CovidApp().run()