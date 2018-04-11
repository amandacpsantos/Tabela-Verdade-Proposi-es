class Operacoes(object):

    def __init__(self, string=None):
        self.__string = str(string)
        self.__listProp = []
        self.__numProp = 0
        self.__listLetras = []

    def getListLetters(self):

        for letra in self.__string:
            if letra.isalpha() is True and letra != "v":
                self.__listLetras.append(letra)

        self.__listLetras = list(set(self.__listLetras))
        return self.__listLetras

    def checkParentese(self):
        if self.__string.count("(") == self.__string.count(")"):
            return True
        else:
            return False

    def getByParentese(self):

        firt = self.__string.rfind("(")
        last = self.__string.find(")", firt)
        while firt != -1:
            #print(firt, last)

            propP = self.__string[firt + 1:last]
            self.__listProp.append(propP)
            self.__string = self.__string[0:firt] + str(self.__numProp) + self.__string[last + 1:]
            self.__numProp += 1
            #print(self.__string)

            firt = self.__string.rfind("(")
            last = self.__string.find(")", firt)

        return self.__listProp

    def getProposicao(self):
        return self.__string

    def getOperacoes(self, operacao):
        posicion = self.__string.find(operacao)

        if operacao != "~":


            while posicion != -1:
                first = 0
                last = 0

                # p^~p
                if self.__string[posicion+1] == "~" and self.__string[posicion-2] != "~":
                    propP = self.__string[posicion - 1:posicion + 3]
                    first = posicion - 1
                    last = posicion + 3

                # ~p^p
                elif self.__string[posicion+1] != "~" and self.__string[posicion-2] == "~":
                    propP = self.__string[posicion - 2:posicion + 2]
                    first = posicion - 2
                    last = posicion + 1

                #  ~p^~p
                elif self.__string[posicion+1] == "~" and self.__string[posicion-2] == "~":
                    propP = self.__string[posicion - 2:posicion + 3]
                    first = posicion - 2
                    last = posicion + 2

                #  p^p
                else:
                    propP = self.__string[posicion - 1:posicion + 2]
                    first = posicion - 1
                    last = posicion + 2

                self.__listProp.append(propP)
                self.__string = self.__string[0:first] + str(self.__numProp) + self.__string[last:]
                self.__numProp += 1

                posicion = self.__string.find(operacao)

        else:

            while posicion != -1:
                propP = self.__string[posicion:posicion + 2]
                self.__listProp.append(propP)
                self.__string = self.__string[0:posicion] + str(self.__numProp) + self.__string[posicion+2:]
                self.__numProp += 1
                #7p=~p
                posicion = self.__string.find(operacao)

        return self.__listProp

    def getNumProp(self):
        return self.__numProp

    def getListProp(self):
        return self.__listProp

    def gerarTabela(self):
        linha = 2 ** self.__listLetras.__len__()
        coluna = self.__listProp.__len__() + self.__listLetras.__len__()