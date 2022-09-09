import matplotlib.pyplot as plt

# Compare avg energy usage for different file configurations

d1 = [
1127,
1147,
1151,
1160,
1124,
1116,
1155,
1116,
1145,
1139,
1098,
]
   
d2 = [
1099,
1142,
1109,
1180,
1157,
1158,
1147,
1144,
1139,
1134,
1129,
]
    
d3 = [
1180,
1217,
1194,
1214,
1151,
1207,
1185,
1142,
1153,
1144,
1136,
]
    

data = [d1, d2, d3]

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = data[i][j] * 3.13 / 1000


plt.boxplot(data, labels=["3.6V", "3.65V", "3.7V"])
    
#plt.legend(["3.6V", "3.65V", "3.7V"])
plt.xlabel("Capacitor voltage (V)")
plt.ylabel("Voltage read by the device (mV)")
plt.show()
#plt.savefig("./plots/TaskCycleComparison.png")















