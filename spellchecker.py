import time

import multiDictionary as md


class SpellChecker:

    def __init__(self):
        self.language = ""
        self.words = []

        self.multi_dictionary = md.MultiDictionary()

        self.rich_parole = {"contains": [], "linear": [], "dichotomic": []}
        self.tempo = {"contains": 0.0, "linear": 0.0, "dichotomic": 0.0}


    def handleSentence(self, txtIn, language):
        self.language = language
        words = replaceChars(txtIn).lower().split(" ")

        start_contains = time.time()
        self.rich_parole["contains"] = self.multi_dictionary.searchWord(words, language)
        end_contains = time.time()
        self.tempo["contains"] = end_contains - start_contains

        start_linear = time.time()
        self.rich_parole["linear"] = self.multi_dictionary.searchWordLinear(words, language)
        end_linear = time.time()
        self.tempo["linear"] = end_linear - start_linear

        start_dichotomic = time.time()
        self.rich_parole["dichotomic"] = self.multi_dictionary.searchWordLinear(words, language)
        end_dichotomic = time.time()
        self.tempo["dichotomic"] = end_dichotomic - start_dichotomic


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def print_errori(self):
        for algoritmo_ricerca in self.rich_parole.keys():
            print("______________________________")
            print(f"Using {algoritmo_ricerca}")
            for parola in self.rich_parole[algoritmo_ricerca]:
                if not parola.corretta:
                    print(parola)
            print(f"Time elapsed: {self.tempo[algoritmo_ricerca]}")

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
