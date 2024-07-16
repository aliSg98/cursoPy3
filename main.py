from src.exceptions import convert
from src.Flight import Flight
from src.Aircraft import Aircraft
from src.conexion_posgressql import conexion_posgres

def main():
    #convert("two nine".split())
    #airtravel
    #f = Flight("SN9899")
    #f.set_number("Airbus677")
    #print(f.number())
    #aircraft
    #a = Aircraft("sb55","Airbus999",100,200) 
    #print(a.registration())
    conexion_posgres()


if __name__ == "__main__":
    main()