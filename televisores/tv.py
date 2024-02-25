class TV ():

    _numTV = 0

    def __init__ (self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None

        TV._numTV += 1
    
    def turnOn (self):

        self._estado = True

    def turnOff (self):

        self._estado = False
    
    def getEstado (self):

        return (self._estado)
    
    def canalUp (self):

        if self._estado and self._canal < 120:

            self._canal += 1

    def canalDown (self):

        if self._estado and 1 < self._canal:

            self._canal -= 1

    def volumenUp (self):

        if self._estado and self._volumen < 7:

            self._volumen += 1
    
    def volumenDown (self):

        if self._estado and self._volumen > 0:

            self._volumen -= 1
    
    def setMarca (self, marca):

        self._marca = marca
    
    def getMarca (self):

        return (self._marca)
    
    def setCanal (self, canal):

        if self._estado and 1 <= canal <= 120:

            self._canal = canal
    
    def getCanal (self):

        return (self._canal)

    def setPrecio (self, precio):

        self._precio = precio
    
    def getPrecio (self):

        return (self._precio)
    
    def setVolumen (self, volumen):

        if self._estado and 0 <= volumen <= 7:

            self._volumen = volumen
    
    def getVolumen (self):

        return (self._volumen)
    
    def setControl (self, control):

        self._control = control
    
    def getControl (self):

        return (self._control)
    
    @classmethod
    def setNumTV (cls, num):

        cls._numTV = num
    
    @classmethod
    def getNumTV (cls):

        return (cls._numTV)
    
if __name__ == "__main__":

    from marca import Marca; from control import Control

    marca = Marca ("a")

    tv1 = TV(marca, True)

    tv2 = TV(marca, False)

    tv3 = TV(marca, True)

    print(TV.getNumTV())

    TV.setNumTV (0)

    tv4 = TV(marca, False)

    print(TV.getNumTV())
