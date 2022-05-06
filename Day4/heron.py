#!/usr/bin/env python3

def heron(a, b, c):
    """Calcula a area de um triangulo"""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area**0.5  # math.sqrt(area)
    
triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
]
	
for t in triangulos:
    area = heron(*t)
    print(f"A area do triangulo é: {area}")