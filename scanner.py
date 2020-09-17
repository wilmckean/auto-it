import socket, re, uuid
from sys import platform
from netifaces import (
    interfaces,
    ifaddresses,
    AF_INET
)

# TODO: Add Linux and OSX support

class GetHostInformation():
    def get_localhost_information(hostname):
        '''
        Scan Local host for basic information
        '''
        # TODO: Add IPv6

        ipv4_addresses = []
        operating_system = platform
        fqdn = socket.getfqdn()
        mac = ":".join(re.findall('..', '%012x' % uuid.getnode()))

        for interface in interfaces():
                for inet in ifaddresses(interface).get(AF_INET, ()):
                    ipv4_addresses.append(inet['addr'])

        host_data = {
            "hostname": hostname,
            "operating_system": operating_system,
            "fqdn": fqdn,
            "mac": mac,
            "ip_address_ipv4": ipv4_addresses[0],
            "link_local_ipv4": ipv4_addresses[1]
        }  
        return host_data