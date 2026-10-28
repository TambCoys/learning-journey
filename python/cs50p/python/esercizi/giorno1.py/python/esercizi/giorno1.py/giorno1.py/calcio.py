def esito(gol_casa, gol_trasferta):
    if gol_casa > gol_trasferta:
        return "1"
    elif gol_casa < gol_trasferta:
        return "2"
    else:
        return "X"


def punti(gol_casa, gol_trasferta):
    match esito(gol_casa, gol_trasferta):
        case "1":
            return (3, 0)
        case "2":
            return (0, 3)
        case "X":
            return (1, 1)


def main():
    risultato = input("Inserisci il risultato (es. 2-1): ")
    try:
        gol_casa, gol_trasferta = map(int, risultato.split("-"))
    except ValueError:
        print("Input non valido: usa il formato '2-1' con numeri non negativi.")
        return
    print(f"Esito: {esito(gol_casa, gol_trasferta)}")
    print(f"Punti: {punti(gol_casa, gol_trasferta)}")


if __name__ == "__main__":
    main()