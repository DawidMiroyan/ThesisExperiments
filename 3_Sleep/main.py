from time import sleep
import machine

############################
# configuration parameters #
############################

required_voltage = 3805 # in mV
read_voltage_mult = 2.93 # 2.882922535

payload_size = 3            # Size of the payload
datarate = 5                # The spreading factor SF7 = 5, SF12 = 0
confirmed_packet = True     # Confirmed packets for skipping Rx2
packet_count = 10

sleep_time = 10 * 1000              # 60s of sleep when voltage > required_voltage
long_sleep_time = sleep_time * 2    # 2m of sleep when  voltage < required_voltage

gpio_enable_time = 10/1000 # in ms
gpio_wait_time = 5/1000
gpio_pin = machine.Pin('P10', mode=machine.Pin.OUT, pull=None, alt=-1)

adc = machine.ADC()
adc_pin = adc.channel(pin='P16', attn=machine.ADC.ATTN_11DB)


def gpio_timeout_handler(alarm):
    gpio_pin.toggle()

# Calculating the supply voltage based on the read adc pin value
def read_voltage():
    adc_val = adc_pin.voltage()
    read_voltage = adc_val 

    return read_voltage

# Calculating the capacitor voltage of the circuit using GPIO pin
def cap_task():
    # Enable gpio pin
    gpio_pin.toggle()
    
    sleep(gpio_enable_time)
    cap_val = read_voltage()
    sleep(gpio_wait_time)
    gpio_pin.toggle()

    return cap_val

# Measure the voltage
voltage = (int) (cap_task() * read_voltage_mult)

# Check if the required voltage threshold of the task is satisfied
if (voltage < required_voltage):
    flag = 1
    sleep_time = long_sleep_time
else:
    flag = 0

import struct
import socket
import ubinascii
from network import LoRa

def connect():
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    # TODO Enter credentials
    dev_addr = struct.unpack(">l", ubinascii.unhexlify(''))[0]
    nwk_swkey = ubinascii.unhexlify('')
    app_swkey = ubinascii.unhexlify('')

    if not lora.has_joined():
        lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))  

    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, confirmed_packet)

    return lora, s

# # Connect to network
lora, s = connect()

for i in range(packet_count):
    # # # make the socket blocking
    # # # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)

    # # Send read voltage and low voltage flag
    val = ((voltage << bytes) + flag) << (5*payload_size)
    data = val.to_bytes(bytes, 'big')

    # # Send data
    s.send(data)

    # # # make the socket non-blocking
    # # # (because if there's no data received it will block forever...)
    s.setblocking(False)
    # # # get any data received (if any...)
    data = s.recv(64)
    # #print(data)

    # Sleep
    machine.sleep(sleep_time)
