# Reverse Shell  
This project demonstrates the functionality of a basic reverse shell, enabling command execution on a target system. It is intended for ethical hacking practice in controlled environments.  

## Features  
- Establishes a reverse connection to an attacker-controlled server.  
- Executes commands received from the server.  

## How to Use  
1. Replace the `server_ip` variable in the script with your own IP address.  
2. Start a listener on your machine using Netcat:  
   ```bash
   nc -lvnp 4444

Run the script on the target machine:

```bash 
python reverse_shell.py
