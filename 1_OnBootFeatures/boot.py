import pycom

# Sets on boot method on/off for True/False value

pycom.pybytes_on_boot(False)
pycom.heartbeat_on_boot(False)
pycom.lte_modem_en_on_boot(False)
pycom.wifi_on_boot(False)
pycom.smart_config_on_boot(False)

