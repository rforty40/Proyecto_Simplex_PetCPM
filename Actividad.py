class Actividad:
    # Constructores

    def __init__(self, identificador,detalle,listaPredecesores,to, tn, tp):
        self.__identificador = identificador
        self.__detalle = detalle
        self.__ti0 = 0
        self.__tj0 = 0
        self.__ti1 = 0
        self.__tj1 = 0
        self.__listaPredecesores = []
        dij = (to+(4*tn)+tp)/6
        self.__dij=round(dij)
        oij = pow(((tp-to)/6),2)
        self.__oij=round(oij,2)
        predecesores = listaPredecesores.split(",")
        for i in range(0, len(predecesores), 1):
            self.__listaPredecesores.append(predecesores[i])
        self.__listaSucesores=[]
        self.__MargenTotal=0
        self.__MargenLibre=0
       

    # Setters

    def setIdentificador(self, identificador):
        self.__identificador = identificador

    def setDetalle(self, detalle):
        self.__detalle = detalle

    def setTi0(self, ti0):
        self.__ti0 = ti0

    def setTj0(self, tj0):
        self.__tj0 = tj0

    def setTi1(self, ti1):
        self.__ti1 = ti1

    def setTj1(self, tj1):
        self.__tj1 = tj1

    def setlistaPredecesores(self, listaPredecesores):
        predecesores = listaPredecesores.split(",")
        for i in range(0, len(predecesores), 1):
            self.__listaPredecesores.append(predecesores[i])
    
    def setlistaSucesores(self, listaSucesores):
        if not listaSucesores=='':
            self.__listaSucesores.append(listaSucesores)



    # Getters
    def getIdentificador(self):
        return self.__identificador

    def getDetalle(self):
        return self.__detalle 

    def getTi0(self):
        return self.__ti0

    def getTj0(self):
        return self.__tj0

    def getTi1(self):
        return self.__ti1

    def getTj1(self):
        return self.__tj1

    def getlistaPredecesores(self):
        return self.__listaPredecesores
    
    def getlistaSucesores(self):
        return self.__listaSucesores

    def getDij(self):
        return self.__dij

    def getOij(self):
        return self.__oij

    def getMargenTotal(self):
        self.__MargenTotal= self.__tj1 - self.__ti0 - self.__dij
        return self.__MargenTotal

    def getMargenLibre(self):
        self.__MargenLibre= self.__tj0 - self.__ti0 - self.__dij
        return self.__MargenLibre