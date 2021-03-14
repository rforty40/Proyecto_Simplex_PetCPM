import Fraccion


class ClaseM:
    # Constructor
    def __init__(self, coeficiente, letraM):
        self.coeficiente = coeficiente
        self.letraM = str(letraM)

    # Setters

    def setCoeficiente(self, coeficiente):
        self.coeficiente = coeficiente

    def setLetraM(self, letraM):
        self.letraM = letraM

    # Getters
    def getCoeficiente(self):
        return self.coeficiente

    def getLetraM(self):
        return self.letraM

    def __str__(self):
        if self.coeficiente.__str__() == "0":
            return "0"
        else:
            return str(self.coeficiente.__str__())+str(self.letraM)

    def esM(self, m):
        m = str(m)
        hayM = m.find('M')
        if hayM == -1:
            return False
        else:
            return True

    def obtenerM(self, stringM):
        frac = Fraccion.Fraccion(0,0)
        clase = ClaseM(frac,"M")
        zjstring = stringM[0:len(stringM)-1]
        clase.setCoeficiente(frac.deTablaFraccion(zjstring))
        clase.setLetraM("M")
        return clase
        

    def obtenerValorSinM(self, M):
        valorSinM = ""
        fracOperacion = Fraccion.Fraccion(0,0)
        frac = Fraccion.Fraccion(0,0)
        hayM = M.find("M")
        if hayM == -1:
            valorSinM = M
        else:
            frac = frac.deTablaFraccion(M[0:hayM])
            frac = frac.multiplicar(Fraccion.Fraccion(10, 1))
            if not hayM == len(M) - 1:
                
                fracOperacion = fracOperacion.deTablaFraccion(
                    M[hayM+2:len(M)])
                if M[hayM+1] == '+':
                    frac = frac.sumar(fracOperacion)
                else:
                    frac = frac.restar(fracOperacion)
            valorSinM = frac.__str__()

        return valorSinM

    def sumaM(self, varM):
        return ClaseM(self.getCoeficiente().sumar(varM.getCoeficiente()), "M")

