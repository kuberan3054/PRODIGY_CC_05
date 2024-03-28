#Task-5
import struct
import socket

def main():
    connection = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))

    while 1:
        raw_data,protocol = connection.rcvfrom(65536)
        dest_mac,src_mac,proto,data = ethernet_frame(raw_data)
        print("source : {} \nDestination : {} \nProtocol : {}".format(src_mac,dest_mac,proto))

#unpacking the ethernet frame
def ethernet_frame(data):
    dest_mac,src_mac,proto = struct.unpack('!6s 6s H',data[:14])
    return get_mac(dest_mac),get_mac(src_mac),socket.htons(proto),data[14:]

#Proper formatted MAC
def get_mac(byte_addr):
    mac = map('{:02x }'.format,byte_addr)
    return ':'.join(mac).upper()

main()
