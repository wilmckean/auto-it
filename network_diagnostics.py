'''
Checks basic network functionality. 
'''
from subprocess import Popen
import speedtest
import socket

class NetworkDiagnostics():

    def check_internet_connection(connectTo='8.8.8.8', port=53, timeout=5):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((connectTo, port))
            print("T")
            return True
        except socket.error as err:
            print(err)
            return False

    def ping_check(addressToPing='8.8.8.8'):
        '''
        Check to see if the destination is reachable.
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
        Check to see if DNS is resolving.
        '''

        ns = Popen(f'nslookup {siteToCheck}')
        ns.wait()

        if(ns.poll()):
            print("DNS does not work")
            return False
        else:
            print("DNS works")
            return True

    def speedtest(timesToRun=1):
        '''
        Returns download[0], upload[1] and ping[2] rates in the form of a list.
        '''
        servers = []
        threads = None

        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.get_best_server()

        for i in range(timesToRun):

            s.download(threads=threads)
            s.upload(threads=threads)
            s.results.share()

            keys = ['download', 'upload', 'ping']
            results = [s.results.dict().get(k,{}) for k in keys]

            for val in range(len(results)):
                if val == 2:
                    results[val] = float("{:.2f}".format(results[val]))
                    continue
                results[val] = results[val] / (1024 ** 2)
                results[val] = float("{:.2f}".format(results[val]))
                
            return(results)