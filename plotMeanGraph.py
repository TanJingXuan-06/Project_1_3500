import csv 
import matplotlib.pyplot as plt

def plot_moisture_graph(file):
    # reading csv file
    data = []
    
    with open('moisture_average_data.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting each data row one by one
        for row in csvreader:
            data.append(row)
        
        volume = [sublist[0] for sublist in data]
        volume = [int(v) for v in volume]
        moisture = [sublist[-1] for sublist in data]
        moisture = [float(m) for m in moisture]
    
    plt.plot([0,50],[0,100], color = "blue")
    plt.plot([0,50],[10,110], linestyle = '--', color = "red" )
    plt.plot([0,50],[-10,90], linestyle = '--', color = "orange" )
    plt.plot([0,50],[3,103], linestyle = 'dotted', color = "black" )
    plt.plot([0,50],[-3,97], linestyle = 'dotted', color = "grey" )    
        
    plt.scatter(volume,moisture, color = "red", s = 10)
    plt.legend(["Linear Line", "+10% Deviation", "-10% Deviation", "+3% Deviation", "-3% Deviation","Actual Data"], loc = 'best')
    plt.title("Moisture Over Volume Graph")
    plt.xlabel("Volume")
    plt.ylabel("Moisturity")
    plt.xlim(0,50)
    plt.ylim(0,100)
    plt.grid()
    
def plot_adc_graph(file):
    # reading csv file
    data = []
    
    with open('adc_average_data.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting each data row one by one
        for row in csvreader:
            data.append(row)
        
        volume = [sublist[0] for sublist in data]
        volume = [int(v) for v in volume]
        adc = [sublist[-1] for sublist in data]
        adc = [float(m) for m in adc]
    
    plt.plot([0,50],[3800,900], color = "blue")
    plt.plot([0,50],[4180,1280], linestyle = '--', color = "red" )
    plt.plot([0,50],[3420,520], linestyle = '--', color = "orange" )
    plt.plot([0,50],[3914,1014], linestyle = 'dotted', color = "black" )
    plt.plot([0,50],[3686,786], linestyle = 'dotted', color = "grey" )   
        
    plt.scatter(volume, adc, color = "red", s = 10)
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
    plt.savefig("Group B4 - Project 1 graphs (average)")
    plt.show()
        
if __name__ == '__main__':
    main()