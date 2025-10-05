def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        b = open(file_path, 'r', encoding = "utf-8") # apre il file
        tot_sezioni = int(b.readline()) # legge la prima riga

        biblioteca = {}
        for i in range(1,tot_sezioni+1): # tot_sezioni inclusa
            biblioteca[i] = [] # per ogni sezione i, creiamo una lista vuota

        for line in b:
            titolo, autore, anno, pagine, sezione = line.strip().split(",")
            libro = {"titolo":titolo, "autore":autore, "anno":int(anno), "pagine":int(pagine)}
            sezione_num = int(sezione)
            if sezione_num in biblioteca:
                biblioteca[sezione_num].append(libro)

        b.close() #chiudo il file
        return biblioteca

    except FileNotFoundError:
        return None


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    for libri in biblioteca.values(): # libri contiene la lista dei libri in quella sezione della biblioteca
        for libro in libri:
            if libro["titolo"].lower() == titolo.lower():
                return None

    if sezione not in biblioteca:
        return None

    nuovo_libro = {"titolo": titolo, "autore": autore, "anno": anno, "pagine": pagine} # salvo nuovo libro come dizionario
    biblioteca[sezione].append(nuovo_libro) # aggiunta del libro nella sezione della biblioteca

    try: # aggiorna il file, aprendolo in "aggiunta", senza eliminare il contenuto già presente nel file
        file = open(file_path, 'w', encoding = "utf-8")
        file.write(f"{titolo},{autore},{anno},{pagine},{sezione}\n")
        file.close()
        return biblioteca

    except FileNotFoundError:
        return None




def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    for (sezione,libri) in biblioteca.items(): # per ogni sezione della biblioteca # items restituisce sia la chiave che il valore
        for libro in libri: # per ogni libro della lista libri
            if libro["titolo"].lower() == titolo.lower():
                return f'{libro["titolo"]},{libro["autore"]},{libro["anno"]}, {libro["pagine"]},{sezione}'
            else:
                return None


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO

    if sezione not in biblioteca:
        return None

    libri = biblioteca[sezione]
    titoli = []

    for libro in libri:
        titoli.append(libro["titolo"]) # aggiunge il titolo del libro di ogni sezione alla lista da ordinare

    titoli.sort()
    return titoli


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

