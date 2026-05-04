#unencrypted-sniffer.py V 1.5 ~

from scapy.all import sniff, TCP, IP
import socket

def callback(packet):
    destination = packet[IP].dst

    try:
      DNS = socket.gethostbyaddr(destination)
      print(f"\nDestination: {DNS} | {destination}")
    except socket.herror:
      print(f"\nNo reverse DNS found | {destination}")
    if packet[TCP].payload:
      print(f"[~] {str(packet[TCP].payload)}")


def main():
    sniff(filter="tcp port 21 or tcp port 23 or tcp port 25 or tcp port 80 or tcp port 119 or tcp port 143", prn=callback, count=0,
store=0)

if __name__ == "__main__":
    main()
