from SALICRUWRAPPER import *
import datetime
import time

# Main
if __name__ == '__main__':
    print("Starting API connection")
    init()

    print("starting reading")
    while(True):
        update()
        print(f"timestamp: {datetime.datetime.fromtimestamp(get_timestamp())}")
        print(f"powerDailyGeneration: {get_powerDailyGeneration()}")
        print(f"powerDailyConsumption: {get_powerDailyConsumption()}")
        print(f"powerSelfConsumption: {get_powerSelfConsumption()}")
        print(f"inverterAlarms: {get_inverterAlarms()}")
        print(f"powerBattery: {get_powerBattery()}")
        print(f"stateOfCharge: {get_stateOfCharge()}")
        print(f"irr: {get_irr()}")
        print(get_all_values()) 
        time.sleep(5)
    
