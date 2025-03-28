import matplotlib.pyplot as plt
import csv 

def plot_moisture_graph(iter):
    
    moisture_data = []
    
    # reading csv file
    with open('moisture_data.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting each data row one by one
        for row in csvreader:
            moisture_data.append(row)
            
        plt.plot([0,50],[0,100], color = "blue")
        plt.plot([0,50],[10,110], linestyle = '--', color = "red" )
        plt.plot([0,50],[-10,90], linestyle = '--', color = "orange" )
        plt.plot([0,50],[3,103], linestyle = 'dotted', color = "black" )
        plt.plot([0,50],[-3,97], linestyle = 'dotted', color = "grey" )
        
        
        volume = [sublist[0] for sublist in moisture_data]
        volume = [int(v) for v in volume]
        
        
        if iter == 3 :             
            
            moisture1 = [sublist[1] for sublist in moisture_data]
            moisture2 = [sublist[2] for sublist in moisture_data]
            moisture3 = [sublist[3] for sublist in moisture_data]
            
            moisture1 = [float(m1) for m1 in moisture1]
            moisture2 = [float(m2) for m2 in moisture2]
            moisture3 = [float(m3) for m3 in moisture3]

     
            plt.scatter(volume, moisture1, color = "red", s = 10)
            plt.scatter(volume, moisture2, color = "black", s = 10)
            plt.scatter(volume, moisture3, color = "purple", s = 10)
            
            plt.legend(["Linear Line", "+10% Deviation", "-10% Deviation", "+3% Deviation", "-3% Deviation","Actual Data 1", "Actual Data 2", "Actual Data 3"])
                        
        if iter == 1 : 
            moisture = [sublist[-2] for sublist in moisture_data]
            moisture = [float(m) for m in moisture]
            plt.scatter(volume, moisture, color = "red", s = 10)
            plt.legend(["Linear Line", "+10% Deviation", "-10% Deviation", "+3% Deviation", "-3% Deviation","Actual Data"], loc = 'best')
        
        
        plt.title("Moisture Over Volume Graph")
        plt.xlabel("Volume")
        plt.ylabel("Moisturity")
        plt.xlim(0,50)
        plt.ylim(0,100)
        plt.grid()

def plot_adc_graph(iter):
    
    adc_data = []
    
    # reading csv file
    with open('adc_data.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting each data row one by one
        for row in csvreader:
            adc_data.append(row)
            
        plt.plot([0,50],[3800,900], color = "blue")
        plt.plot([0,50],[4180,1280], linestyle = '--', color = "red" )
        plt.plot([0,50],[3420,520], linestyle = '--', color = "orange" )
        plt.plot([0,50],[3914,1014], linestyle = 'dotted', color = "black" )
        plt.plot([0,50],[3686,786], linestyle = 'dotted', color = "grey" )   
        volume = [sublist[0] for sublist in adc_data]
        volume = [int(v) for v in volume]
        
        
        if iter == 3 :             
            
            adc1 = [sublist[1] for sublist in adc_data]
            adc2 = [sublist[2] for sublist in adc_data]
            adc3 = [sublist[3] for sublist in adc_data]
            
            adc1 = [float(m1) for m1 in adc1]
            adc2 = [float(m2) for m2 in adc2]
            adc3 = [float(m3) for m3 in adc3]

     
            plt.scatter(volume, adc1, color = "red", s = 10)
            plt.scatter(volume, adc2, color = "black", s = 10)
            plt.scatter(volume, adc3, color = "purple", s = 10)
            
            plt.legend(["Linear Line", "+10% Deviation", "-10% Deviation", "+3% Deviation", "-3% Deviation", "Actual Data 1", "Actual Data 2", "Actual Data 3"], loc = 'best')
                        
        if iter == 1 : 
            adc = [sublist[-1] for sublist in adc_data]
            adc = [float(a) for a in adc]
            plt.scatter(volume, adc, color = "red", s = 10)
            print("Hi")
            plt.legend(["Linear Line", "+10% Deviation", "-10% Deviation", "+3% Deviation", "-3% Deviation", "Actual Data"], loc = 'best')
        
        
        
        plt.title("ADC Over Volume Graph")
        plt.xlabel("Volume")
        plt.ylabel("ADC Value")
        plt.xlim(0,50)
        plt.ylim(900,4000)
        plt.grid()
        
        
def main():
    plt.figure(figsize=(12,4))
    plt.suptitle("GROUP B4 - Project 1", fontsize = 20)
    
    
    plt.subplot(1,2,1)
    plot_moisture_graph(1)
    
    plt.subplot(1,2,2)
    plot_adc_graph(1)
    
    plt.tight_layout(h_pad= 10)
    plt.savefig("Group B4 - Project 1 graphs")
    plt.show()
        
main()