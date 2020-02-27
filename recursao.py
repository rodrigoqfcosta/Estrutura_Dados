'''
Existem dados que tem uma caracteristica especial
Chamamos de instancia o valor concredto que usamos ao chamar um método na
função
'''
def soma (a, b):
    print (f' Instancia: f({a}, {b})')
    return a+b

#Até aqui so tenho uma função na memoria, nao tenho uma instância rodando

print("Resultado:",soma(10, 32))
#ao executar o print acima, tenho uma instancia com 10 e 32

print("Resultado:", soma(soma(5,5), soma(12, 20)))
#para calcular o print acima, tenho 3 instancias a serem resolvidas

'''
Alguns dados possuem uma caractristica interessantes
Toda instância menor tem a mesma forma da instância maior
Uma forma de programar, para estes dados, usa o que chamamos de "recursão"
'''
def fat(n):
    print(f' Instancia: fat({n})')
    if n <= 1:
        return 1
    else:
        print(f'chamou: {n} * fat ({n-1})')
        return n*fat(n-1)
#exemplo: fat(4) na matemática, é o mesmo que a * fat (3)

print (fat(3))
'''
sempre é mais eficiente programar recursivamente.
A computação se apoia sobre trÊs pernas: correção, eficiência e elegância
a elegância Imre Simon
Correção: cumpre o prometido
eficiência: não perde tempo atoa
elegante: simples e limpo


Vamos mostrar um exemplo de código recursivo "ruim"
elegante, correto, porém "ineficiente"
'''
def fib (n):
    #print(f'Instãncia: fib({n})')
    if n <= 2:
        return 1
    else:
        #print(f'Chamada: fib({n-1}) + fib({n-2})')
        return fib(n-1) + fib(n-2)
print(fib(5))

#arrumando

dic = {}
def fib (n):
    #print(f'Instãncia: fib({n})')
    if n <= 2:
        return 1
    else:
        if n not in dic: #so calcula a recursão se n não está aqui
            dic[n] = fib(n-1) + fib(n-2)
        #print(f'Chamada: fib({n-1}) + fib({n-2})')
        return dic[n]
print(fib(60))

#Posso usar alguma biblioteca? Sim, lru_cache

from functools import lru_cache
@lru_cache(maxsize=None)
def fib (n):
    #print(f'Instãncia: fib({n})')
    if n <= 2:
        return 1
    else:
        #print(f'Chamada: fib({n-1}) + fib({n-2})')
        return fib(n-1) + fib(n-2)
print (fib(60))

#06/08/2019

def fat(n):
    if n <= 1:
        return 1 
    else:
        return n * fat(n-1) 
print (fat(4))

def fib(n):
    #print (f'Instância: fib({n})')
    if n <= 2:
        return 1
    else:
        #print (f'Chamada: fib ({n-1}) + fib ({n-2})')
        return fib(n-1) + fib(n-2)
print (fib(10))

#como remover as chamadas duplicadas
#Usando Estrutura de Dados!!!!
#Faça uma versão usando dicionários

dic = {}
def fib(n):
    if n <= 2:
        return 1
    else:
        if n not in dic: dic[n] = fib (n-1) + fib(n-2)
        return dic[n]

print(fib(100))
                
#Utilizando biblioteca 
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print (fib(100))


def fat(n):
    if n <= 1:
        return 1
    else:
        return n * fat(n-1)
print(fat(6))
