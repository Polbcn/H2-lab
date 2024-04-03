from SALICRUWRAPPER import *
import datetime
import time
import requests


# Main
if __name__ == '__main__':
    # headers = connect()
    # API = "https://api.equinox.salicru.com/"
    # #Try connect
    # response = requests.get(API+"plants/9114/realTime", headers=headers)
    # print(response.status_code)
    # print(response.text)

    print("Starting API connection")
    print("starting reading")
    while(True):
        print(get_all_values())
        print(get_inverterAlarms())
        print(realTime())
        time.sleep(60000)
    
