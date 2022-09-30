import paramiko
import telnetlib


def ssh_login(host, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print(f'Login successful on {host}:{port} with username: {username}, password: {password}')
    except:
        print(f'Login failed with username: {username}, password: {password}')


def telnet_login(host, port ,username, password):
    host_url = f'http://{host}:{port}/'
    tn = telnetlib.Telnet(host_url)

    tn.read_until('Login: ')
    tn.write(username + '\n')
    tn.read_until('Password: ')
    tn.write(password + '\n')

    try:
        res = tn.expect(['Last login'])
        if res[0] > 0:
            print(f'Telnet login successful on {host}:{port} with username: {username}, password: {password}')
        tn.close()
    except EOFError:
        print(f'Login failed with username: {username}, password: {password}')


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 2200

    with open('default_creds.txt', 'r') as f:
        for line in f:
            vals = line.split()
            username = vals[0].strip()
            password = vals[1].strip()

            ssh_login(host, port, username, password)
            telnet_login(host, port, username, password)
