import paramiko
import subprocess
import pytest


server_ip = '192.168.56.102'
password = 'strax'
username = 'strax'

@pytest.fixture(scope='function')
def server():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command('iperf3 -s')
    if(stderr is not None):
        print(f"Error during creation of iperf server: {stderr}")
        

    yield ssh

    ssh.close()

@pytest.fixture(scope='function')
def client(server):
        iperf_command = f'iperf3 -c {server_ip}'
        process = subprocess.Popen(iperf_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()

        output = process.stdout.read().decode('utf-8')
        error = process.stderr.read().decode('utf-8')

        return {'output': output, 'error': error}
        