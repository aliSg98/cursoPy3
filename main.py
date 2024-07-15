from src.exceptions import convert
from src.Flight import Flight
from src.Aircraft import Aircraft

def main():
    convert("two nine".split())
    #airtravel
    f = Flight("SN9899")
    f.set_number("Airbus677")
    print(f.number())
    #aircraft
    a = Aircraft("sb55","Airbus999",100,200) 
    print(a.registration())

if __name__ == "__main__":
    main()