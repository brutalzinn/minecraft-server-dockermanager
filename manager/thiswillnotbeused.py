# import subprocess
# import socket
# HOST = '0.0.0.0'
# PORT = 5000
# sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sSocket.bind((HOST,PORT))
# sSocket.listen()
# print("Aguardando conexão com o mod.")
# conn, ender = sSocket.accept()
# print("Conectando em", ender)
# while True:
#     data = conn.recv(1024)
#     if not data:
#         print("Fechando a conexão")
#         conn.close()
#         break
#     s = subprocess.getstatusoutput(data.decode())
#     conn.sendall(str(s).encode())
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 5000))
s.listen(2)
conn, addr = s.accept()
print("accepted")
print(bytes.decode(conn.recv(1024)))