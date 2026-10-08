from deposito_strumenti import DepositoStrumenti
from datetime import datetime
#MANCANO I COMMENTI
def menu():
    print("\n--- MENU DEPOSITO STRUMENTI ---")
    print("1. Modifica nome del responsabile del deposito")
    print("2. Carica strumenti da file")
    print("3. Aggiungi un nuovo strumento (da tastiera)")
    print("4. Visualizza strumenti ordinati per marca")
    print("5. Presta uno strumento")
    print("6. Termina prestito strumento")
    print("7. Per visualizzare tutto il deposito per intero") #aggiunta della visuallizazione per intero
    print("8. Esci")
    return input("Scegli un'opzione >> ")

def main():
    deposito = DepositoStrumenti("Deposito Strumenti Civico", "Alessandro Visconti")

    while True:
        scelta = menu()
        #FUNZIONA, TESTATA
        if scelta == "1":
            nuovo_responsabile = input("Inserisci il nuovo responsabile: ").strip()
            deposito.responsabile = nuovo_responsabile
            print(f"Responsabil del deposito cambiato correttamente: {deposito.responsabile}")
        #FUNZIONA, TESTATA
        elif scelta == "2":
            while True:
                try:
                    file_path = input("Inserisci il path del file da caricare: ").strip()
                    deposito.carica_file_strumenti(file_path)
                    print(f"Deposito creato con successo! ") #piccolo controllo x il deposito
                    break
                except Exception as e:
                    print(e)
        #FUNZIONA, TESTATA
        elif scelta == "3":
            tipo = input("Tipo di strumento: ")
            marca = input("Marca: ")
            try:
                anno_acquisto = int(input("Anno di acquisto: ").strip())
                valore = float(input("Valore (euro): ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno e valore.")
                continue
            strumento = deposito.aggiungi_strumento(tipo, marca, anno_acquisto, valore)
            print(f"Strumento aggiunto: {strumento}")

        #FUNZIONA, TESTATA
        elif scelta == "4":
            strumenti_ordinati = deposito.strumenti_ordinati_per_marca()
            for s in strumenti_ordinati:
                print(f'- {s}')
        #FUNZIONA, TESTATO
        elif scelta == "5":
            id_strumento = input("ID strumento: ").strip()
            cognome_allievo = input("Cognome allievo: ").strip()
            data = datetime.now().date()
            try:
                prestito = deposito.nuovo_prestito(data, id_strumento, cognome_allievo)
                print(f"Prestito andato a buon fine: {prestito}") #PRESTITO A ME
            except Exception as e:
                print(e)
        #FUNZIONA, TESTATO
        elif scelta == "6":
            id_prestito = input("ID prestito da terminare: ")
            try:
                deposito.termina_prestito(id_prestito)
                print(f"Prestito {id_prestito} terminato con successo.")
            except Exception as e:
                print(e)
        # FUNZIONA, TESTATO
        #AGGIUNTA PERSONALE PER VEDERE IL CONTENUTO DEL DEPOOSITO DOPO AVER FATTO DELLE INTERAZIONI
        elif scelta == "7":
            print(f"{deposito.__str__()}")
        # FUNZIONA, TESTATO
        elif scelta == "8":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida!")

if __name__ == "__main__":
    main()
