#! usr/bin/env python3

import os

class UI:
    version = "1.0"

    def __init__(self):
        pass

    def clearscreen(self):
        os.system('clear')

    def banner(self):
        self.clearscreen()
        print("                                             _            ")
        print(" _ __   _____      _____ _ __ _ __  _ __ ___| |_ ___ _ __ ")
        print("| '_ \ / _ \ \ /\ / / _ \ '__| '_ \| '__/ _ \ __/ _ \ '__|")
        print("| |_) | (_) \ V  V /  __/ |  | |_) | | |  __/ ||  __/ |   ")
        print("| .__/ \___/ \_/\_/ \___|_|  | .__/|_|  \___|\__\___|_|   ")
        print("|_|                          |_|                          ")
        print(" _              _ _    _ _   ")
        print("| |_ ___   ___ | | | _(_) |_ ")
        print("| __/ _ \ / _ \| | |/ / | __|")
        print("| || (_) | (_) | |   <| | |_ ")
        print(" \__\___/ \___/|_|_|\_\_|\__|")
        print("                             ")
        print("----------------------------------------------------------")

    def showmenu(self,options):
        print('select an option:',end='\n')
        for option in options:
            print(''.join(['\t[@]','%s\t----> %s'%option,]))
        else:
            print("----------------------------------------------------------")


if __name__ == "__main__":
    ui = UI()
    ui.clearscreen()
    ui.banner()
