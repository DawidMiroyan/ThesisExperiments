import matplotlib.pyplot as plt
from data import taskUsage, taskDuration, sleepUsage

# Compare avg energy usage for different file configurations
x = range(0, 200)
#tasks = [
#    "sleep",
    #"sleep @3.5V",
    # "deep0 \w",
    # "deep0 \wo",
    # "deep1",
    # "deep2",
    # "deep3",
    #"deep4",
    #"deep0 \w @3.5V",
    #"deep1 \w @3.5V"
#]
  
tasks = [  
    "sleep @3.3V",
    "deep @3.3V",
    "sleep @3.5V",
    "deep @3.5V",
]
    
taskAvgs = dict()

for task in tasks:
    avgs = []
    taskTotal = taskUsage[task]*taskDuration[task]
    for sleepDuration in x:
        avgs.append((taskTotal+(sleepUsage[task]*sleepDuration)) / (taskDuration[task]+sleepDuration))
    taskAvgs[task] = avgs

for task in tasks:
    plt.plot(x, taskAvgs[task])

plt.ylim(0, 40)
plt.legend(tasks)
plt.xlabel("Sleep duration (s)")
plt.ylabel("Average cycle consumption (mA)")
# plt.show()
plt.savefig("./plots/TaskCycleComparison.png")
