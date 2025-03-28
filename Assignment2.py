import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Importing Data
data = pd.read_csv('moisture_average_data.csv', header=None)
dataReap = pd.read_csv('moistureReap_average_data.csv', header=None)
dataInacc = pd.read_csv('adc_average_data.csv', header=None)
dataInacc = dataInacc.to_numpy()
dataReap  = dataReap.to_numpy()
data = data.to_numpy()
input = data[:, 0]
output = data[:, 1]
inputReap = dataReap[:, 0]
outputReap = dataReap[:, 1:4]
inputInacc = dataInacc[:, 0]
outputInacc = dataInacc[:, 1:3]
outputInaccAvg = dataInacc[:, 4]

## QUESTION 7
# Terminal Point Line
m = (output[-1] - output[0])/(input[-1] - input[0])
c = output[0]
xvals = np.linspace(input[0], input[-1], 26)
yvals = m*xvals + c


# Deviation Calculations
deviation = abs(yvals - output)
max_dev = max(deviation)
nonlinearity = (max_dev/max(output)) * 100
print(f"non-linearity = {nonlinearity:.4f}")

## QUESTION 10
# Each data points range caluclations
max_out = np.max(outputReap, axis = 1)
min_out = np.min(outputReap, axis = 1)
range_out = max_out-min_out


# Repeatability Calculations
repeatability = (range_out/(np.max(outputReap) - np.min(outputReap))) * 100
repeatability = np.mean(repeatability)
print(f"repeatability = {repeatability:.8f}")

# plt.scatter(input, output)
# plt.plot(xvals, yvals)
# plt.show()

# Inaccuracy
m = -58
c = 3800
print()
xvals = np.linspace(inputInacc[0], inputInacc[-1], 26)
yvals = m*xvals + c

deviation = abs(yvals - outputInaccAvg)
max_dev = max(deviation)
inaccuracy = (max_dev/(3800-900)) * 100
print(f"Inaccuracy = {inaccuracy:.8f}")


