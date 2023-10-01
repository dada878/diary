import subprocess

def runCommand(cmd):
    runner = subprocess.Popen([*cmd.split()], stdout=subprocess.PIPE, shell=True)
    return runner.communicate()[0].decode('utf-8')

while 1:
    path = runCommand('cd')
    command = input(f"{path[:-1].strip()} >> ")
    output = runCommand(command)
    print(output)