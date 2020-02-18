import paramiko

nbytes = 4096
hostname = '0.tcp.ap.ngrok.io'
port = 15592
username = 'colab'
password = '4FCAhcksEiUmTL__cY6BDqI7kBf6JjE2xE6JsP3RfrY'
command = 'echo "sex"'

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect(hostname, port, username=username, password=password)

_, ss_stdout, ss_stderr = client.exec_command(command)
r_out, r_err = ss_stdout.readlines(), ss_stderr.read()

print(r_out)
print(r_err)

client.close()