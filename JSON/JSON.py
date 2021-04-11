import json
import os
from Resources.g import G

#Clase encargada de realizar la lectura del JSON entregado
class Lector:


    #Constructor de la clase Lector
    #self.g es el objeto Gramatica 
    #self.VT lista de terminales
    #self.VN lista de no terminales
    #self.S string con el simbolo inicial
    #self.P lista con las producciones
    
    def __init__(self):
        self.file = ""
        self.g = G()
        self.VT = []
        self.VN = []
        self.S = ""
        self.P = []

    #Funcion encargada de leer el JSON
    def readGrammar(self):
        if os.name is "posix":
            file = "JSON/grammar1.JSON"
            self.slash = "/"
        else:
            file = "JSON\\grammar1.JSON"
            self.slash = "\\"
        with open(file) as jfile:
            data = json.load(jfile)

        #Se realiza un recorrido por el archivo convertido en data
        for initial in data:
            if initial == "G":
                for element in data["G"]:
                    if element == "VT":
                        for k in data["G"]["VT"]:
                            self.VT.append(k)
                    elif element == "VN":
                        for i in data["G"]["VN"]:
                            self.VN.append(i)
                    elif element == "S":
                        self.S = data["G"]["S"]
                    elif element == "P":
                        for productions in data["G"]["P"]:
                            self.P.append(productions)
        #Se mandan todos los elementos a la funcion que generará los primeros
        self.g.getFirst(self.VT, self.VN, self.S, self.P)
