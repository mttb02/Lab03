import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!
    try:
        txtIn = int(txtIn)
        if not 1 <= txtIn <= 4:
            raise ValueError
    except ValueError:
        raise ValueError("Inserire numero tra 1 e 4")

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"italian")
        sc.print_errori()
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"english")
        sc.print_errori()
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"spanish")
        sc.print_errori()
        continue

    if int(txtIn) == 4:
        break