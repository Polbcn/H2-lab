import requests
import time
import datetime
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

class SALICRUAPI:
    def __init__(self, plantId = "9114"):
        # API URL
        self.API = "https://api.equinox.salicru.com/"
        #ID de planta
        self.plantId = plantId

    # Functions
    # Connect API
    def connect_API(self):
        # endpoint
        url = "users/login"
        # User data
        myobj = {"email": USER, "password": PASSWORD, "appVersion": "web"}

        # Request
        response = requests.post(self.API+url, json = myobj)
        print(response.text)
        self.token = response.json()["token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def update(self):
        lastread = self.get_last_read()
        self.timestamp = lastread["timestamp"]
        self.powerDailyGeneration = lastread["powerDailyGeneration"]
        self.powerDailyConsumption = lastread["powerDailyConsumption"]
        self.powerSelfConsumption = lastread["powerSelfConsumption"]
        self.inverterAlarms = lastread["inverterAlarms"]
        self.powerBattery = lastread["powerBattery"]
        self.stateOfCharge = lastread["stateOfCharge"]
        self.irr = lastread["irr"]
     
    def get_last_read(self):
        # Medidas de tiempo
        iniTime = int(time.time()-6000000)
        toTime = int(time.time()+6*60*1000)
        # Petición
        url = f"measures/{self.plantId}/minute/{iniTime}/{toTime}"
        response = requests.get(self.API+url, headers=self.headers)
        # Ultima medida
        actualMeasure = response.json()[len(response.json())-1]
        # Marca de tiempo de la ultima medida
        timestamp = actualMeasure["timestamp"]
        date = datetime.datetime.fromtimestamp(timestamp)
        # Devolver ultima medida en json
        return actualMeasure

    def get_multiple_reads(self, iniTime, toTime):
        # Petición
        url = f"measures/{self.plantId}/minute/{iniTime}/{toTime}"
        response = requests.get(self.API+url, headers=self.headers)
        # Devolver todas las medidas en json
        return response.json()