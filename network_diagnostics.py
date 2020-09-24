'''
Checks basic network functionality. 
'''
from subprocess import Popen
import speedtest as st
import socket
from decimal import Decimal

class NetworkDiagnostics():

    def check_internet_connection(connectTo='8.8.8.8', port=53, timeout=5):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((connectTo, port))
            return True
        except socket.error as err:
            print(err)
            return False

    def ping_check(addressToPing='8.8.8.8'):
        '''
        Checks to see if a destination is reachable.
        '''
        ping = Popen(f'ping {addressToPing}')
        ping.wait()

        if(ping.poll()):
            print("destination not reachable")
            return False
        else:
            print("destination reachable")
            return True

    # Add traceroute for Linux
    def nslookup_check(siteToCheck='https://google.com'):
        '''
        Checks to see if DNS is resolving.
        '''
        ns = Popen(f'nslookup {siteToCheck}')
        ns.wait()

        if(ns.poll()):
            print("DNS does not work")
            return False
        else:
            print("DNS works")
            return True

    def speedtest():
        '''
        Returns download[0], upload[1] and ping[2] rates in the form of a list.
        '''
        servers = []
        threads = None

        s = st.Speedtest()
        s.get_servers(servers)
        s.get_best_server()

        s.download(threads=threads)
        s.upload(threads=threads)
        s.results.share()

        results = [s.results.download, s.results.upload, s.results.ping]

        # Formats the objects in the results list to have 2 decimal places.
        # Also converts download and upload from bits to Mbits
        for val in range(len(results)):
            if val == 2:
                results[val] = Decimal(str(results[val])).quantize(Decimal('1.00'))
                continue
            results[val] = results[val] / (1024 ** 2)
            results[val] = Decimal(str(results[val])).quantize(Decimal('1.00'))
        return(results)
    
    def speedtest_avgs(runs=5):

        download = Decimal('0.0')
        upload = Decimal('0.0')
        ping = Decimal('0.0')
        
        for run in range(runs):
            temp_list = NetworkDiagnostics.speedtest()
            download += Decimal(str(temp_list[0]))
            upload += Decimal(str(temp_list[1]))
            ping += Decimal(str(temp_list[2]))

        avg_dl = Decimal(str(download/runs)).quantize(Decimal('1.00'))
        avg_up = Decimal(str(upload/runs)).quantize(Decimal('1.00'))
        avg_ping = Decimal(str(ping/runs)).quantize(Decimal('1.00'))

        return str([avg_dl, avg_up, avg_ping])