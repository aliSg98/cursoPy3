t = ["madrid", 'bcn', 'london']
print(type(t))

a = ("malaga", 123)

print(type(a))

colors = ';'.join(['aa','b','c'])
print(colors.split(';'))

h = {2,4,5}
print(type(h))

l = list(range(10,20))
#print(l)
for li in l:
   print(li)

s = [1,2,3,4,5]
for i in range(len(s)):
    print(s[i])

#print("Len: "+(str)(len(s)-1))
print(s[1:2])

words = "java html css react"
words.split()

print(words)


numbers = [14,65,78,2,3]
numbers.sort()
print(numbers)

#diccionarios
urls = {'google':'www.google.com','github': 'github.com'}
#print(type(urls))
g=dict(w=99,k=0)
urls.update(g)
print(urls)

dic = {'123':[1,2,3],
       'he':[3,4,5],
       'gh':[3,5,6]}
print(type(dic))

dic['123'] += [5,6,7]
print(dic)

#set
se = {123,"gg",22}
#print(type(se))
se.add(23)
se.update([45,76,88])
se.remove(45)
print(se)