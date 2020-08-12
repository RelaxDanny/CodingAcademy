import dpkt
import socket
from functools import reduce
import statistics
import matplotlib.pyplot as plot

#The Acknowledge number == 0 and Flags : 0x002(SYN)
SYN = b'\x00\x00\x00\x00\xa0\x02\xa5d'
#34: 36 src port
#36: 38 des port
#38: 42 sequence number
SRC_IP = "130.245.145.12"
DES_IP = "128.208.2.198"

#Read the pcap file into a python list
f = open('LAB3.pcap', 'rb')
pcap = dpkt.pcap.Reader(f).readpkts()

num_of_tcp_flows = 0
src_ports = {}

# Find SYN
for packet in pcap:
#35~38 = src port and des port  
    if (packet[1])[6:9] == b'\x00#$':
        
        src_port = int.from_bytes((packet[1])[34:36], "big")
        des_port = int.from_bytes((packet[1])[36:38], "big")
        #{b'\xa9\xea': b'P*', b'\xa9\xec': b'P\xd9', b'\x00P': b'\xec\x8b', b'\xa9\xee': b'P\x98'}
        src_ports[src_port] = des_port
    if SYN in packet[1]:
        num_of_tcp_flows += 1
print("The number of TCP flows initiated by the sender is ", num_of_tcp_flows)


for src_port, des_port in src_ports.items():
    
    print("TCP flow between", SRC_IP, ":", str(src_port), "and", DES_IP, ":", str(des_port))

    #For the first 2 transactions after the TCP connection is set up (from sender to receiver),
    # get the values of the Sequence number, Ack number, and Receive Window size.
    
    packets_sent = {"transactions":0, "ws":0, "packets":[], "log":"Packet Sent"}
    packets_recv = {"transactions":0, "ws":0, "packets":[], "log":"Packet Received"}
    
    #Get the first 2 packets sent after set-up
    count_sent = 0
    tmp = []
    tmp2 = []
    counter = 0
    for packet in pcap:
        ethernet_ = dpkt.ethernet.Ethernet(packet[1])
        ip = ethernet_.data
        tcp = ip.data
        if int.from_bytes((packet[1])[34:36], 'big') == src_port and int.from_bytes((packet[1])[36:38], "big") == des_port:
            tmp.append(tcp)
            count_sent += 1
        if count_sent == 4:
            packets_sent["packets"].append(tmp[2])
            break
    print(packets_sent)
    count_recv = 0
    # Get the first 2 packets ACK-ed after set-up
    for packet in pcap:
        ethernet_ = dpkt.ethernet.Ethernet(packet[1])
        ip = ethernet_.data
        tcp = ip.data
        if int.from_bytes((packet[1])[34:36], 'big') == des_port and int.from_bytes((packet[1])[36:38], "big") == src_port:
            tmp2.append(tcp)
            count_recv += 1
        if count_recv == 3:
            packets_recv["packets"].append(tmp2[1])
            break
        
    for i in (1,2):
        print("\tTransaction", i, "after setup")
        for j in [packets_sent, packets_recv]:
            print("\t\t",j["log"])
            print("\t\t\tSequence number:", j["packets"][i-1].seq)
            print("\t\t\tAck number:", j["packets"][i-1].ack)
            print("\t\t\tReceive Window size in bytes:", j["packets"][i-1].win << j["ws"])