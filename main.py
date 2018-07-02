#data di inizio progetto: 30/06/2018
#applicazione per invia e ricevere messaggio testuali in LAN

import sys
import my_function

#costanti
localhost = "0.0.0.0"     #server ip
port = 50006                #half-duplex port

###############################################################################

        #############
        # programma #
        #############
        
if __name__ == '__main__':      #programma lanciato come main
    while True:
        my_function.grafica()
        print()
        print("1) Ricevere messaggi")
        print("2) Inviare messaggi")
        print("3) Esci")
        try:
            scelta = int(input(">>> "))
        
            if scelta == 1:         #ricevere messaggio
                try:
                    my_function.sub_server((localhost, port))
                except ConnectionResetError:
                    #il client ha chiuso la connessione inaspettatamente
                    print()
                    print("Il client ha interrotto la connessione")
                    print()
                
            elif scelta == 2:       #inviare messaggio
                print()
                indirizzo_server = input("Inserire indirizzo IP del contatto>>> ")
                my_function.conn_sub_server((indirizzo_server, port))

            elif scelta == 3:
                print()
                print("Esco dal programma...")
                print()
                sys.exit()
                
            else:
                print()
                print("Inserire un comando giusto")
                print()
            
        except ValueError:
            print()
            print("Carattere inserito non ammesso")
            print()
