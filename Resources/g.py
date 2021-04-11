#Clase en encargada de manejar la gramatica para generar los primeros, siguientes y conjunto prediccion
class G:

    #Constructor con las listas de primeros, siguientes y conjunto prediccion
    def __init__(self):
        self.first = []
        self.dictFirst = {}
        self.first2 = []
        self.dictFirst2= {}
        self.following = []
        self.setPredict = []
        self.evalWord = ""
        self.evalWord2 = ""

    #Funcion encargada de generar los primeros a partir de los elementos entregados por el lector JSON
    def getFirst(self, VT, VN, S, P):
        #Se realiza un recorrido por cada uno de las producciones
        for productions in P:
            # se realiza un recorrido por cada Clave:Valor
            for x, y in productions.items():
                #Se realiza un vaciado de lista en cada iteracion
                self.first = []
                #se realiza un recorrido por cada uno de los Valores
                for value in y:
                    #se separa cada Valor en caracteres y se recorre
                    for char in value:
                        #si el caracter es igual a espacio se deja de iterar
                        if char == " ":
                            break
                        #se agrega a una variable caracteres hasta que se encuentre un espacio
                        self.evalWord = self.evalWord + char
                    #se hace un recorrido por la lista de no terminales
                    for noT in VN:
                        #se verifica si la variable a evaluar se encuentra en la lista de no terminales
                        if self.evalWord == noT:
                            self.first.append(self.getFirstWithNoT(VT, VN, S, P, self.evalWord))
                            #se vacia la palabra a evaluar
                            self.evalWord = ""
                    #se hace un recorrido por la lista de terminales
                    for T in VT:
                        #se verifica si la variable a evaluar se encuentra en la lista de terminales
                        if self.evalWord == T:
                            #si se encuentra, se agrega la variable a la lista de primeros
                            self.first.append(self.evalWord)
                            #se vacia la palabra a evaluar
                            self.evalWord = ""
                #se crea un diccionario con Clave (inicio de produccion) y con Valor (La lista de primeros de ese inicio de produccion)
                self.dictFirst[x] = self.first
        print("Primeros:", self.dictFirst)

    def getFirstWithNoT(self, VT, VN, S, P, word):
        self.evalWord2 = ""
        self.first2 = []
        for productions in P:
            for x, y in productions.items():
                if x == word:
                    for value in y:
                        for char in value:
                            if char == " ":
                                break
                            self.evalWord2 = self.evalWord2 + char
                        for noT in VN:
                            if self.evalWord2 == noT:
                                self.getFirstWithNoT(VT, VN, S, P, self.evalWord2)
                                self.evalWord2 = ""
                        for T in VT:
                            if self.evalWord2 == T:
                                self.first2.append(self.evalWord2)
                                self.evalWord2 = ""
                    self.dictFirst2[x] = self.first2
                    return self.dictFirst2[x]


    def getFollowing(self, VT, VN, S, P):
        pass




