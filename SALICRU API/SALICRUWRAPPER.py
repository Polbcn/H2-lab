import SALICRUAPI
import requests

# SALICRU API PYTHON WRAPPER
# Functions
api = SALICRUAPI.SALICRUAPI()
def init():
    api.connect_API()

def update():
    api.update()

# Setters
def set_plantId(plantId): 
    api.plantId = plantId

# Getters
# Get Plant ID
def get_plantId():
    return api.plantId

# Get token
def get_token():
    return api.token

# Get headers auth
def get_headers():
    return api.headers

# Obtener información de la planta
def get_plant_info():
    # endpoint
    url = "plants/me"
    # Request
    try:
        response = requests.get(api.API+url, headers=api.headers)
        if(response.status_code != 200):
            raise ConnectionError("Error en la petición: "+str(response.status_code))
    except ConnectionError as e:
        print(e)
        return
    return response.json()

# Obtener la ultima medida
def get_last_read():
    return api.realTime()

# MUST DO UPDATE TO GET THE LAST READ
# Get timestamp from lastread
def get_timestamp():
    return api.timestamp

# Get powerDailyGeneration from lastread
def get_powerDailyGeneration():
    return api.powerDailyGeneration

# Get powerDailyConsumption from lastread
def get_powerDailyConsumption():
    return api.powerDailyConsumption

# Get powerapiConsumption from lastread
def get_powerSelfConsumption():
    return api.powerSelfConsumption

# Get inverterAlarms from lastread
def get_inverterAlarms():
    return api.inverterAlarms

# Get powerBattery from lastread
def get_powerBattery():
    return api.powerBattery

# Get stateOfCharge from lastread
def get_stateOfCharge():
    return api.stateOfCharge

# Get irr from lastread
def get_irr():
    return api.irr

def get_all_values():
    array = [get_timestamp(),
             get_powerDailyGeneration(),
            get_powerDailyConsumption(),
            get_powerSelfConsumption(),
            get_powerBattery(),
            get_stateOfCharge(),
            get_irr()]
    return array