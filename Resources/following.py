class Following:

    # Constructor con las listas de primeros, siguientes y conjunto prediccion
    def __init__(self):
        self.dictFirst = {}
        self.following = []
        self.dictFollowing = {}
        self.dictGrammarFinal = {}
        self.dictFinal = {}

    def getFollowing(self, VT, VN, S, P, dictGrammarFinal, dictFirst):
        """
        Funcion que genera los siguientes
        """
        values = []
        wordSearch = ""
        word = ""
        #se realiza iteraciones por cada una de las producciones
        for productions in P:
            # se realiza un bucle en cada una de la key - values en las producciones
            for x, y in productions.items():
                #se iteran las producciones por cada elemento
                for value in y:
                    #se realiza un split para meter cada elemento en una lista
                    values.append(value.split())
        # se procede a iterar el diccionario para conseguir los primeros previamente hechos
        for x, y in dictFirst.items():
            #se vacia la lista de siguientes
            self.following = []
            #se iteran los values
            for i in range(len(values)):
                #se iteran los elementos de los values
                for j in range(len(values[i])):
                    #se verifica si la key es igual al value en el que se encuentra y si este
                    #es el ultimo seguido de un lambda
                    if x == values[i][j] and values[i][j] == "".join(values[i][-1:]):
                        #de ser así se guarda la key
                        word = x
                        # se verifica si la key esta en los no terminales
                        if word in VN:
                            #se itera el diccionario de gramatica general la cual contiene la key 
                            #y sus respectivas producciones
                            for m, n in dictGrammarFinal.items():
                                # se recorren los values
                                for char in n:
                                    # se verifica la key guardada es igual a alguno de estos caracteres
                                    if word == char:
                                        #se recorren los siguientes para agregarlos para la condicion de lambda
                                        for q, p in self.dictFollowing.items():
                                            #se recorren los values
                                            for elem in p:
                                                #se verifica si la key de las producciones es igual 
                                                # a las key de los siguientes
                                                if q == m:
                                                    #se verifica si el value se encuentra en la lista de siguientes
                                                    if elem not in self.following:
                                                        # si no está se agrega
                                                        self.following.append(elem)
                    # se verifica si la key es igual al elemento en el que se encuentra
                    elif x == values[i][j]:
                        #se guarda en una variable el siguiente a este
                        word = values[i][j + 1]
                        # se verifica si la variable es un valor terminal
                        if word in VT:
                            #se agrega el valor terminal
                            self.following.append(word)
                        #se verifica si la variable es un NO terminal
                        elif word in VN:
                            #se recorren los values
                            for k, v in dictFirst.items():
                                #se recorre cada elemento de los values
                                for elem in v:
                                    #se verifica si la variable tiene primeros
                                    if k == word:
                                        #se verifica si el value se encuentra en la lista de siguientes
                                        if elem not in self.following:
                                            # si no está se agrega
                                            self.following.append(elem)
            # se verifica si la x es simbolo inicial
            if x == S:
                #se agrega a los siguientes
                self.following.append("$")
            #se crea el diccionario para cada key
            self.dictFollowing[x] = self.following
