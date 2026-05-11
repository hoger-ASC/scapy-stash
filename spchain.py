from scapy.all import *
import socket
import threading

threads = []
scanned = False

def port_scan(target, port, min_port):
  global scanned
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 ; TCP
    sock.settimeout(1)
    connected = sock.connect_ex((target_ip, port))
    if connected == 0:
      print(f"[~] Port {port} is open")
      sock.close()
    scanned = True

# Error logging
  except socket.gaierror:
    print(f"\n[~] Could not resolve hostname - {target} - (IP/DNS)\n")
  except socket.error:
    print(f"\n[~] Socket error; port {port}: {socket.error}\n")

# parameters & call

target_choice = input("[+] Scan IP or DNS: ")
if target_choice == "IP":
  target_ip = input("[+] Enter target IP: ")
else:
  target = input("[+] Enter target DNS: ")
  target_ip = socket.gethostbyname(target)  # Translation

min_port = int(input("[+] Enter minimum port: "))
port = int(input("[+] Enter maximum port (most: 65535): "))
port_scan(target_ip, port, min_port)

# Process threading

for port in range(min_port, port):
  t = threading.Thread(target=port_scan, args=(target_ip, port, min_port))
  threads.append(t)
  t.start()

for t in threads:
  t.join()

# Scapy packet sniffing
destination = target_ip

def make_callback(target_ip):
  def callback(packet):
      destination = packet[IP].dst
      DNS = target_ip
      try:
        print(f"\nDestination: {DNS}")
      except socket.herror:
        print(f"\nNo reverse DNS found | {destination}")
      if TCP in packet and packet[TCP].payload:
          print(f"[~] {str(packet[TCP].payload)}")
  return callback

def Sniff(target_ip, port, min_port):
    min_port = str(min_port)
    port = str(port)
    target_ip = str(target_ip)
    print("Sniffing with Scapy, press CTRL+C to cancel...")
    sniff(filter=f"tcp portrange {min_port}-{port} and ip and host {target_ip}", prn=make_callback, store=0)

if scanned:
    Sniff(target_ip, port, min_port)
    print("\nFinished sniffing instance")
