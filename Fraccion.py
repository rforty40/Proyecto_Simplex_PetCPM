class Fraccion:
    # Constructor
    def __init__(self, numerador, denominador):
        if not denominador == 0:
            self.numerador = numerador
            self.denominador = denominador
        else:
            self.numerador = 0
            self.denominador = 0

    # Setters

    def setNumerador(self, numerador):
        self.numerador = numerador

    def setDenominador(self, denominador):
        self.denominador = denominador
    # Getters

    def getNumerador(self):
        return self.numerador

    def getDenominador(self):
        return self.denominador

    # Operaciones Basicas: SUMA, RESTA, MULTIPLICACION Y DIVISION
    def sumar(self, frac2):
        nuevoNum = (frac2.getNumerador()*self.getDenominador()) + \
            (frac2.getDenominador()*self.getNumerador())
        nuevoDen = frac2.getDenominador()*self.getDenominador()
        return Fraccion(nuevoNum, nuevoDen)

    def restar(self, frac2):
        nuevoNum = (self.getNumerador()*frac2.getDenominador()) - \
            (self.getDenominador()*frac2.getNumerador())
        nuevoDen = frac2.getDenominador()*self.getDenominador()
        return Fraccion(nuevoNum, nuevoDen)

    def multiplicar(self, frac2):
        nuevoNum = self.getNumerador()*frac2.getNumerador()
        nuevoDen = self.getDenominador()*frac2.getDenominador()
        return Fraccion(nuevoNum, nuevoDen)

    def dividir(self, frac2):
        nuevoNum = self.getNumerador()*frac2.getDenominador()
        nuevoDen = frac2.getNumerador()*self.getDenominador()
        return Fraccion(nuevoNum, nuevoDen)

    # Metodo para obtener el maximo comun divisor
    def mcd(self, frac):
        num = frac.getNumerador()
        den = frac.getDenominador()
        aux_num = 0
        aux_den = 0
        mcd = 0
        if not num == 0:
            if num < 0:
                num = -1*num
            if den < 0:
                den = -1*den

            if num > den:
                aux_num = num
                aux_den = den
            else:
                aux_num = den
                aux_den = num

            while(not aux_den == 0):
                mcd = aux_den
                aux_den = aux_num % aux_den
                aux_num = mcd
        else:
            mcd = 1

        return mcd

    def simplificar(self, frac):
        mcd = self.mcd(frac)
        frac.setNumerador(int(frac.getNumerador()/mcd))
        frac.setDenominador(int(frac.getDenominador()/mcd))

        if frac.getNumerador() < 0 and frac.getDenominador() < 0:
            frac.setNumerador(-1*frac.getNumerador())
            frac.setDenominador(-1*frac.getDenominador())
        elif frac.getNumerador() >= 0 and frac.getDenominador() < 0:
            frac.setNumerador(-1*frac.getNumerador())
            frac.setDenominador(-1*frac.getDenominador())
        return frac

    def __str__(self):
        if not self.getNumerador() == 0:
            self.simplificar(self)
            if self.getDenominador() == 1:
                return str(self.getNumerador())
            else:
                return str(self.getNumerador()) + "/"+str(self.getDenominador())
        else:
            return "0"
    

    def posicionBarra(self, cadena):
        return cadena.find("/")

    def deTablaFraccion(self, fraccionString):
        newFraccion = Fraccion
        posicionBarra = self.posicionBarra(fraccionString)
        numerador = ""
        denominador = ""

        if posicionBarra == -1:
            newFraccion = Fraccion(int(fraccionString), 1)
        else:
            numerador = fraccionString[0:posicionBarra]
            denominador = fraccionString[posicionBarra+1:len(fraccionString)]
            newFraccion = Fraccion(int(numerador), int(denominador))
        return newFraccion

    def getPuntoDecimal(self, decimalStr):
        return decimalStr.find(".")

    def getParInt(self, val):
        i = self.getPuntoDecimal(val)
        return val[0:i]

    def getPartDecimal(self, val):
        i = self.getPuntoDecimal(val)
        return val[i+1:len(val)]

    def factorMultiplicador(self, longitud):
        factorMultiplicador = "1"
        for i in range(0, longitud, 1):
            factorMultiplicador += "0"
        return int(factorMultiplicador)

    def toFraccion(self, decimal):
        newFraccion = Fraccion
        parInt = self.getParInt(str(decimal))
        partDecimal = self.getPartDecimal(str(decimal))
        num = int(parInt)
        den = int(partDecimal)
        if num < 0:
            den = -1*den
        factorMultiplicador = self.factorMultiplicador(len(partDecimal))
        if num == 0:
            newFraccion = Fraccion(den, factorMultiplicador)
        else:
            f1 = Fraccion(num, 1)
            f2 = Fraccion(den, factorMultiplicador)
            newFraccion = f1.sumar(f2)
        return newFraccion


    def toDecimal(self):
        decimal =0
        decimal = float(decimal)
        decimal = float(self.getNumerador())/float(self.getDenominador())
        return decimal
    #'''
    def devolverValorSR(self,stringDecimal):
        try:
            frac = Fraccion(0,0)
            decimal = float(0)
            if frac.posicionBarra(stringDecimal) == -1:
                decimal = float(stringDecimal)
            else:
                decimal = 1
            entero = int(decimal)  
            print("decimal --> "+str(decimal))
            print("entero --> "+str(entero)) 
            if decimal % entero == 0:
                return stringDecimal
            else:
                return frac.toFraccion(decimal).__str__()
        except ValueError:
            return "Dato vacio"
    