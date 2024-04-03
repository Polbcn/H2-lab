import requests
import time
import datetime
from dotenv import load_dotenv
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
        self.token = ""
        self.headers = {}

    # Functions
    # Connect API
    def connect_API(self):
        # endpoint
        url = "users/login"
        # User data
        myobj = {"email": USER, "password": PASSWORD, "appVersion": "web"}

        # Request
        response = requests.post(self.API+url, json = myobj)
        if(response.status_code != 200):
            if response.status_code == 401:
                raise ConnectionError("Error en la autenticación: "+str(response.status_code))
            raise ConnectionError("Error en la petición: "+str(response.status_code))
        elif(response.json()["token"] == None):
            raise ConnectionError("Error al obtener el token de autenticacion")
        else:
            self.token = response.json()["token"]
            self.headers = {"Authorization": f"Bearer {self.token}"}
            print("Conexión establecida")


    def update(self):
        try:
            lastread = self.realTime()
            self.timestamp = lastread["timestamp"]
            self.powerDailyGeneration = lastread["powerDailyGeneration"]
            self.powerDailyConsumption = lastread["powerDailyConsumption"]
            self.powerSelfConsumption = lastread["powerSelfConsumption"]
            self.inverterAlarms = lastread["inverterAlarms"]
            self.powerBattery = lastread["powerBattery"]
            self.stateOfCharge = lastread["stateOfCharge"]
            self.irr = lastread["irr"]
            print("Datos actualizados correctamente")
        except ConnectionError as e:
            print(e)
            return # En caso de error devuelvo void
        
    def realTime(self):
        url = "plants/"+str(self.plantId)+"/realTime"
        response = requests.get(self.API+url, headers=self.headers)
        if(response.status_code != 200):
            raise ConnectionError("Error en la petición: "+str(response.status_code))
        else:
            return response.json()
