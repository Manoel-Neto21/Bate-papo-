import socket
import threading

HOST = '127.0.0.1'
PORT = 50000

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except:
        print("\nNão foi possivel conectar ao servidor!\n")

    print("para sair digite CTRL+X\n")
    print('\nConectado ')

    if username == '':
        username = 'Anonimo'
    
    #crias as threads para o usuario poder mandar e receber mensagens ao mesmo tempo
    thread1 = threading.Thread(target=receiveMsg,args=[s])
    thread2 = threading.Thread(target=sendMsg,args=[s, username])

    #inicia as threads
    thread1.start()
    thread2.start()

#função para enviar mensagens as servidor
def sendMsg(s, username):
    while True:
        try:
            msg= input("\n")
            s.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return
#função para tratar mensagens recebidas do servidor
def receiveMsg(s):
    while True:
        try:
            msg = s.recv(2048).decode('utf-8')
            print(msg +'\n')
        except:
            print('\nNão foi possivel conectar ao servidor!\n')
            print('Pressione <Enter> para Continuar...')
            s.close()
            break


# while msg != '\x18':
#     s.send(msg.encode())
#     r = s.recv(2048).decode()
#     print(r)
#     msg= input("Mensagem a enviar: ")
# print("Desconectado")
# s.close()

main()