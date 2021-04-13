from Resources.first import First
from Resources.following import Following
from Resources.setPrediction import SetPrediction

# Clase en encargada de manejar la gramatica para generar los primeros, siguientes y conjunto prediccion
class G:

    def __init__(self):
        """
        Constructor con los objetos de primeros, siguientes y conjunto prediccion
        """
        self.classFirst = First()
        self.classFollowing = Following()
        self.classSetPrediction = SetPrediction()


    def initial(self, VT, VN, S, P):
        """
        Funcion encargada de empezar el funcionamiento
        """
        self.classFirst.getFirst(VT, VN, S, P)
        self.classFollowing.getFollowing(
            VT, VN, S, P, self.classFirst.dictGrammarFinal, self.classFirst.dictFirst)
        self.show(VT, VN, S, P, self.classFirst.dictFirst,
                  self.classFollowing.dictFollowing, self.classSetPrediction.dictFinal)

    
    def show(self, VT, VN, S, P, dictFirst, dictFollowing, dictFinal):
        """
        Funcion encargada de generar la vista de los datos generados
        """
        print("PRIMEROS:")
        for x, y in dictFirst.items():
            print(x, "-->", y)

        print("___________________________________________________________________________")

        print("SIGUIENTES:")
        for x, y in dictFollowing.items():
            print(x, "-->", y)

        print("___________________________________________________________________________")

        var1 = self.classSetPrediction.getSetPrediction(
            VT, VN, S, P, self.classFirst.dictFirst, self.classFollowing.dictFollowing, self.classFirst.dictGrammar)

        print("CONJUNTO PREDICCIÓN:")
        for x, y in dictFinal.items():
            print(x, "-->", y)

        print("___________________________________________________________________________")
        print(var1)
