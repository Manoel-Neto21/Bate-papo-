

import socket
from _thread import *
import threading
qui
HOST ='localhost'
PORT = 50000

#lista de clientes ativos no servidor
clients =[]

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #inicia o server e deixa ele aberto a conexões 
    try:
        s.bind((HOST, PORT))
        s.listen()
    except:
        return print("\n Não foi possivel iniciar o servidor!\n")

    #aceita as conexões dos clientes e adiciona a info do cliente na lista de clientes 
    while True:
        conn , addrs = s.accept()
        clients.append(conn)
        print('Conectado a ', addrs)

        #inicia a thread que vai executar as funções sobre os clientes no servidor
        thread1 = threading.Thread(target=msgReceivedTreatment,args=[conn])
        thread1.start()

#tratamento de mensagens dos clientes pelo servidor
def msgReceivedTreatment(conn):
    while True:
        try:
            msg = conn.recv(2048)
            broadcast(msg , conn)

        except:
            deleteClient(conn)

# quando algum usuario mandar uma mensagem essa função e ativada para mandar a mensagen a todos usuarios no server exceto o usuario que mandou a mensagem.
def broadcast(msg, conn):
    for users in  clients:
        if users != conn:
            try:
                users.send(msg)
            except:
                #se essa exceção for ativada quer dizer que o cliente esta indisponivel ou seja desconectado entao ele sera removido da lista de clientes
                deleteClient(users)


#remove um cliente da lista de cliente
def deleteClient(conn):
    clients.remove(conn)
        
main()