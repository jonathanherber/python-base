#!/usr/bin/env python3

import os
import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("operacao: ")
    n1 = input("valor 1: ")
    n2 = input("valor 2: ")
    arguments = [operation,n1,n2]
elif len(arguments) != 3:
    print("numero de arg invalido")
    sys.exit(1)
    
operation,*nums = arguments

valid_operation = ("sum","difference","product","quotient")
if operation not in valid_operation:
    print("operacao invalida")
    sys.exit(1)

valida_nums = []
for num in nums:
    if not num.replace(".","").isdigit():
        print("numero invalido")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    valida_nums.append(num)
    
n1,n2 = valida_nums

if operation == "sum":
    result = n1 + n2
elif operation == "difference":
    result = n1 - n2
elif operation == "quotient":
    result = n1 / n2
elif operation == "product": 
    result = n1 * n2

path = os.curdir
filepath = os.path.join(path, "calculadora.log")

with open (filepath, "a") as file_:
    file_.write(f"{operation}, {n1},{n2} = {result}\n")

print(result)