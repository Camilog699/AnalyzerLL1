#Clase en encargada de manejar la gramatica para generar los primeros, siguientes y conjunto prediccion
class G:

    #Constructor con las listas de primeros, siguientes y conjunto prediccion
    def __init__(self):
        self.first = []
        self.following = []
        self.setPredict = []

    #Funcion encargada de generar los primeros a partir de los elementos entregados por el lector JSON
    def getFirst(self, VT, VN, S, P):
        #Se realiza un recorrido por cada uno de las producciones
        for productions in P:
            # se realiza un recorrido por cada uno de los no terminales
            for x in productions.keys():
                # se realiza un recorrido por cada uno de los terminales
                for y in productions.values():
                    print(x, "=>", y)