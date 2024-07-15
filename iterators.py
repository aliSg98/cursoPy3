lista = ["summer", "winter", "Autum", "Spring"]
def iteration(iterable):
    iterable=iter(iterable)
    try:
        return print(next(iterable))
    except StopIteration:
        raise ValueError("Iterable empty")
    
iteration(lista)

