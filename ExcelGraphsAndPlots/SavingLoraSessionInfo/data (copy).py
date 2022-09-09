# sleep         : 3s task followed by light sleep
# deep0 \w      : ~2.5s init + 3s task + ~150ms flash
# deep0 \wo     : ~2.5s init + 3s task
# deep1         : ~1.6s init + 3s task + ~150ms flash
# deep2         : ~1.3s init + 3s task + ~150ms flash
# deep3         : ~1.3s init + 3s task + ~150ms flash
# deep4         : ~1.2s init + 3s task + ~150ms flash

taskUsage = {
    "sleep": 36,
    "sleep @3.5V": 35,
    "deep0 \w": 74,
    "deep0 \wo": 75, 
    "deep1": 77,
    "deep2": 79,
    "deep3": 78.5,
    "deep4": 80,
    "deep0 \w @3.5V": 33.5,
    "deep1 \w @3.5V": 34,
}

# mA
sleepUsage = {
    "sleep": 3.05,
    "sleep @3.5V": 0.86,
    "deep0 \w": 0.3,
    "deep0 \wo": 0.3,
    "deep1": 0.3,
    "deep2": 0.3,
    "deep3": 0.3,
    "deep4": 0.3,
    "deep0 \w @3.5V": 0.3,
    "deep1 \w @3.5V": 0.3,
}

# s
taskDuration = {
    "sleep": 3.013,
    "sleep @3.5V": 3.013,
    "deep0 \w": 5.725,
    "deep0 \wo": 5.575,
    "deep1": 4.824,
    "deep2": 4.592,
    "deep3": 4.565,
    "deep4": 4.394,
    "deep0 \w @3.5V": 5.725,
    "deep1 \w @3.5V": 4.824,
}