import csv 
import numpy as np 

def average(file) :
    
    raw_data = []
    compiled_data = []
    
    with open(file, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting each data row one by one
        for row in csvreader :
            raw_data.append(row)
            
    
    volume = [sublist[0] for sublist in raw_data]
    volume = [int(v) for v in volume]
    moisture = [sublist[1] for sublist in raw_data]
    moisture = [float(m) for m in moisture]
    
    for counter in range(0,len(moisture),3) : 
        
        sum = 0 
        
        raw_data = []
        raw_data.append(volume[counter])
        
        for i in range(0,3) : 
            
            actual_count = counter + i 
            
            sum += moisture[actual_count]
            raw_data.append(moisture[actual_count])
        
            
        mean = sum / 3 
        mean = round(mean,4)
        raw_data.append(mean)
        compiled_data.append(raw_data)
        
        if counter == 78 : 
            break 
        
    return compiled_data
        
def main() : 
    
    moisture = average('moisture_data.csv')  
    
    with open('moisture_average_data.csv', 'w', newline='') as csv_moisture_file:
        writer = csv.writer(csv_moisture_file)
        writer.writerows(moisture)
        
      
    adc = average('adc_data.csv')  
    
    with open('adc_average_data.csv', 'w', newline='') as csv_adc_file:
        writer = csv.writer(csv_adc_file)
        writer.writerows(adc)
    
    
        
        
main()
            
            
    
    
            