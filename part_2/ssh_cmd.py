import paramiko


def ssh_command(ip, port, user, passwd, cmd):
    """The function connects to SSH-server
    and execute a command"""
    client = paramiko.SSHClient()
    # SSH-server has to accept ssh-key and establish a connection
    # (because we controll the both of ends of the connection
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    # if the connection is succeeded, execute the command
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())

# bandit.labs.overthewire.org:2220
# bandit0 / bandit0

if __name__ == '__main__':
    # getpass is for getting user's name
    # in the environment
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)




