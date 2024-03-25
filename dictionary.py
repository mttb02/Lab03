class Dictionary:
    def __init__(self, lingua):
        self._dict = []
        self.lingua = lingua

    def loadDictionary(self):
        with open(f"resources/{self.lingua}.txt", 'r', encoding='utf-8') as file_dizionario:
            for parola in file_dizionario:
                self._dict.append(parola.strip("\n"))
        return self

    def printAll(self):
        for parola in self._dict:
            print(parola+"\n")

    def __contains__(self, parola):
        if self.dict.__contains__(parola):
            return True
        else:
            return False


    @property
    def dict(self):
        return self._dict