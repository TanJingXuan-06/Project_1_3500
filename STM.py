# should be serial_handler 
import serial
from serial.tools import list_ports
import time 
import matplotlib.pyplot as plt
import csv 

# define variable 
timeLst = [] ; 
voltageLst = [] ; 

# the target string to determine if STM 32 is connected 
STM32Name = "STMicroelectronics STLink Virtual COM Port"


def check_STM32_connectivity():
    """ 
    Attempts to find and connect to the STM32.
    
    Returns: 
        ListPortInfo: The STM32 port. 
        int: -1 if a port isn't found.
    """ 
    # get the list of ports
    listOfPorts = list_ports.comports()
    # loop through all the items in the list 
    for indexList in range (len(listOfPorts)) : 
        port = listOfPorts[indexList]   
        # convert the portName to string to use find()
        portNameStr = str(port)
        # find the index of the STM32 
        # if not found will return -1 
        if portNameStr.find(STM32Name) != -1 : 
            stm32_port = port
            return stm32_port 
            
        
    return -1 

def get_data() : 
    """ 
    Records and prints voltage reading from the sensor
    Gets 20 raw voltage data from the sensor including the mean of these 20 datas. 

    Returns: 
        Mean data received : if STM32 board is found.
        None: if STM32 board isn't found.
    """ 
    stm32_port = check_STM32_connectivity()
    
    if stm32_port == -1 :
        print("STM32 board not found. Please ensure it is connected.")
        return 
    
    try : 
        ser = serial.Serial(port =stm32_port.name, baudrate=115200 , timeout=1)    
        # print(f"Stm32 Connected to {stm32_port}") 
        ser.write(b"RUN")       #"Send RUN to STM32"
        time.sleep(0.5)
    
        while True:
                
            data_received = ser.readline().decode("utf-8").strip()
            
            # if STM sent any data 
            if data_received : 
                
                # can add to print any data that is being sent 
                
                # if the data is Mean Value 
                if "Mean Value" in data_received:
                    print("Single Measurement complete!")
                    return float(data_received[13::])        
        
    except KeyboardInterrupt or serial.SerialException:
        print("Error") 
        

def moisture(data) : 
    """ 
    Calculates moisture .
    
    Input:  
        Mean Data  

    Returns: 
        Moisture calculate from data 
    """
    
    min = 900 
    max = 3800
    
    mois = round(((1-(data-min)/(max-min))*100),4)
    
    if mois > 100 : 
        mois = 100 
        
    elif mois < 0 :
        mois = 0 
    
    return mois   


def moisture_status(value):
         
    if value >= 95:
        return "WET"
    
    elif value <= 5:
        return "DRY"
    
    else : 
        return "DAMP"
    
def data_reader():
    
    """ 
    Gets 3 sets of mean data 
    Calculate the mean of these 3 mean data. 
    Creates a CSV file [volume, raw mean 1, raw mean 2, raw mean 3, mean of mean]

    Returns: 
        NONE 
    """
    
    volume = int(input("How many ml is added? "))
    measurement_list = []
    csvList = []
    csvList.append(volume)
    
    adcList = [] 
    adcList.append(volume)
    numbeOfIteration = 1
    
    adc_sum = 0 
        
    # get 3 datas     
    for i in range(0,numbeOfIteration):
        
        # get data 
        data = get_data()
        
        # calculate moisture
        data_mois = moisture(data)
        
        # add to measurement list 
        measurement_list.append(data_mois)
        
        # add to adc adc list 
        adcList.append(data)
        
        adc_sum += data 
        
    adc_mean = adc_sum / numbeOfIteration 
    adc_mean = round(adc_mean,4)   
    adcList.append(adc_mean)     
        
    # find mean of mean 
    sum = 0
    for i in measurement_list : 
        sum += i 

    mean = sum / numbeOfIteration 
    mean =  round(mean,4)   
    
    # [volume,x,x,x,mean]
    csvList.extend(measurement_list)
    csvList.append(mean)
    moisture_stat = moisture_status(mean)
    csvList.append(moisture_stat)    
        
    print(f"\nThe last 3 mean data is: {measurement_list}% ")
    print(f"The average of the mean datas is {mean}% , moisture status: {moisture_stat} ")
    
    with open('moisture_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([csvList])
        
    with open('adc_data.csv', 'a', newline='') as csv_adc_file:
        writer = csv.writer(csv_adc_file)
        writer.writerows([adcList])
        

def main():
    
    """ 
    Continue asking user if he wants to continue getting data or not 

    Returns: 
        NONE 
    """
    
    while True : 
        try : 
            user_input = input("Y/N? ")
            if user_input == "Y" or user_input == "y" : 
                data_reader()
                
            else : 
                break 
            
        except ValueError: 
            continue 

if __name__ == '__main__':
    main()
    
    