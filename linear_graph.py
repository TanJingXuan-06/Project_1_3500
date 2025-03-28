from matplotlib import pyplot as plt 
import csv 


def plot_linear_graph():
    
    data = []
    
    # reading csv file
    with open('initial_range_data.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        # extracting each data row one by one
        for row in csvreader:
            data.append(row)
            
    volume = [sublist[0] for sublist in data]
    volume = [int(v) for v in volume]
    initial_range_data = [sublist[-1] for sublist in data]
    initial_range_data = [float(a) for a in initial_range_data]
    
    
    plt.figure(figsize=(12,3))
    plt.plot([volume[0],volume[-1]],[initial_range_data[0],initial_range_data[-1]])
    plt.scatter(volume,initial_range_data,color = 'red')
    plt.legend(["Linear Line", "Initial Range Data"], loc = 'best')
    plt.title("Initial Range Data Over Volume Graph")
    plt.xlabel("Volume")
    plt.ylabel("Inital Range Data (volts)")
    plt.xlim(-5,55)
    plt.ylim(2.4,3.3)
    plt.grid()    
    plt.savefig("Group B4 - Initial Range Data Graph")
    plt.show()    
    
def main():
    
    plot_linear_graph()
    
if __name__ == '__main__':
    main()