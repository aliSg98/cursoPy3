from src.exceptions import convert
from src.airtravel import Flight

def main():
    convert("two nine".split())
    #airtravel
    f = Flight("SN9899")
    print(f.number())

if __name__ == "__main__":
    main()