# Code used in experiments used for the thesis "Performance analysis of Battery-less LoRaWAN devices with Solar Harvesting"

This repository contains the code used for the different experiments used in the thesis.

A tutorial on how to set up the FiPy can be found at `https://docs.pycom.io/gettingstarted/`.

A basic FiPy project consists of 2 files: main.py and boot.py. These are the files provided for each experiment.

Experiment | Folder | Description
---|---|---
Disabling boot features | 1_OnBootFeatures | Enables/Disables feature in boot.py
CodeStructure  | 2_CodeStructure | Contains larger file showing longer boot time
Sleep | 3_Sleep | Full code with light sleep method (fast wakeup)
DeepSleep | 4_DeepSleep | Full code with deep sleep method (slow wakeup with lower sleep consumption)

Experiments 2, 3 and 4 all connect to the network before sending a packet. The credentials for connecting to the network need to be filled in first and are marked with a `TODO`.
The minimum voltage to succesfully execute a task can be calculated using `RequiredVoltage/requiredVoltage.py`

Remaining parameters include:
- required_voltage: minimum voltage required to send a task
- read_voltage_mult: multiplier for the read voltage that was divided by the voltage divider
- payload size
- datarate: 0-5 corresponding to SF12-SF7
- sleep_time: duration of the sleep state
- long_sleep_time: second sleep duration used when current_voltage < required_voltage
- save_nvram: whether to save the LoRaWAN session state to flash
- gpio_pin and adc_pin: determine the pins to be used for reading the capacitor voltage