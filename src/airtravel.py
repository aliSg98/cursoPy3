class Flight:

    #constructor
    def __init__(self,number):
        #_number la _ para encapsulacion, proteger
        self._number = number

    def number(self):
        return self._number