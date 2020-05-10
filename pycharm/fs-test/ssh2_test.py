import paramiko

ip='10.12.69.21'
port=22
username='ubuntu'
password='etrocks'

cmd='some useful command'
cmd='ls'


ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

stdin,stdout,stderr=ssh.exec_command('aws s3 ls dev-et-data/v1DRB_outputs/model_outputs/')
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)

print ('this many lines in a steffi dir',len(outlines))