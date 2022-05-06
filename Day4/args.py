#!/bin/usr/env python3

def soma(n1,n2):
    return n1-n2

valores = {"n2":15, "n1":10}
valores1 = (1,2)


print(soma(**valores))  #desempacotamento de dict

print(soma(*valores1))  #desempacotamento de tuple

param =  isinstance("texto",str)  #verificar se um param é determinado tipo
print(param)