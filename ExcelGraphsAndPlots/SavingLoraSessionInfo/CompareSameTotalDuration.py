import matplotlib.pyplot as plt
from data import taskUsage, taskDuration, sleepUsage

# Compare avg energy usage for different file configurations

tasks = [
    "sleep",
    # "sleep @3.5V",
    "deep0 \w",
    "deep0 \wo",
    "deep1",
    "deep2",
    "deep3",
    "deep4",
    # "deep0 \w @3.5V",
    # "deep1 \w @3.5V"
]
mi = 0
ma = 200

maxTaskDuration = int(max(taskDuration.values() ))
taskAvgs = dict()

for task in tasks:
    avgs = []
    taskTotalUsage = taskUsage[task]*taskDuration[task]
    for sleepDuration in range(mi, ma):
        avgs.append((taskTotalUsage+(sleepUsage[task]*(maxTaskDuration-taskDuration[task]+sleepDuration))) / (maxTaskDuration+sleepDuration))
    taskAvgs[task] = avgs

x = range(mi+maxTaskDuration, ma+maxTaskDuration)

for task in tasks:
    plt.plot(x, taskAvgs[task])
plt.legend(tasks)
plt.xlabel("Task cycle duration in ms (task+sleep)")
plt.ylabel("Average cycle consumption in mA")
plt.show()
# plt.savefig("./plots/ConstantTaskCycleDuration_3.5V.png")
