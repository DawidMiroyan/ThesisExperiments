import machine
import time
from network import LoRa
import struct
import socket
import ubinascii
# import os

# configuration parameters
abp = True # set to False to use OTAA
loraWAN = True # set to False to use LoRa RAW (manual lora configuration)
transmission_interval = 10 # in seconds
sleep_time = transmission_interval*1000
packet_count = 10 # total number of packets to send

# Allows us to exit the code using ctrl+c
time.sleep(1) 

def connect_loraWAN_abp():
    print("Connecting with ABP")
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    # TODO Enter credentials
    dev_addr = struct.unpack(">l", ubinascii.unhexlify(''))[0]
    nwk_swkey = ubinascii.unhexlify('')
    app_swkey = ubinascii.unhexlify('')
    
    lora.nvram_restore()
    if(lora.has_joined() == False):
        print("LoRa not joined yet")
        lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))  

    print('Joined')
    return lora

def connect_loraWAN_OTAA():
    print("Connecting with OTAA")
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    # create an OTAA authentication parameters, change them to the provided credentials

    # TODO Enter credentials
    app_eui = ubinascii.unhexlify('')
    app_key = ubinascii.unhexlify('')
    dev_eui = ubinascii.unhexlify('')

    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

    # wait until the module has joined the network
    while not lora.has_joined():
        time.sleep(5)
        print('Not yet joined...')

    print('Joined')
    return lora

def connect_loraRAW():
    power_mode = LoRa.ALWAYS_ON
    device_class = LoRa.CLASS_A
    lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868, power_mode=power_mode, device_class=device_class)
    return lora

def create_LoRa_socket(loraWAN):
     # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    if (loraWAN):
        # set the LoRaWAN data rate
        s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    
    return s

def lora_cb(lora):
    events = lora.events()
    tx_counter = lora.stats().tx_counter
    if events & LoRa.RX_PACKET_EVENT:
        print('Lora packet received')
    if events & LoRa.TX_PACKET_EVENT:
        print('Lora packet nr ' + str(tx_counter+1) + ' sent')
    if events & LoRa.TX_FAILED_EVENT:
        print('Lora packet transmission failed')

def connect_and_socket(loraWAN, abp):
    if (loraWAN):
        if (abp):
            lora = connect_loraWAN_abp()
        else:
            lora = connect_loraWAN_OTAA()
    else:
        lora = connect_loraRAW()
        
    s = create_LoRa_socket(loraWAN)

    # lora.callback(trigger=(LoRa.RX_PACKET_EVENT | LoRa.TX_PACKET_EVENT), handler=lora_cb)

    print("Connected and created socket")
    return lora, s


# abp, 3pkt, nblocking, nreboot
def experiment1():
    print("Running experiment 1: abp, 3pkt, nblocking, nreboot")

    lora, s = connect_and_socket(True, True)

    # send some data
    for i in range(packet_count):
        # send some data
        # print("Sending packet " + str(i))
        s.send(bytes([0x01, 0x02]))

        machine.sleep(sleep_time)
    print("Experiment done")

# abp, 3pkt, wblocking, nreboot
def experiment2():
    print("Running experiment 2: abp, 3pkt, wblocking, nreboot")
    lora, s = connect_and_socket(True, True)

    # send some data
    for i in range(packet_count):
        # make the socket blocking
        # (waits for the data to be sent and for the 2 receive windows to expire)
        s.setblocking(True)

        # send some data
        s.send(bytes([0x01, 0x02]))

        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        s.setblocking(False)
        # get any data received (if any...)
        data = s.recv(64)
        print(data)

        machine.sleep(sleep_time)
    print("Experiment done")

# abp, n pkt, nblocking, wreboot
def experiment3():
    print("Running experiment 3: abp, n pkt, nblocking, wreboot")
    lora, s = connect_and_socket(True, True)

    # send some data
    for i in range(packet_count):
        # send some data
        s.send(bytes([0x01, 0x02]))

        if (i < packet_count-1):
            machine.sleep(sleep_time)

    # Store lora state
    lora.nvram_save()

    # Deep Sleep
    machine.deepsleep(sleep_time)
    print("Experiment done")

# abp, n pkt, wblocking, wreboot
def experiment4():
    print("Running experiment 4: abp, n pkt, nblocking, wreboot")
    lora, s = connect_and_socket(True, True)

    # send some data
    for i in range(packet_count):
        # make the socket blocking
        # (waits for the data to be sent and for the 2 receive windows to expire)
        s.setblocking(True)

        # send some data
        s.send(bytes([0x01, 0x02]))

        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        s.setblocking(False)
        # get any data received (if any...)
        data = s.recv(64)
        print(data)

        if (i < packet_count-1):
            machine.sleep(sleep_time)

    # Store lora state
    lora.nvram_save()

    # Deep Sleep
    machine.deepsleep(sleep_time)
    print("Experiment done")
    

# OTAA, 3pkt, nblocking, nreboot
def experiment5():
    print("Running experiment 5: OTAA, 3pkt, nblocking, nreboot")
    lora, s = connect_and_socket(True, False)

    # send some data
    for i in range(packet_count):
        # send some data
        s.send(bytes([0x01, 0x02]))

        machine.sleep(sleep_time)
    print("Experiment done")

# OTAA, 3pkt, wblocking, nreboot
def experiment6():
    print("Running experiment 6: OOTA, 3pkt, wnblocking, nreboot")
    lora, s = connect_and_socket(True, False)

    # send some data
    for i in range(packet_count):
        # make the socket blocking
        # (waits for the data to be sent and for the 2 receive windows to expire)
        s.setblocking(True)

        # send some data
        s.send(bytes([0x01, 0x02]))

        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        s.setblocking(False)
        # get any data received (if any...)
        data = s.recv(64)
        print(data)

        machine.sleep(sleep_time)
    print("Experiment done")

# OTAA, n pkt, nblocking, wreboot
def experiment7():
    print("Running experiment 7: abp, n pkt, nblocking, wreboot")
    lora, s = connect_and_socket(True, False)

    # send some data
    for i in range(packet_count):
        # send some data
        s.send(bytes([0x01, 0x02]))

        if (i < packet_count-1):
            machine.sleep(sleep_time)

    # Store lora state
    lora.nvram_save()

    # Deep Sleep
    machine.deepsleep(sleep_time)
    print("Experiment done")

# OTAA, n pkt, wblocking, wreboot
def experiment8():
    print("Running experiment 8: abp, n pkt, wblocking, wreboot")
    lora, s = connect_and_socket(True, False)

    # send some data
    for i in range(packet_count):
        # make the socket blocking
        # (waits for the data to be sent and for the 2 receive windows to expire)
        s.setblocking(True)

        # send some data
        s.send(bytes([0x01, 0x02]))

        # make the socket non-blocking
        # (because if there's no data received it will block forever...)
        s.setblocking(False)
        # get any data received (if any...)
        data = s.recv(64)
        print(data)

        if (i < packet_count-1):
            machine.sleep(sleep_time)

    # Store lora state
    lora.nvram_save()

    # Deep Sleep
    machine.deepsleep(sleep_time)
    print("Experiment done")

# Run an experiment
experiment8()
