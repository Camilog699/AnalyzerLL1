class SetPrediction:

    # Constructor con las listas de primeros, siguientes y conjunto prediccion
    def __init__(self):
        self.dictFinal = {}

    def getSetPrediction(self, VT, VN, S, P, dictFirst, dictFollowing, dictGrammar):
        """
        Funcion encargada de almacenar las producciones de generadas por cada key
        """
        bigList = []
        word = ""
        tempKey = ""
        for x, y in dictGrammar.items():
            if x != tempKey:
                tempKey = x
                if self.checkRepeated(bigList):
                    return "Esta gramática NO es compatible para un analizador LL1"
                bigList = []
            for i in range(len(y)):
                word = y[i][0]
                if word in VT and word != "λ":
                    bigList.append([word])
                if word in VN:
                    for k, v in dictFirst.items():
                        if k == word:
                            bigList.append(v)
                if word == "λ":
                    for m, n in dictFollowing.items():
                        if m == x:
                            bigList.append(n)
            self.dictFinal[x] = bigList
        return "Esta gramática es compatible para un analizador LL1"

    def checkRepeated(self, lista):
        """
        Funcion encargada de generar la comparativa entre las sublistas
        """
        if len(lista) < 2:
            return False
        for i in range(len(lista) - 1):
            if not self.checkEqual(lista[i], lista[i + 1]):
                return False
        return True

    def checkEqual(self, list1, list2):
        """
        Funcion encargada de verificar si 2 listas son iguales
        """
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True
