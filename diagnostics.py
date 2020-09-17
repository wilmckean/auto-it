from subprocess import Popen, check_output


class Diagnostics():

    def ping_check(address):
        '''
        Check to see if the destination is reachable.
        '''
        ping = Popen(f'ping {address}')
        ping.wait()
        if(ping.poll()):
            print("not reachable")
            return False
        else:
            print("reachable")
            return True