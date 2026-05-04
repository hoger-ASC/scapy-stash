def callback(packet):
    print(f"\nDestination: {packet[IP].dst}")
    if packet[TCP].payload:
      print(f"[~] {str(packet[TCP].payload)}")


def main():
    sniff(filter="tcp port 21 or tcp port 23 or tcp port 25 or tcp port 80 or tcp port 119 or tcp port 143", prn=callback, count=1,
store=0)

if __name__ == "__main__":
    main()
