#my_function.py

import socket
import sys

########################################################

def grafica():
    print()
    print("#########################################")
    print("#                                       #")
    print("# ##             ###       ###       ## #")
    print("# ##            #   #      ## #      ## #")
    print("# ##           #     #     ##  #     ## #")
    print("# ##          #       #    ##   #    ## #")
    print("# ##         ###########   ##    #   ## #")
    print("# ##        #           #  ##     #  ## #")
    print("# ##       #             # ##      # ## #")
    print("# ######## #             # ##       ### #")
    print("#                                       #")
    print("#########################################")

########################################################

#funzioni client

                ##########
                # CLIENT #
                ##########

def invia_mex(s):
    while True:
        comando = input("Inserire testo>>> ")
        temp = comando
        if comando == "exit":
            print()
            print("Chiudo la connessione col contatto...")
            s.close()
            break
        elif comando == "":
            print("Inserire una parola")
        else:
            s.send(comando.encode())
            data = str(s.recv(4096), "utf-8")
            if data == temp:
                print("Messaggio inviato")
                print()
            else:
                print("Errore")
                break
            
def conn_sub_server(indirizzo_server):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #creazione socket client
        s.connect(indirizzo_server)
        print("Connessione stabilita")
    except socket.error as errore:
        print(f"Connessione fallita {errore}")
        sys.exit()
    invia_mex(s)

#############################################################################

#funzioni server

                ##########
                # SERVER #
                ##########

def ricevi_mex(conn):
    while True:
        richiesta = conn.recv(4096)
        if not richiesta:
            print()
            print("Connessione chiusa...")
            print()
            conn.close()
            break
        else:    
            print("Messaggio>>> " + str(richiesta, "utf-8"))
            conn.send(richiesta)


def sub_server(indirizzo, backlog = 5):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(indirizzo)
        s.listen(backlog)
        print()
        print("Server inizializzato ora in ascolto.")
        print()
    except socket.error as errore:
        print(f"Errore: {errore}")
        print("Tentativo di reinizializzazione del Server")
        sub_server(indirizzo, backlog = 5)
    conn, indirizzo_client = s.accept()
    print(f"Connessione con il client stabilita: {indirizzo_client}")
    print()
    print("Messaggi ricevuti:")
    ricevi_mex(conn)
