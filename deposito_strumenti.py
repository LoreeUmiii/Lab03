import csv #usare il reader
from operator import attrgetter
#import datetime

class Strumento:
    def __init__(self, codice, tipo, marca, anno, valore): #attributi privati
        self.__codice = codice
        self.__tipo = tipo
        self.__marca = marca
        self.__anno = int(anno)
        self.__valore = float(valore)

    @property #ordinare per marca
    def marca(self):
        return self.__marca

    @property #aggiungere uno strumento
    def codice(self):
        return self.__codice

    def __str__(self): #stampare tutto il deposito
        return f"Strumento: {self.__codice} di tipo: {self.__tipo}, marca: {self.__marca}, anno: {self.__anno}, valore: {self.__valore}"

class Prestito:
    def __init__(self, codiceP, data, codiceStrumento, cognomeAllievo):
        self.__codiceP = codiceP
        self.__data = data
        self.__codiceStrumento = codiceStrumento
        self.__cognomeAllievo = cognomeAllievo

    @property
    def codiceStrumento(self):
        return self.__codiceStrumento

    @property
    def codiceP(self):
        return self.__codiceP

    def __str__(self): #stampare il prestito
        return f"Prestito: {self.__codiceP} in data: {self.__data}. Strumento: {self.__codiceStrumento} in prestito a: {self.__cognomeAllievo}"

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []
        self.prestiti = []

    def __str__(self):
            info = f"=== Deposito: {self.nome} ===\n"
            info += f"Responsabile: {self.responsabile}\n"
            info += f"Strumenti totali registrati: {len(self.strumenti)}\n"

            if self.strumenti:
                info += "Elenco strumenti:\n"
                for s in self.strumenti:
                    info += f"  - {s}\n"
            else:
                info += "  (Nessuno strumento presente nel deposito)\n"

            info += f"Prestiti attivi: {len(self.prestiti)}\n"
            if self.prestiti:
                info += "Elenco prestiti:\n"
                for p in self.prestiti:
                    info += f"  - {p}\n"

            return info
    #FUNZIONA, TESTATA
    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as fileIn:
                reader = csv.reader(fileIn)
                for row in reader:
                    codice, tipo, marca, anno, valore = (
                        row[0].strip(), row[1].strip(),
                        row[2].strip(), row[3].strip(),
                        row[4].strip(),
                    )
                    strumento = Strumento(codice, tipo, marca, anno, valore)
                    self.strumenti.append(strumento)
            return self.strumenti
        except FileNotFoundError:
            return "File non trovato!! "

    #FUNZIONA, TESTATA
    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if not self.strumenti:
            codiceNuovo = 1
        else:
            codiceUltimo = self.strumenti[-1].codice.strip("S")
            codiceNuovo = int(codiceUltimo) + 1
        codiceFinale = f"S{codiceNuovo}"
        nuovoStrumento = Strumento(codiceFinale,tipo,marca,anno_acquisto,valore)
        self.strumenti.append(nuovoStrumento)
        return nuovoStrumento
    #FUNZIONA, TESTATA
    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.strumenti, key=attrgetter("marca"))

    #FUNZIONA, TESTATA
    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # Variabili di supporto
        strumentoTrovato = False
        codiceMax = 0

        for s in self.strumenti:
            if id_strumento == s.codice:
                strumentoTrovato = True
                break
        if not strumentoTrovato:
            raise Exception(f"Lo strumento con codice {id_strumento} non è stato trovato!! ")

        for p in self.prestiti:
            if id_strumento == p.codiceStrumento:
                raise Exception(f"Lo strumento: {id_strumento} è già stato prestato!! ")

        # Da problemi con i duplicati, ma sarebbe la forma più semplice non tenendone conto
        codicePrestito = f"P{(len(self.prestiti) + 1)}"

        # Metodo nuvovo:
        for p in self.prestiti:
            codiceP = int(p.codiceP.strip("P"))

            # Ultimo valore come max
            if codiceP > codiceMax:
                codiceMax = codiceP

        codicePrestito = f"P{codiceMax + 1}"

        prestito = Prestito(codicePrestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(prestito)
        return prestito

    #FUNZIONA, TESTATA
    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        prestitoDaEliminare = None

        for p in self.prestiti:
            if id_prestito == p.codiceP :
                prestitoDaEliminare = p

        if prestitoDaEliminare is None:
            raise Exception(f"Errore il seguente prestito: {id_prestito} non risulta essere nel database ")

        self.prestiti.remove(prestitoDaEliminare)
        #Aggiungere il modo per cambiare il codice univoco una volta terminato
        #un prestito.. FATTO NELLA FUNZIONE SOPRA
        return prestitoDaEliminare
