from itertools import islice

lista = ["summer", "winter", "Autum", "Spring"]
def iteration(iterable):
    iterable=iter(iterable)
    try:
        return print(next(iterable))
    except StopIteration:
        raise ValueError("Iterable empty")
    
iteration(lista)

#####islice
#crear iterable
data = range(10)
#desde el 2 al 7 sin incluir el 7
res = islice(data,2,7)
#convierto a lista
print(list(res))


####zip
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers2 = [12,34,5,6,7,8,9,10,11]
for item in zip(numbers,numbers2):
    print(item)
