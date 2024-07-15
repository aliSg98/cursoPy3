class Flight:

    #constructor
    def __init__(self,number):
        #_number la _ para encapsulacion, proteger
        self._number = number

    #getter
    def number(self):
        return self._number

    #setter   
    def set_number(self, number: int):
        self._number = number
    

    