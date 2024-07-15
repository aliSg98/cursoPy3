class Aircraft:

    def __init__(self,registration:str,model:str,num_rows:int,num_seats:int):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats = num_seats

    def registration(self):
        return self._registration
    
    def num_seats(self):
        return self._num_seatss
    
