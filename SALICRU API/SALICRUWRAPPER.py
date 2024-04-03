import requests
import time
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
token = ""


# API URL
API = "https://api.equinox.salicru.com/"
#ID de planta
plantId = "9114"

def connect():
    # endpoint
    url = "users/login"
    # User data
    myobj = {"email": USER, "password": PASSWORD, "appVersion": "web"}
    # Request
    response = requests.post(API+url, json = myobj)
    if(response.status_code != 200):
        print("error: "+str(response.status_code))
        raise ConnectionError("Error en la conexion inicial: "+str(response.status_code))
    token = response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    return headers

headers = connect()

def realTime():
    url = "plants/"+plantId+"/realTime"
    response = requests.get(API+url, headers=headers)
    if(response.status_code != 200):
        print("error: "+str(response.status_code))
        raise ConnectionError("Error en la petición de datos: "+str(response.status_code))
    print(response.status_code)
    return response.json()

def get_inverterAlarms():
    return realTime()["inverterAlarms"]

def get_all_values():
    valuesdict = realTime()
    array = [valuesdict["timestamp"], 
             valuesdict["powerDailyGeneration"], 
             valuesdict["powerDailyConsumption"], 
             valuesdict["powerSelfConsumption"], 
             valuesdict["powerBattery"], 
             valuesdict["stateOfCharge"], 
             valuesdict["irr"],
             valuesdict["gridPower"]]
    return array