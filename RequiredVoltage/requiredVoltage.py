import math

def requiredVoltage(Ih, Req, t, C, Vt):
    # Calculate minimum voltage needed to succesfully execute a task
    # given the specifications of the setup 
    V0 = ((Vt - (Ih*Req*(1-math.exp((-t)/(Req*C))))) / (math.exp((-t)/(Req*C))))
    return V0

# All parameters in μ
Vt = 3600000        # μV    Minimum operating voltage
E  = 4120000        # μV    Maximum operating voltage
Ih = 7000            # μ     Harvesting current
C  = 1500000        # μF    Capacitance in microFarads

# Expects average consumption and total duration of the task
# in microamps and microseconds
# 95mA and 5s is then [95000, 5000000]
setups = {
    # "DR0 @3.3V": [95996, 4954000],
    # "DR1 @3.3V": [90595, 4600167],
    # "DR2 @3.3V": [88438, 4289667],
    # "DR3 @3.3V": [83550, 3831333],
    # "DR4 @3.3V": [80063, 3836333],
    # "DR5 @3.3V": [78637, 3834833],
    #"DR5 @3.5": [34880, 2878000],
    
    # "DR0 @3.35V":[62960, 4951167],
    # "DR0 @3.5V": [52184, 5001600],

    # "DR5 Large @3.3V" : [74000, 5725000],
    # "DR5 @3.35V": [46800, 2846000],
    # "DR5 @3.5": [34880, 2878000],
    # "Yes RX": [77170, 4740000],
    # "No RX": [76910, 3979000]

    # Full VD Setup
    # "DR0 @3.3V": [99496, 4773689],
    # "DR1 @3.3V": [102586, 3860471],
    # "DR2 @3.3V": [90273, 3827287],
    # "DR3 @3.3V": [83569, 3827475],
    # "DR4 @3.3V": [80416, 3822264],
    "DR5 @3.3V": [79171, 3826022],

    # No VD, No Actual Measuring
    # "DR0 @3.3V": [97958, 4774480],
    # "DR1 @3.3V": [100687, 3873398],
    # "DR2 @3.3V": [87693, 3973380],
    # "DR3 @3.3V": [81568, 3824788],
    # "DR4 @3.3V": [76371, 3960879],
    # "DR5 @3.3V": [76931, 3772980],
}

for key in setups:
    Ic = setups[key][0]
    t = setups[key][1]
    Req = E/Ic
    V = requiredVoltage(Ih, Req, t, C, Vt)
    # print(key, ": %.4f"%(V/1000000), "V")
    print("%.4f"%(V/1000000))
