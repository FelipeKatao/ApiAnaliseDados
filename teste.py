
def a(teste,*arg): # ('ola', 4, 5, 6)
    return str(arg)+str(teste)

def b(**args):  # {'c': '0', 'b': '90'}
    ListaChaves = []
    for i in args:
        ListaChaves.append(i)
    print(ListaChaves)
    for a in ListaChaves:
        print(args[a])
    return args

print(a("a","ola",4,5,6))
print(b(c="0",b="90"))

# (  ) Tupla 
# { } Objeto / Dicionario
# [ ]  Lista / Vetor