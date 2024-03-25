import timeit
from math import floor

import dictionary as d
import richWord as rw
import dictionary as d


class MultiDictionary:

    def __init__(self):
        self.dictionaries = {"italian": d.Dictionary("Italian").loadDictionary(), "english": d.Dictionary("English").loadDictionary(), "spanish": d.Dictionary("Spanish").loadDictionary()}

    def printDic(self, language):
        self.dictionaries.get(language).printAll()

    def searchWord(self, words, language):
        rich_parole_contains = []
        for parola in words:
            temp_richword = rw.RichWord(parola)
            if self.dictionaries.get(language).__contains__(parola):
                temp_richword.corretta = True
            else:
                temp_richword.corretta = False
            rich_parole_contains.append(temp_richword)
        return rich_parole_contains

    def searchWordLinear(self, words, language):
        rich_parole_linear = []
        for parola in words:
            temp_richword = rw.RichWord(parola)
            for p in self.dictionaries.get(language).dict:
                if p == parola:
                    temp_richword.corretta = True
            if temp_richword.corretta is None:
                temp_richword.corretta = False
            rich_parole_linear.append(temp_richword)
        return rich_parole_linear

    def searchWordDichotomic(self, words, language):
        rich_parole_dichotomic = []
        for parola in words:
            temp_richword = rw.RichWord(parola)
            esito = ricercaDicotomica(parola, self.dictionaries.get(language).dict)
            temp_richword.corretta = esito
            rich_parole_dichotomic.append(temp_richword)
        return rich_parole_dichotomic

def ricercaDicotomica(parola, dizionario):
    if len(dizionario) == 0:
        return False
    temp_parola = dizionario[floor(len(dizionario)/2)]
    if parola < temp_parola:
        esito = ricercaDicotomica(parola, dizionario[0:floor(len(dizionario)/2)])
    if parola > temp_parola:
        esito = ricercaDicotomica(parola, dizionario[0:floor(len(dizionario)/2)])
    if parola == temp_parola:
        return True
    return esito


